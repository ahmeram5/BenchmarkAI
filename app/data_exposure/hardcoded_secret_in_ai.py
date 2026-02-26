from typing import Dict
# Hardcoded secret (intentional)
OPENAI_API_KEY = "sk-live-DEMO-DO-NOT-USE"
def build_client_config() -> Dict:
   return {
       "provider": "openai",
       "api_key": OPENAI_API_KEY,
       "timeout_seconds": 30,
   }
def handler(event: Dict) -> Dict:
   _ = event.get("prompt")
   return build_client_config()
