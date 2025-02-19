import cv2
import numpy as np

def cartoonize_image(input_image_path, save_path):
    img = cv2.imread(input_image_path)
    if img is None:
        raise ValueError("Could not read the image")

    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, labels, centers = cv2.kmeans(data, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    quantized = np.uint8(centers)[labels.flatten()].reshape(img.shape)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(cv2.medianBlur(gray, 7), 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    
    cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
    cv2.imwrite(save_path, cartoon)
    return cartoon

if __name__ == "__main__":
    try:
        cartoonize_image("onset.PNG", "cartoon_output.jpg")
        print("Image cartoonized successfully!")
    except Exception as e:
        print(f"Error: {e}")
