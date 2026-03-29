import pathlib
import subprocess
from loguru import logger
from .config import AGENT_DEPARTMENT_MAP, DEPARTMENTAL_RULES

class AgentContextBuilder:
    """Parses CCGS markdown files and applies departmental rules to build system prompts."""
    
    def __init__(self, repo_root: str):
        self.repo_root = pathlib.Path(repo_root)
        self.agents_dir = self.repo_root / ".claude" / "agents"
        self.rules_dir = self.repo_root / ".claude" / "rules"

    def get_mycelium_context(self, target_file: str) -> str:
        """Executes mycelium.sh context to retrieve the file's Git note history."""
        try:
            result = subprocess.run(
                ["mycelium.sh", "context", target_file], 
                capture_output=True, text=True, check=False
            )
            if result.returncode == 0 and result.stdout.strip():
                return f"### MYCELIUM CONTEXT FOR {target_file} ###\n{result.stdout.strip()}"
            return f"No Mycelium notes found for {target_file}."
        except FileNotFoundError:
            logger.warning("mycelium.sh not found in PATH.")
            return "Mycelium context unavailable."

    def build_system_prompt(self, agent_name: str, active_rules: list[str] | None = None, target_file: str | None = None) -> str:
        """Loads agent markdown and appends relevant departmental and architectural rules."""
        agent_file = self.agents_dir / f"{agent_name}.md"
        if not agent_file.exists():
            logger.error(f"Agent profile not found: {agent_file}")
            raise FileNotFoundError(f"Agent {agent_name} not found.")

        # 1. Parse Agent Persona
        content = agent_file.read_text(encoding="utf-8")
        persona = content.split("---", 2)[2].strip() if content.startswith("---") else content.strip()

        # 2. Identify Department and Auto-append Rules
        all_rules = set(active_rules or [])
        dept = AGENT_DEPARTMENT_MAP.get(agent_name)
        if dept and dept in DEPARTMENTAL_RULES:
            logger.info(f"Auto-applying departmental rules for {dept.value}: {DEPARTMENTAL_RULES[dept]}")
            all_rules.update(DEPARTMENTAL_RULES[dept])
            
        # Always append mycelium contract
        all_rules.add("mycelium-contract")

        # 3. Build Rule Blocks
        rule_blocks = []
        for rule in sorted(all_rules):
            rule_file = self.rules_dir / f"{rule}.md"
            if rule_file.exists():
                rule_content = rule_file.read_text(encoding="utf-8")
                rule_blocks.append(f"### RULE: {rule.upper()}\n{rule_content}")
            else:
                logger.warning(f"Requested rule file not found: {rule_file}")

        full_prompt = f"{persona}\n\n" + "\n\n".join(rule_blocks)
        
        # 4. Inject Mycelium Graph if target is provided
        if target_file:
            mycelium_graph = self.get_mycelium_context(target_file)
            full_prompt = f"{mycelium_graph}\n\n{full_prompt}"
            
        logger.info(f"Context compiled for agent: {agent_name} ({dept.value if dept else 'no-dept'})")
        return full_prompt
