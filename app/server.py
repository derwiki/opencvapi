import httplib
from io import BytesIO
import os
import sys

import flask

from classifier import FaceClassifier

app = flask.Flask(__name__)
#TODO create directory if doesn't exist or use tempdir
app.config['UPLOAD_FOLDER'] = '/tmp/opencvapi/upload/'
app.config['MAX_CONTENT_LENGTH'] = 512 * 1024

def stream_size(stream):
    stream.seek(0, os.SEEK_END)
    file_length = stream.tell()
    stream.seek(0, os.SEEK_SET)
    return file_length

def file_size(file_path):
    return os.stat(file_path).st_size

def classifiers():
    return os.listdir('classifiers/')

def error(message):
  return [message, 413]

@app.route('/', methods=['GET'])
def index():
    return flask.render_template(
        'index.html',
        classifiers=classifiers()
    )

@app.route('/classifier', methods=['POST'])
def classifier():
    file = flask.request.files['image']
    classifier = flask.request.form['classifier']
    in_image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.name)

    image_size = stream_size(file)
    print "stream size: {}".format(image_size)
    if image_size > 512 * 1024:
        return error("Uploaded image too large: {}".format(image_size))

    file.save(in_image_path)
    print "file size: {}".format(file_size(in_image_path))
    out_image_path = FaceClassifier(in_image_path).face_squares()

    return flask.send_file(
        out_image_path,
        mimetype="image/jpg",
        attachment_filename=file.name
    )

@app.route('/face/count', methods=['POST'])
def face_count():
    image = flask.request.files['image']
    return flask.jsonify(FaceClassifier(image.filename).face_count())

@app.route('/favicon.ico')
def favicon():
   return ('', httplib.NO_CONTENT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
