from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status/<currstatus>')

def status(currstatus):
    return "Pokemon Status"

@app.errorhandler(404)
def page_not_found(error):
    return "Opps, the URL you requested for does not exist",404

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9116, debug=True)
