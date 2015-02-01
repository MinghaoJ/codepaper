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
app.config['PROPAGATE_EXCEPTIONS'] = True

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
            file.save(os.path.join(path, filename))
            head = gp.makeGraph()
            eval.inputNodes = []
            nodes = eval.seekInputNodes(head)
            eval.functionNodes = []
            f_nodes = eval.seekFunctionNodes(head)
            print nodes
            return render_template('input.html', val='value', nodes=nodes)
    return send_from_directory(path, 'static/index.html')
   
@app.route('/input', methods=['GET', 'POST'])
def input():
    head = gp.makeGraph()
    eval.inputNodes = []
    nodes = eval.seekInputNodes(head)
    eval.functionNodes = []
    f_nodes = eval.seekFunctionNodes(head)
    inp = []
    for node in nodes:
        if "input_" + node.name in request.form:
            inp.append(request.form["input_" + node.name])
    return eval.evaluate(head, eval.setInputs(inp))


def uploaded_file(filename):
    return send_from_dictionary(app.config['UPLOAD_FOLDER'], filename)

app.run()
