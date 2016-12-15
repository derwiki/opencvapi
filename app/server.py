import httplib
import os

import flask

from classifier import Classifier, FaceClassifier

app = flask.Flask(__name__)
#TODO create directory if doesn't exist or use tempdir
app.config['UPLOAD_FOLDER'] = '/tmp/opencvapi/upload/'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 4

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
    image_file = flask.request.files['image']
    classifier_file = flask.request.form['classifier']
    in_image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.name)

    image_size = stream_size(image_file)
    print "stream size: {}".format(image_size)
    if image_size > 1024 * 1024 * 4:
        return error("Uploaded image too large: {}".format(image_size))

    image_file.save(in_image_path)
    print "image_file size: {}".format(file_size(in_image_path))
    out_image_path = Classifier(in_image_path, classifier_file).feature_squares()

    return flask.send_file(
        out_image_path,
        mimetype="image/jpg",
        attachment_filename=image_file.name
    )

@app.route('/face/count', methods=['POST'])
def face_count():
    image = flask.request.files['image']
    return flask.jsonify(FaceClassifier(image.filename).feature_count())

@app.route('/favicon.ico')
def favicon():
    return ('', httplib.NO_CONTENT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
