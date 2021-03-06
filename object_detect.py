import numpy as np
import cv2
import matplotlib.pyplot as plt
import write_to_mathematica

def main(record=False):
    face_c = cv2.CascadeClassifier(
        "classifier/haarcascade_frontalface_default.xml")
    profile_c = cv2.CascadeClassifier("classifier/haarcascade_profileface.xml")
    # smile_c = cv2.CascadeClassifier("classifier/haarcascade_smile.xml")
    # full_body_c = cv2.CascadeClassifier("classifier/haarcascade_fullbody.xml")

    vid = cv2.VideoCapture("viclong.mov")
    if record:
        fourcc = cv2.VideoWriter_fourcc(*'mov')
        out = cv2.VideoWriter('output.mov', fourcc, 20.0, (640, 480))

    if not vid.isOpened():
        print("not opened")
        input()
    samples = 1000
    im_data = np.empty(samples)

    for l in range(samples):
        try:
            ret, img = vid.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_c.detectMultiScale(gray, 1.3, 5)
            profiles = profile_c.detectMultiScale(gray, 1.3, 5)
            # bodies = full_body_c.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                #draw the rect around the face
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                cv2.rectangle(img, (x, y), (x + w//4, y + h//2), (255, 0, 0), 1)
                cv2.rectangle(img, (x, y), (x + 3*w//4, y + 3*h//4), (255, 0, 0), 1)
                cv2.rectangle(img, (x, y), (x + 3*w//4, y + h//2), (255, 0, 0), 1)
                cv2.rectangle(img, (x, y), (x + w//4, y + 3*h//4), (255, 0, 0), 1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, 'Face', (x + w // 2, y), font,
                            0.5, (255, 255, 255), 1, cv2.LINE_AA)

                sum=0
                count=0
                for i in range(x+h//4,x+3*h//4,10):
                    for j in range(y+h//2,y+3*h//4,10):
                        sum += img[i,j][0]
                        count+=1

                        #[img[x+w//4,y+h//2+k*h//80][0] for i in range(1,20) for k in range(1,20)]
                
                im_data[l] = sum/(count)
            #sum([img[x+w//4,y+h//2][0],img[x+3*w//4,y+3*h//4][0],img[x+w//4,y+3*h//4][0],img[x+3*w//4,y+h//2][0]])

            # roi_gray = gray[y:y + h, x:x + w]  # get the face
            # roi_color = img[y:y + h, x:x + w]  # get the face

            # smiles = smile_c.detectMultiScale(
            #     roi_gray)  # look for smile on face

            #count = 0

            # for (sx, sy, sw, sh) in smiles:
            #     # draw the smile box
            #     if count >= 1:
            #         break
            #     cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh),
            #                   (0, 0, 255), 1)
            #     count += 1

        # for (x, y, w, h) in profiles:
        #     # draw the rect around the profile of the face
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     cv2.putText(img, 'Face', (x + w // 2, y), font,
        #                 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        # for (x, y, w, h) in bodies:
        #     # draw the rect around the body
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 1)

            if record:
                out.write(img)
            cv2.imshow('vid', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break

    vid.release()
    if record:
        out.release()
    cv2.destroyAllWindows()
    write_to_mathematica.write(im_data)
if __name__ == "__main__":
    main()
