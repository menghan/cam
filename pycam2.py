import cv


def main():
    cv.NamedWindow('w1', cv.CV_WINDOW_AUTOSIZE)
    camera_index = 0
    capture = cv.CaptureFromCAM(camera_index)
    while True:
        frame = cv.QueryFrame(capture)
        cv.ShowImage('w1', frame)
        cv.WaitKey(10)


if __name__ == '__main__':
    main()
