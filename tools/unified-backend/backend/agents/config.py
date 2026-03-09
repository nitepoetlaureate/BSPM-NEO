from enum import Enum
from typing import Dict, List

class Department(Enum):
    EXECUTIVE = "executive"
    DESIGN = "design"
    NARRATIVE = "narrative"
    ART = "art"
    ENGINEERING = "engineering"
    LEVEL = "level"
    AUDIO = "audio"
    QA = "qa"

# Mapping of all 48 agents to their atomic departments
AGENT_DEPARTMENT_MAP: Dict[str, Department] = {
    # Executive
    "producer": Department.EXECUTIVE,
    "creative-director": Department.EXECUTIVE,
    "technical-director": Department.EXECUTIVE,
    "release-manager": Department.EXECUTIVE,
    "devops-engineer": Department.EXECUTIVE,
    
    # Design
    "game-designer": Department.DESIGN,
    "systems-designer": Department.DESIGN,
    "economy-designer": Department.DESIGN,
    "prototyper": Department.DESIGN,
    
    # Narrative
    "narrative-director": Department.NARRATIVE,
    "world-builder": Department.NARRATIVE,
    "writer": Department.NARRATIVE,
    "localization-lead": Department.NARRATIVE,
    
    # Art
    "art-director": Department.ART,
    "technical-artist": Department.ART,
    "ui-programmer": Department.ART,
    "ux-designer": Department.ART,
    
    # Engineering
    "lead-programmer": Department.ENGINEERING,
    "gameplay-programmer": Department.ENGINEERING,
    "engine-programmer": Department.ENGINEERING,
    "tools-programmer": Department.ENGINEERING,
    "network-programmer": Department.ENGINEERING,
    "security-engineer": Department.ENGINEERING,
    "ai-programmer": Department.ENGINEERING,
    
    # Level
    "level-designer": Department.LEVEL,
    "accessibility-specialist": Department.LEVEL,
    
    # Audio
    "audio-director": Department.AUDIO,
    "sound-designer": Department.AUDIO,
    
    # QA
    "qa-lead": Department.QA,
    "qa-tester": Department.QA,
    "performance-analyst": Department.QA,
    
    # Others / Misc (Categorized into best fit)
    "analytics-engineer": Department.QA,
    "community-manager": Department.EXECUTIVE,
}

# Departmental Rules Whitelist
# These rules are automatically appended to every agent in the department
DEPARTMENTAL_RULES: Dict[Department, List[str]] = {
    Department.ART: ["art-bible"],
    Department.ENGINEERING: ["gbvm-reference", "json-injection"],
    Department.DESIGN: ["game-pillars"],
    Department.NARRATIVE: ["character-standards"],
    Department.LEVEL: ["gbc-hardware-limits"],
    Department.QA: ["test-standards"]
}
