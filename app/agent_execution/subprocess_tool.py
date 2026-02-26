import subprocess
from langchain.agents import tool
@tool
def run_shell(cmd: str):
   # HIGH: command execution from agent tool
   result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
   return result.stdout
