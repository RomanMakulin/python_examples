import cv2

fase_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('lections/lec2/face.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = fase_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)


# cv2.imshow('result', img)
# cv2.waitKey(0)

cap = cv2.VideoCapture('lections/lec2/test_video.mp4')

while True:
    sucsess, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fase_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break