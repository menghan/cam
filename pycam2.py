import cv

cv.NamedWindow('w1', cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)


def repeat():
    global capture  # declare as globals since we are assigning to them now
    global camera_index
    frame = cv.QueryFrame(capture)
    cv.ShowImage('w1', frame)
    c = cv.WaitKey(10)


def main():
    while True:
        repeat()


if __name__ == '__main__':
    main()
