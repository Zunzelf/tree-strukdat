from flask import Flask, render_template, request

app = Flask(__name__, template_folder='views')

@app.route('/')
def main_web():
   return render_template('main2.html')

if __name__ == '__main__':
   app.run()