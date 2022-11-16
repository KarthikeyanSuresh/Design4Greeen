from flask import Flask
app = Flask(__name__)

@app.route("/")
def main:
  print("title")
  print("\n\n  body")
  
  
  
  __name__ == __main__
