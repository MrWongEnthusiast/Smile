from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'The Official Mr Stevenson Fan Page'


app.run(host='0.0.0.0')
