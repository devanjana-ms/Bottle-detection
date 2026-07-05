from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train the model on CPU
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640, #640*640
    batch=16, #1-16,17-32         # safer for CPU/RAM
    device="cpu",   
    name="bottle_model"
)

print("Training completed!") 