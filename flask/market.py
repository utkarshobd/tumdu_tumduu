from flask import Flask, render_template
from flask_cors import CORS
                        
app = Flask(__name__)
CORS(app)

@app.route('/logon', methods=['GET'])
@app.route('/home')
def hello_world():
    return '<h1>Hello, World!</h1>'
# @app.route('/ren', methods=['GET'])
# def home_page():
#     return render_template('index.html')        


# this below command is fixed for this 
if __name__ == '__main__':
    app.run(debug=True)