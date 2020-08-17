import cv2
cars_cascade = cv2.CascadeClassifier("cars.xml")
def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,255,0), thickness=2)
    return frame
def Simulator():
    Carvideo = cv2.VideoCapture("videoplayback.mp4")
    while Carvideo.isOpened():
        ret, frame = Carvideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cars_frame = detect_cars(frame)
            cv2.imshow("frame", cars_frame)
        else:
            break
        if controlkey == ord("q"):
            break
    Carvideo.release()
    cv2.destroyAllWindows()
if __name__ ==  "__main__":
    Simulator()