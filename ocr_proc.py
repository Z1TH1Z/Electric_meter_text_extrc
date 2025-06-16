import cv2
import easyocr
import matplotlib.pyplot as plt


image_path = "11.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['en'])

results = reader.readtext(image)

for (bbox, text, prob) in results:
    print(f"Detected: {text} (Confidence: {prob:.2f})")
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image_rgb, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.axis("off")
plt.title("OCR Result")
plt.show()
