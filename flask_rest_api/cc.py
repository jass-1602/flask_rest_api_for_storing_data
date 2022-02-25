from flask import request


from flask import request
from flask import Flask, request, redirect
app = Flask(__name__)
app.debug = True
from flask import request
@app.route('/login/<username>', methods=['GET'])
def login(username):
    return username
app.run()