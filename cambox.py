import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    face_c = cv2.CascadeClassifier(
        "classifier/haarcascade_frontalface_default.xml")
    vid = cv2.VideoCapture(0)

    x, y, w, h = 600, 100, 100, 100

    samples = 200
    avg = np.zeros(samples)

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
    for i in range(samples):
        ret, img = vid.read()
        face = img[y:(y + h), x:(x + w)]
        avg[i] = np.sum(face) / (3* w * h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.imshow('vid', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
    plt.plot(np.arange(samples), avg)
    plt.show()
    fft = np.abs(np.fft.rfft(avg))

    plt.plot(fft)
    plt.show()

if __name__ == "__main__":
    main()
