import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
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
            return redirect(url_for('upload_file', filename=filename))
    return send_from_directory(path, 'index.html')


def uploaded_file(filename):
    return send_from_dictionary(app.config['UPLOAD_FOLDER'], filename)
    
app.run()