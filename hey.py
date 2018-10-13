from flask import Flask, render_template, request

app=Flask(__name__)

def hey():
    return render_template('Hello.html')
