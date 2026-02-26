from typing import Dict, List
def build_request(messages: List[Dict[str, str]]) -> Dict:
   req = {
       "model": "gpt-4",
       "messages": messages,
       # MEDIUM: max_tokens/max_output_tokens intentionally omitted
       # "max_output_tokens": 256,
   }
   return req
def handler(event: Dict) -> Dict:
   prompt = (event.get("prompt") or "")
   messages = [{"role": "user", "content": prompt}]
   return build_request(messages)
