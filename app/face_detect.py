# https://github.com/shantnu/FaceDetect/

import cv2
import tempfile

class FaceDetect:
    def __init__(self, image_path, classifier=None):
        self.image_path = image_path

        casc_path = "classifiers/%s" % (classifier or 'haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(casc_path)

        self.image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    def face_count(self):
        return dict(face_count=len(self.faces))

    def face_squares(self):
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        temp = tempfile.NamedTemporaryFile(suffix='.jpg')
        cv2.imwrite(temp.name, self.image)
        return temp
