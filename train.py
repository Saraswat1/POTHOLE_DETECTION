from ultralytics import YOLO


model = YOLO("yolov8n.yaml")
# Train the model
results = model.train(data="config.yaml", epochs=100)