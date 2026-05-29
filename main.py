from flask import Flask,render_template,request,redirect, url_for,flash
import os,uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create',methods=['GET','POST'])
def create():
    myid = str(uuid.uuid1())
    
    if request.method == 'POST':
        print(request.files.keys())
        desc = request.form.get('text')
        user_id = request.form.get('uuid')
        print(user_id)
            
        for key,val in request.files.items():
            file = request.files[key]
            if file:
                folder_path = os.path.join(app.config['UPLOAD_FOLDER'], user_id)
                os.makedirs(folder_path, exist_ok=True)
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],user_id, filename))

            with open(os.path.join(app.config['UPLOAD_FOLDER'],user_id,"desc.txt"),"w") as f:
                f.write(desc)

    return render_template('create.html',myid=myid)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)