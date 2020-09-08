from flask import Flask
from flask import render_template
from flask import request
import os

app=Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template('index.html')
@app.route('/files')
def files_folder():
    files=os.listdir("static/music") # obtenemos los archivos del directorio music
    for elements in files:
        if "mp3" not in elements:
            file.remove(elements)
    return render_template('files.html',values=files)

if __name__ == '__main__':
    app.run( debug=True, host= '0.0.0.0' )
