from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from K3s Cluster! This is a Python Flask app running on a single node K3s Cluster.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
