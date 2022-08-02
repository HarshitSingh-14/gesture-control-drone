from sre_constants import SUCCESS
from tkinter.tix import Tree
import cv2
from cv2 import threshold
from djitellopy import tello
import cvzone
from flask import Config


threshold = 0.65
# for detecting duplicates
nmsThreshold =0.2
cap = cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,480)


NamesOfObjects= []
NameFile = 'coco.names'
ConfigFile = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
WeightFile = 'frozen_inference_graph.pb'
with open(NameFile,'rt') as f:
    NamesOfObjects = f.read().split('\n')
print(NamesOfObjects)


# Using pretrained model
# document coco
net = cv2.dnn_DetectionModel(WeightFile,ConfigFile)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)





while True:
    success ,img = cap.read()
    classIds, confidence , boundingBox= net.detect(img, confThreshold=threshold, nmsThreshold=nmsThreshold)
    try:
        for classId, conf, box in zip(classIds.flatten(), confidence.flatten(), boundingBox):
            cvzone.cornerRect(img, box)# draw rectangle
            cv2.putText(img, f'{NamesOfObjects[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
    except:
        pass
    cv2.imshow("img",img)
    cv2.waitKey(1)