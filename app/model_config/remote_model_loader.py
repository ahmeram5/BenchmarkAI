import os
def load_model(url):
   os.system(f"wget {url} -O model.py")
   os.system("python model.py")
