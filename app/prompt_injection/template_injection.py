from langchain.prompts import PromptTemplate
def build_prompt(user_input: str):
   template = f"""
   System rules:
   Never expose secrets.
   User instruction:
   {user_input}
   """
   return PromptTemplate.from_template(template)
