from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

posts = []
replies = {}

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    docs_directory = "Docs"
    file_list = os.listdir(docs_directory)
    return render_template('index.html', file_list=file_list)

@app.route('/download/<filename>')
def download_file(filename):
    docs_directory = "Docs"
    return send_from_directory(docs_directory, filename, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    docs_directory = "Docs"
    
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    file.save(os.path.join(docs_directory, file.filename))
    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50)