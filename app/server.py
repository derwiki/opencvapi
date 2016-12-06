import sys

import flask

from face_detect import FaceDetect

app = flask.Flask(__name__)

@app.route('/face', methods=['PUT'])
def face():
    image = flask.request.files['image']
    return flask.jsonify(FaceDetect(image.filename).perform())

if __name__ == '__main__':
    app.run()
