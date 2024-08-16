
from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('../Yolo_weights/yolov8n.pt')  # load a pretrained model (recommended for training)

    results = model.train(data='../DataSet/License_Plate_object-3/data.yaml', epochs=100, imgsz=640)