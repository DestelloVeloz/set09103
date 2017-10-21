from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome To Pokemon!"

@app.route('/status/<currstatus>')

def status(currstatus):
    return "Pokemon Status"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9116, debug=True)
