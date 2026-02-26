from typing import Any, Dict
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
def _build_prompt(user_prompt: str) -> str:
   # realism: structure prompt; still unsafe if used incorrectly
   return f"Return ONLY a Python expression.\nUser: {user_prompt}\nExpression:"
def run(user_prompt: str) -> Any:
   prompt = _build_prompt(user_prompt)
   response = llm.invoke(prompt)
   text = (response.content or "").strip()
   # HIGH: evaluating dynamic model output
   result = eval(f"{text}")  # noqa: S307
   return result
def handler(event: Dict[str, Any]) -> Dict[str, Any]:
   user_prompt = (event.get("prompt") or "")
   out = run(user_prompt)
   return {"result": str(out)}
