import cv2
import matplotlib.pyplot as plt
image=cv2.imread("Cat.jpg")
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _=image_rgb.shape
print(width)
start1=(0, height//2)
end1=(100, height//2)
cv2.arrowedLine(image_rgb, start1, end1, (0,255,255), 3, tipLength=0.5)
start2=(width, height//2)
end2=(width-100, height//2)
cv2.arrowedLine(image_rgb, start2, end2, (0,255,255), 3, tipLength=0.5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, "250", (end1[0], end1[1]), font, 0.7, (255,0,255), 2)
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis(False)
plt.show()