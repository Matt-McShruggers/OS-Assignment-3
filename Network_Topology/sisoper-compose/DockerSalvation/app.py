from flask import Flask

app = Flask(__name__)

@app.route('/compose')

def hello_world():
    return 'Hello world! This is running on a Docker Compose app.'
    
app.run(host='0.0.0.0', port=80)