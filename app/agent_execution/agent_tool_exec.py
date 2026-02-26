from typing import Any, Dict
from langchain.agents import tool
# --- Helpers (padding + realism) ---
def _normalize(text: str) -> str:
   return (text or "").strip()
def _audit(event: Dict[str, Any]) -> None:
   # placeholder: pretend we log telemetry
   _ = event.get("request_id")
   _ = event.get("user")
@tool
def python_repl(command: str) -> str:
   """
   Insecure tool: executes arbitrary Python.
   This is intentionally unsafe and should be flagged as HIGH.
   """
   cmd = _normalize(command)
   if not cmd:
       return "no-op"
   # HIGH: arbitrary code execution
   exec(cmd, globals())  # noqa: S102
   return "executed"
def handler(event: Dict[str, Any]) -> Dict[str, Any]:
   _audit(event)
   user_input = event.get("prompt", "")
   # pretend the agent selected this tool based on user input
   python_repl(user_input)
   return {"ok": True}
