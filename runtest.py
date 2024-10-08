"""import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
model_path = '/Users/wangzhan/Documents/Python/WRO/sugarcaneyumyum.v1i.yolov11/runs/detect/train2/weights/best.pt'
model = YOLO(model_path)"""



# Open the webcam
"""cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform object detection
    results = model(frame)

    # Check the results of the detection
    print(results[0].boxes)  # This should print information about detected objects

    # Annotate and display the frame
    annotated_frame = results[0].plot()

    cv2.imshow('Webcam - YOLOv8 Object Detection', annotated_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("Exiting...")

        break

cap.release()
cv2.destroyAllWindows()"""


import cv2
from ultralytics import YOLO
from time import sleep

# Load the trained YOLOv8 model
model_path = '/Users/wangzhan/Documents/Python/WRO/sugarcaneyumyum.v1i.yolov11/runs/detect/train3/weights/best.pt'
model = YOLO(model_path)

# Path to your video file (replace 'your_video.mp4' with the actual path to your video)
img_path = '/Users/wangzhan/Documents/Python/WRO/sugarcaneyumyum.v1i.yolov11/train/images/messageImage_1728292929582.jpg'

# Open the video file
cap = cv2.VideoCapture(img_path)

# Check if the video file was opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame from the video
    ret, frame = cap.read()

    # If no frame is returned, break the loop (end of the video)
    if not ret:
        print("End of video or failed to grab frame.")
        break

    # Perform object detection on the current frame
    results = model(frame)

    # Print detection results (bounding boxes, scores, etc.)
    print(results[0].boxes)  # Prints information about detected objects

    # Annotate the frame with the results
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)
    cv2.waitKey(5000)

    # Press 'q' to exit the loop and stop the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
