memory_store = {}
def save_conversation(user_id, history):
   # sensitive history stored without protection
   memory_store[user_id] = history
