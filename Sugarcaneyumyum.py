from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.yaml')  # Use YOLOv8 nano, or replace with 'yolov8n.pt' for pretrained

# Train the model using your dataset
results = model.train(data='/Users/wangzhan/Documents/Python/WRO/sugarcaneyumyum.v1i.yolov11/dataset.yaml', epochs=10)


# Print out results
print(results)
