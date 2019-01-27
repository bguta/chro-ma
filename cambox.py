import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    vid = cv2.VideoCapture('face.avi')

    x, y, w, h = 200, 100, 16, 16

    samples = 50
    avg_r = np.zeros(samples)
    avg_g = np.zeros(samples)
    avg_b = np.zeros(samples)

    # ready = False

    # print("Waiting ...")
    # print("Enter q to start")
    # while not ready:
    #     ret, img = vid.read()
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    #     cv2.imshow('vid', img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    print("Starting ... ")
    if not vid.isOpened():
        print("not opened")
        input()
    for i in range(samples):
        ret, img = vid.read()
        blur = cv2.GaussianBlur(img, (7, 7), 0, 0)

        face_r, face_g, face_b = blur[y:(y + h), x:(x + w), 0], blur[y:(y + h), x:(x + w), 1], blur[y:(y + h), x:(x + w), 2]
        avg_r[i], avg_g[i], avg_b[i] = np.sum(face_r) / (w * h), np.sum(face_g) / (w * h), np.sum(face_b) / (w * h)
        cv2.rectangle(blur, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.imshow('vid', blur)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("... Done")

    vid.release()
    cv2.destroyAllWindows()
    plt.plot(np.arange(len(avg_r)), avg_r, color="r")
    plt.plot(np.arange(len(avg_g)), avg_g, color="g")
    plt.plot(np.arange(len(avg_b)), avg_b, color="b")
    plt.show()
    fftr = np.abs(np.fft.rfft(avg_r))
    fftg = np.abs(np.fft.rfft(avg_g))
    fftb = np.abs(np.fft.rfft(avg_b))

    plt.plot(np.arange(4, len(fftr)) * 30 * 60 / (2 * len(fftr)), fftr[4:] + fftg[4:] + fftb[4:])

    plt.show()

if __name__ == "__main__":
    main()
