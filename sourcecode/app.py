from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html'), 200

@app.route('/status/<currstatus>')

def status(currstatus):
    return "Pokemon Status"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9116, debug=True)
