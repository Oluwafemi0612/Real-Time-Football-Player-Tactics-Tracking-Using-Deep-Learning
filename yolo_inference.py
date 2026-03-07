from ultralytics import YOLO
model = YOLO('yolo26x')

results = model.predict('input_video/E3c993bd2_0 (74).mp4', save=True)
print(results[0])
print('-----------------------------')
for box in results[0].boxes:
    print(box)  # Bounding box coordinates