from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def hey():
    return render_template('Hello.html')
app.run(debug=True)
