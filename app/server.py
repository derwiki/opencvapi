from io import BytesIO
import os
import sys

import flask

from face_detect import FaceDetect

app = flask.Flask(__name__)
#TODO create directory if doesn't exist or use tempdir
app.config['UPLOAD_FOLDER'] = '/tmp/opencvapi/upload/'

@app.route('/face/count', methods=['POST'])
def face_post():
    image = flask.request.files['image']
    return flask.jsonify(FaceDetect(image.filename).face_count())

@app.route('/face/squares', methods=['GET'])
def face_squares_get():
    return flask.render_template('face_squares.html')

@app.route('/face/squares', methods=['POST'])
def face_squares_post():
    file = flask.request.files['image']
    in_image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.name)
    file.save(in_image_path)
    out_image_path = FaceDetect(in_image_path).face_squares()

    return flask.send_file(
        out_image_path,
        mimetype="image/jpg",
        attachment_filename=file.name
    )

if __name__ == '__main__':
    app.run()
