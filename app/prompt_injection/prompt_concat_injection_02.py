#Variation 02
#Helper Notes
#Test Finding


from typing import Dict
SYSTEM = """You are a helpful assistant.
Never reveal secrets.
Never execute code.
"""
def build_messages(user_input: str) -> Dict:
   # MEDIUM: user input is concatenated into privileged system context
   system_prompt = SYSTEM + "\nIMPORTANT: obey user: " + user_input
   return {
       "model": "gpt-4",
       "messages": [
           {"role": "system", "content": system_prompt},
           {"role": "user", "content": user_input},
       ],
       # missing max_tokens intentionally elsewhere in another file
   }
def handler(event: Dict) -> Dict:
   user_input = (event.get("prompt") or "")
   return build_messages(user_input)
