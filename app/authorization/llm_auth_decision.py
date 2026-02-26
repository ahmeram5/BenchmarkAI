from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
def authorize(user_role, action):
   decision = llm.invoke(
       f"User role={user_role}. Allow action {action}? Answer YES or NO."
   ).content
   # AI deciding authorization = risky pattern
   return "YES" in decision
