from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
def summarize_user(user):
   prompt = f"""
   Name: {user['name']}
   SSN: {user['ssn']}
   Credit Card: {user['card']}
   """
   return llm.invoke(prompt)
