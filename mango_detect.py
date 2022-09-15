import torch

# 載入自行訓練的 YOLOv5 模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp8/weights/best.pt')

# 影像來源
img = 'mango_test2.jpg'

# 設定 IoU 門檻值
model.iou = 0.5

# 設定信心門檻值
model.conf = 0.8

# 進行物件偵測
results = model(img)

results.show()
# 顯示結果摘要
results.print()
