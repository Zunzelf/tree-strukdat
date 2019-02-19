from flask import Flask, request, render_template
from util.document_parser import Parser
from util.tree import Tree

app = Flask(__name__)

lsWords = Parser.parse("daftar-kata.txt")
dictionary = Tree()
dictionary.generateRef(lsWords)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    if dictionary.check(name):
        return "{}!".format("valid")
    else:
        return "{}!".format("tidak valid") 

@app.route('/input/')
def my_form():
    return render_template('main.html')

# @app.route('/input/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text     

if __name__ == '__main__':
    app.run(host = "192.168.137.1")