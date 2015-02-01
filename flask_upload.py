import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import GraphParse as gp
import functions as fn
import eval
#from app import app

path = os.getcwd()
UPLOAD_FOLDER = path + '/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename("image.jpg")
            print filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            head = gp.makeGraph()
            nodes = eval.seekInputNodes(head)
            return render_template('input.html', val='value', nodes=nodes)
    return send_from_directory(path, 'static/index.html')
   
@app.route('/input', methods=['GET', 'POST'])
def input():
    head = gp.makeGraph()
    nodes = eval.seekInputNodes(head)
    input = []
    for node in nodes:
        input.append(request.form["input_" + node.name])
    eval.setInputs(input, nodes)
    return eval.evaluate(head)
def uploaded_file(filename):
    return send_from_dictionary(app.config['UPLOAD_FOLDER'], filename)

app.run()
