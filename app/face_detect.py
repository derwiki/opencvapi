# https://github.com/shantnu/FaceDetect/

import cv2

class FaceDetect:
    def __init__(self, image_path):
        self.image_path = image_path

    def perform(self):
        casc_path = "classifiers/haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(casc_path)

        image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        file_path = "public/%s" % self.image_path
        print "Writing to: %s" % file_path
        cv2.imwrite(file_path, image)
        return dict(face_count=len(faces))
