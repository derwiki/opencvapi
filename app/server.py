import sys
from io import BytesIO

import flask

from face_detect import FaceDetect

app = flask.Flask(__name__)

@app.route('/face/count', methods=['PUT'])
def face():
    image = flask.request.files['image']
    return flask.jsonify(FaceDetect(image.filename).face_count())

@app.route('/face/squares', methods=['PUT'])
def face_squares():
    image = flask.request.files['image']
    _, out_image, _ = FaceDetect(image.filename).face_squares()
    return flask.send_file(BytesIO(out_image))

if __name__ == '__main__':
    app.run()
