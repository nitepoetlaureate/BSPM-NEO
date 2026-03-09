import pytest
import respx
from httpx import Response
from backend.agents.context_builder import AgentContextBuilder
from backend.agents.critic_loop import CriticLoopEngine

def test_context_builder_loads_agent(tmp_path):
    agents_dir = tmp_path / ".claude" / "agents"
    agents_dir.mkdir(parents=True)
    (agents_dir / "test-agent.md").write_text("---name: test---Persona Body")
    
    builder = AgentContextBuilder(str(tmp_path))
    prompt = builder.build_system_prompt("test-agent")
    assert "Persona Body" in prompt

def test_context_builder_appends_rules(tmp_path):
    agents_dir = tmp_path / ".claude" / "agents"
    rules_dir = tmp_path / ".claude" / "rules"
    agents_dir.mkdir(parents=True)
    rules_dir.mkdir(parents=True)
    
    (agents_dir / "actor.md").write_text("Actor Persona")
    (rules_dir / "rule1.md").write_text("Rule Content")
    
    builder = AgentContextBuilder(str(tmp_path))
    prompt = builder.build_system_prompt("actor", active_rules=["rule1"])
    assert "Actor Persona" in prompt
    assert "Rule Content" in prompt

@pytest.mark.asyncio
@respx.mock
async def test_critic_loop_consensus():
    # Mock the LLM endpoint
    url = "https://api.mockllm.com/v1/chat/completions"
    respx.post(url).mock(return_value=Response(
        200, 
        json={"choices": [{"message": {"content": "Approved. The logic is sound."}}]}
    ))
    
    engine = CriticLoopEngine(url, "fake_token")
    draft, critique = await engine.run_loop("actor_prompt", "critic_prompt", "do math")
    
    assert "Approved." in critique
    assert respx.calls.call_count == 2 # 1 for actor draft, 1 for critic response
