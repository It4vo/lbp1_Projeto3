from flask import Flask, request

app = Flask(__name__)

@app.before_request
