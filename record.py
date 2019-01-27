import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def rec():
    filename = 'data/output.avi'
    vid = cv2.VideoCapture(0)
    face_c = cv2.CascadeClassifier(
        "classifier/haarcascade_frontalface_default.xml")

    # x, y, w, h = 312, 90, 16, 16
    samples = 800

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    ready = False

    recs = []

    print("Waiting ...")
    print("Enter q to start")
    while not ready:
        ret, img = vid.read()

        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_c.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.imshow('vid', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Starting ... ")
    out = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))
    for i in range(samples + 15):
        printProgressBar(i, samples + 14, prefix='Progress:', suffix='Complete', length=50)

        ret, img = vid.read()
        if (i > 15):
            out.write(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_c.detectMultiScale(gray, 1.3, 5)
        if(i > 15):
            recs.append(faces[0])

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.imshow('vid', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Done ... ")

    vid.release()
    cv2.destroyAllWindows()

    return recs


if __name__ == "__main__":
    rec()
