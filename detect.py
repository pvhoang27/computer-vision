import torch

# 🔍 Model
# Các lựa chọn model: 'yolov5n', 'yolov5s', 'yolov5m', 'yolov5l', 'yolov5x', hoặc 'custom' (nếu bạn có model riêng)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 🖼️ Ảnh đầu vào
img = "https://ultralytics.com/images/zidane.jpg"  # hoặc đường dẫn local, hoặc ảnh đọc bằng OpenCV, PIL, numpy, list

# 🚀 Inference
results = model(img)

# 📊 Kết quả
results.print()          # In ra thông tin phát hiện
results.show()           # Hiển thị ảnh có bounding boxes
results.save()           # Lưu ảnh kết quả vào thư mục runs/detect/exp
