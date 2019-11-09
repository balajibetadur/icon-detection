




# OpenCV program to detect google maps icon in real time
# Output the coordinates of icon

import cv2


cascade = cv2.CascadeClassifier('gmaps.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized.
while 1:
    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects icons of different sizes in the input image
    icons = cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in icons:
        # Rectangular border around the detected icon
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print('(%s' % str(x) + ', %s)' % y)

    # Display an image in a window
    cv2.imshow('img', img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()


