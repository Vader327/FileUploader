from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import shutil
import socket

url_to_connect = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../../Extras/Outputs'

@app.route('/')
def index():
   return render_template('index.html')
	
@app.route('/', methods=['POST'])
def upload_file():
   if request.method == 'POST':
      files = request.files.getlist("file")
      for file in files:
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
         
      return redirect(url_for('index'))

@app.route('/download', methods=['GET'])
def download():
   shutil.make_archive('../../Extras/Zips/files', 'zip', 'C://Users/Saaheer/Desktop/Programming/Extras/Outputs')
   return send_file('C://Users/Saaheer/Desktop/Programming/Extras/Zips/files.zip', as_attachment=True)
		
if __name__ == '__main__':
   app.run(debug=True, host=url_to_connect)
