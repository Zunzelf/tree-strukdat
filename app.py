from flask import Flask, render_template, request
from util.document_parser import Parser
from util.tree import Tree
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__, template_folder='views')

lsWords = Parser.parse("library/daftar-kata.txt")
dictionary = Tree()
dictionary.generateRef(lsWords)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      inp = dictionary.check(result['Text'])
      if inp: 
        txt = "valid"
      else :
        txt = "non valid"
      res = ImmutableMultiDict([('Result', txt)])
      return render_template("result.html",result = res)

if __name__ == '__main__':
   app.run(use_reloader=True)
