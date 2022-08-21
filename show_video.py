# import the opencv library
import cv2
from datetime import datetime

# define a video capture object
vid = cv2.VideoCapture(0)
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
font = cv2.FONT_HERSHEY_SIMPLEX

def add_text(frame, text, position):
    """
    colour white = (255,255,255)
    colour black = (0,0,0)
    """
    cv2.putText(frame, text, position, font, 1, (0,255,0), 2, cv2.LINE_AA)

while(True):
    # Capture the video frame
    ret, frame = vid.read()
    datetime_now = datetime.now()
    # Display Date
    add_text(frame, datetime_now.strftime("%Y.%m.%d %H:%M:%S.%f")[:-4], (10, 30))
    # Display the resulting frame
    cv2.imshow('window', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
