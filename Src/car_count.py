import cv2
from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
from Utils.sort import *

def count(src):
    cap = cv.VideoCapture(src)

    classNames = ['person',
                  'bicycle',
                  'car',
                  'motorcycle',
                  'airplane',
                  'bus',
                  'train',
                  'truck',
                  'boat',
                  'traffic light',
                  'fire hydrant',
                  'stop sign',
                  'parking meter',
                  'bench',
                  'bird',
                  'cat',
                  'dog',
                  'horse',
                  'sheep',
                  'cow',
                  'elephant',
                  'bear',
                  'zebra',
                  'giraffe',
                  'backpack',
                  'umbrella',
                  'handbag',
                  'tie',
                  'suitcase',
                  'frisbee',
                  'skis',
                  'snowboard',
                  'sports ball',
                  'kite',
                  'baseball bat',
                  'baseball glove',
                  'skateboard',
                  'surfboard',
                  'tennis racket',
                  'bottle',
                  'wine glass',
                  'cup',
                  'fork',
                  'knife',
                  'spoon',
                  'bowl',
                  'banana',
                  'apple',
                  'sandwich',
                  'orange',
                  'broccoli',
                  'carrot',
                  'hot dog',
                  'pizza',
                  'donut',
                  'cake',
                  'chair',
                  'couch',
                  'potted plant',
                  'bed',
                  'dining table',
                  'toilet',
                  'tv',
                  'laptop',
                  'mouse',
                  'remote',
                  'keyboard',
                  'cell phone',
                  'microwave',
                  'oven',
                  'toaster',
                  'sink',
                  'refrigerator',
                  'book',
                  'clock',
                  'vase',
                  'scissors',
                  'teddy bear',
                  'hair drier',
                  'toothbrush']

    # mask = cv.imread("../Images/mask.png")
    mask = cv.imread("../Images/mask2.png")

    model = YOLO('../Yolo_weights/yolov8n.pt')
    tracker = Sort(max_age=20, min_hits=2, iou_threshold=.3)
    # limits = [300, 337, 858, 324] # line 1
    limits = [50, 570, 650, 570]  # traffic_2_720.mp4") mask

    total_count = []
    id_list = []

    while True:
        success, img = cap.read()
        roi = cv.bitwise_and(img, mask)
        results = model(source=roi, stream=True)
        detections = np.empty((0, 5))
        cv.line(img, (limits[0], limits[1]), (limits[2], limits[3]), color=(0, 0, 255), thickness=2)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                w = x2 - x1
                h = y2 - y1

                conf = math.ceil((box.conf[0] * 100)) / 100
                # conf = math.ceil((box.conf[0]))

                cls = int(box.cls[0])
                currentClass = classNames[cls]

                if ((currentClass == 'car' or currentClass == 'bus' or currentClass == 'truck' or
                     currentClass == 'motorcycle') and conf > 0.3):
                    # cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                    #                    scale=0.6, thickness=1, offset=3)
                    currentArray = np.array([x1, y1, x2, y2, conf])
                    detections = np.vstack((detections, currentArray))

        resultsTracker = tracker.update(detections)

        for result in resultsTracker:
            x1, y1, x2, y2, id = result
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w = x2 - x1
            h = y2 - y1

            cvzone.cornerRect(img, (x1, y1, w, h), l=9, t=2, rt=2, colorR=(255, 0, 0))
            cvzone.putTextRect(img, f'{int(id)} {conf}', (max(0, x1), max(20, y1)), 1, 2, offset=3)

            cx, cy = x1 + w // 2, y1 + h // 2  # center of box
            cv.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[1] + 20:
                if total_count.count(id) == 0:
                    total_count.append(id)
                    # df = pd.DataFrame(data=[id])
                    id_list.append(id)
                    print(id_list)
                    cv.line(img, (limits[0], limits[1]), (limits[2], limits[3]), color=(0, 255, 0), thickness=2)

        cvzone.putTextRect(img, f'{len(total_count)}', (50, 50), )

        cv.imshow("Image", img)
        # cv.imshow("ROI", roi)
        cv.waitKey(1)


count()