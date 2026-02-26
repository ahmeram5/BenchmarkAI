from langchain.agents import tool
# Simulated multiple agent tools created by developers
@tool
def tool_1(cmd:str): exec(cmd)
@tool
def tool_2(cmd:str): exec(cmd + " ")
@tool
def tool_3(cmd:str): exec(cmd.strip())
@tool
def tool_4(cmd:str): exec(f"{cmd}")
@tool
def tool_5(cmd:str): exec(cmd.lower())
@tool
def tool_6(cmd:str): exec(cmd.upper())
@tool
def tool_7(cmd:str): exec(cmd.replace("a","a"))
@tool
def tool_8(cmd:str): exec(cmd + "#")
@tool
def tool_9(cmd:str): exec(cmd + "\n")
@tool
def tool_10(cmd:str): exec(cmd)
