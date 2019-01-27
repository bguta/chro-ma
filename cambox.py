import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    face_c = cv2.CascadeClassifier(
        "classifier/haarcascade_frontalface_default.xml")
    vid = cv2.VideoCapture("output.avi")

    x, y, w, h = 200, 100, 128, 128

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')

    samples = 750
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
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    for i in range(samples):
        ret, img = vid.read()
        blur = cv2.GaussianBlur(img, (301, 301), 0, 0)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # faces = face_c.detectMultiScale(gray, 1.3, 5)
        # for (x, y, w, h) in faces:
        face_r, face_g, face_b = blur[y:(y + h), x:(x + w), 0], blur[y:(y + h), x:(x + w), 1], blur[y:(y + h), x:(x + w), 2]
        avg_r[i], avg_g[i], avg_b[i] = np.sum(face_r) / (w * h), np.sum(face_g) / (w * h), np.sum(face_b) / (w * h)
        cv2.rectangle(blur, (x, y), (x + w, y + h), (255, 0, 0), 1)

        cv2.imshow('vid', img)
        # out.write(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
    plt.plot(np.arange(len(avg_r)), avg_r, color="r")
    plt.plot(np.arange(len(avg_g)), avg_g, color="g")
    plt.plot(np.arange(len(avg_b)), avg_b, color="b")
    plt.show()
    fftr = np.abs(np.fft.rfft(avg_r))
    fftg = np.abs(np.fft.rfft(avg_g))
    fftb = np.abs(np.fft.rfft(avg_b))

    plt.plot(np.arange(4, len(fftr)) * 30 * 60 / len(fftr), fftr[4:])
    plt.plot(np.arange(4, len(fftg)) * 30 * 60 / len(fftg), fftg[4:])
    plt.plot(np.arange(4, len(fftb)) * 30 * 60 / len(fftb), fftb[4:])
    plt.show()

if __name__ == "__main__":
    main()
