import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def rec():
    filename = 'data/output.avi'
    vid = cv2.VideoCapture(0)

    x, y, w, h = 200, 100, 16, 16
    samples = 250

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    ready = False

    print("Waiting ...")
    print("Enter q to start")
    while not ready:
        ret, img = vid.read()
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.imshow('vid', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Starting ... ")
    out = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))
    for i in range(samples + 15):
        ret, img = vid.read()
        if (i > 15):
            out.write(img)

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.imshow('vid', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Done ... ")

    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    rec()
