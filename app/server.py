import httplib
from io import BytesIO
import os
import sys

import flask

from face_detect import FaceDetect

app = flask.Flask(__name__)
#TODO create directory if doesn't exist or use tempdir
app.config['UPLOAD_FOLDER'] = '/tmp/opencvapi/upload/'

def classifiers():
    return os.listdir('classifiers/')

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
    file.save(in_image_path)
    out_image_path = FaceDetect(
      in_image_path,
      classifier=classifier
    ).face_squares()

    return flask.send_file(
        out_image_path,
        mimetype="image/jpg",
        attachment_filename=file.name
    )

@app.route('/face/count', methods=['POST'])
def face_count():
    image = flask.request.files['image']
    return flask.jsonify(FaceDetect(image.filename).face_count())

@app.route('/favicon.ico')
def favicon():
   return ('', httplib.NO_CONTENT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
