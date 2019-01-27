import numpy as np
import cv2
import matplotlib.pyplot as plt
<<<<<<< HEAD
import callMatlab as mat
import glob

import os
import subprocess
=======
import operator
>>>>>>> 8acf1e5108144ef8def13b16fc0c3b2780f32e5b

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
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
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def npmax(l):
    return np.argmax(l)

def main():
    subprocess.call("reproduce_results.bat")
    f = glob.glob("Results/*.avi")[0]
    vid = cv2.VideoCapture(f)

    x, y, w, h = 200, 100, 16, 16

    samples = 100
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
        printProgressBar(i, samples, prefix = 'Progress:', suffix = 'Complete', length = 50)

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

    ri = npmax(fftr[4:])
    gi = npmax(fftg[4:])
    bi = npmax(fftb[4:])

    rrange = np.arange(4, len(fftr)) * 30 * 60 / len(fftr)
    grange = np.arange(4, len(fftg)) * 30 * 60 / len(fftg)
    brange = np.arange(4, len(fftb)) * 30 * 60 / len(fftb)

    print("\n\nRed max freq is {} bpm\n".format(rrange[ri]))
    print("Green max freq is {} bpm\n".format(rrange[gi]))
    print("Blue max freq is {} bpm\n".format(rrange[bi]))

    plt.plot(rrange, fftr[4:])
    plt.plot(grange, fftg[4:])
    plt.plot(brange, fftb[4:])
    plt.plot(np.arange(4, len(fftr)) * 30 * 60 / (2 * len(fftr)), fftr[4:] + fftg[4:] + fftb[4:])

    plt.show()

if __name__ == "__main__":
    main()
