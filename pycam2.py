#!/usr/bin/env python
# coding=utf-8

import sys
import time
import datetime

import cv


def frame2gray(frame):
    gray_im = cv.CreateImage(cv.GetSize(frame), 8, 1)
    cv.CvtColor(frame, gray_im, cv.CV_BGR2GRAY)
    return gray_im


def get_gray_frame(capture):
    return frame2gray(cv.QueryFrame(capture))


def get_frame_hist(frame):
    hist = cv.CreateHist([256], cv.CV_HIST_ARRAY, [[0, 255]], 1)
    cv.CalcHist([frame], hist)
    return hist


def get_file_name():
    now = datetime.datetime.now()
    return 'image-%s.jpg' % now.isoformat()


def main():
    time_span = 3600 * 10
    interval = 1
    start_time = time.time()
    capture = cv.CaptureFromCAM(0)
    for i in xrange(sys.maxint):
        frame = get_gray_frame(capture)
        hist = get_frame_hist(frame)
        change = False
        if i > 0:
            method = cv.CV_COMP_CORREL
            dist = cv.CompareHist(hist, last_hist, method)
            change = dist <= 0.99
            if change:
                cv.SaveImage(get_file_name(), frame)
        last_hist = hist
        if change:
            interval = 0.75
        else:
            interval = 1
        time.sleep(interval)
        if time.time() - start_time > time_span:
            break


if __name__ == '__main__':
    main()
