from flask import Flask

app = Flask(__name__)

@app.route('/appb')
def appb():
    return 'Hello appb'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
