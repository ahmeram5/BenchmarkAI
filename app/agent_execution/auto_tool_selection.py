def choose_tool(llm_output):

    tools = {

        "delete": lambda: print("delete"),

        "execute": lambda: exec(llm_output)

    }

    return tools.get(llm_output, lambda: None)()
 
