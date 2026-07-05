import cv2
import os

video_path = r"C:\Users\ADMIN\vs code\bottle2.mp4"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frames_to_extract = 120

step = total_frames // frames_to_extract #3600//120 step=30

count = 0
saved = 0

while cap.isOpened() and saved < frames_to_extract:
    ret, frame = cap.read()

    if not ret: #retrun value
        break

    if count % step == 0:
        cv2.imwrite(
            os.path.join(output_folder, f"frame_{saved:03d}.jpg"),
            frame
        )
        saved += 1

    count += 1

cap.release()

print(f"Extracted {saved} frames.")