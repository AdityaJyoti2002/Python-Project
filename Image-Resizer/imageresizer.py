import cv2

image = cv2.imread("/Users/adityajyoti/Documents/Python/project/Image-Resizer/new post.png", cv2.IMREAD_UNCHANGED )
cv2.imshow("title", image )

scale_parcent = 50

new_width = int(image.shape[1] * scale_parcent/100)
new_height = int(image.shape[0] * scale_parcent/100)

output = cv2.resize(image, (new_width, new_height))

cv2.imwrite('/Users/adityajyoti/Documents/Python/project/Image-Resizer/newimage.png', output)
cv2.waitKey(0)
