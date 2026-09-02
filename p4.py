import cv2

# Read RGB image
image = cv2.imread("C:/Users/Student/cv1/color.png")

# Check if image is loaded
if image is None:
    print("Image not found!")
    exit()

# Convert RGB image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set threshold value
threshold_value = 200

# Apply binary threshold
_, threshold_image = cv2.threshold(
    gray, threshold_value, 255, cv2.THRESH_BINARY
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Threshold Image", threshold_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
