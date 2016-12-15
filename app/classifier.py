# https://github.com/shantnu/FaceDetect/

import cv2
import tempfile

class Classifier(object):
    def __init__(self, image_path, classifier_path):
        self.image_path = image_path

        casc_path = "classifiers/{}".format(classifier_path)
        cascade = cv2.CascadeClassifier(casc_path)
        print "loaded classifier: {}".format(classifier_path)

        self.image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.features = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    def feature_count(self):
        return dict(feature_count=len(self.features))

    def feature_squares(self):
        print "len(self.features): {}".format(len(self.features))
        for (x, y, w, h) in self.features:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        temp = tempfile.NamedTemporaryFile(suffix='.jpg')
        cv2.imwrite(temp.name, self.image)
        return temp

class FaceClassifier(Classifier):
    def __init__(self, image_path):
        super(FaceClassifier, self).__init__(image_path, 'haarcascade_frontalface_default.xml')
