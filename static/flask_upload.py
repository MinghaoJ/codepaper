import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import GraphParse as gp
import functions as fn
import eval
from app import app

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
            filename = secure_filename(file.filename)
            print filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            head = gp.makeGraph()
            eval.evaluate(head)
    return send_from_directory(path, 'index.html')
    
def uploaded_file(filename):
    return send_from_dictionary(app.config['UPLOAD_FOLDER'], filename)

def index(nodes):
    for nodes in 
    return render_template('subindex.html', val='value')
    
app.run()