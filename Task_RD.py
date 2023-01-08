# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:04:44 2023

@author: Patryk
"""
import cv2
import threading
import queue

global test_capture
global test_sample

# %%cell 1
#### Comment 1 Create a queue for sending frames from ThreadA to ThreadB
frame_queue = queue.Queue()
processed_queue = queue.Queue()

class ThreadA(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        
        global test_capture
        test_capture = capture
        
#### Comment 2 Load the video
        capture = cv2.VideoCapture("source.avi")
        while capture.isOpened():
#### Comment 3 Read each frame
            ret, frame = capture.read()
            if ret is None:
                break
            
#### Comment 4 Send the frame to ThreadB by queue
            frame_queue.put(frame)
            
#### Comment 5 Release the video capture and signal the end of the video in queue
        capture.release()
        print("Video thread done")
        frame_queue.put(None)

# %%cell 2
class ThreadB(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        
        global test_sample
        test_sample = sample
        
#### Comment 6 Load the sample image
        sample = cv2.imread("sample.png")
        frame_number = 0
        while True:
            
#### Comment 7 Get a frame from the queue
            frame = frame_queue.get()
            if frame is None:
                break
            
#### Comment 8 Use cv2.matchTemplate() to find the position of the sample image in the frame
            result = cv2.matchTemplate(frame, sample, cv2.TM_CCOEFF_NORMED)
            _, _, _, position = cv2.minMaxLoc(result)
            
#### Comment 9 Get the top-left and bottom-right coorddinates of the rectangle
            x, y = position
            h, w = sample.shape[:-1]
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            
#### Comment 10 Draw a rectangle at the position of the sample image
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 5)
            
#### Comment 11 Send the processed frame to main()
            processed_queue.put((frame, top_left, frame_number))
            
            frame_number += 1
            
        print("Proccesing threa done")
        frame = None
        top_left = None
        frame_number = None
        processed_queue.put((frame, top_left, frame_number))
            
            
# %%cell 3

def main():
#### Comment 12 Create and start the threads
    thread_a = ThreadA()
    thread_b = ThreadB()
    thread_a.start()
    thread_b.start()
    
    while True:
#### Comment 13 Get a frame from the queue
        frame, position, frame_number = processed_queue.get()
        if frame is None:
            break
        
#### Comment 14 Save
        x, y = position
        print(f"{frame_number}: {x} {y}")
        filename = f"processed/frame{frame_number}_{x}_{y}.png"
        cv2.imwrite(filename, frame)
    print("Main thread done")

if __name__ == "__main__":
    main()
