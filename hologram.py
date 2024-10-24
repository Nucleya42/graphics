import cv2
import numpy as np

# Load the input image
image = cv2.imread(r'C:/Users/SUBHA/OneDrive/Pictures/radha.jpg')


# Resize the image for better visibility
image = cv2.resize(image, (1400, 800))

# Create a hologram effect using a color gradient overlay
def apply_hologram_effect(img):
    # Create a blue-green gradient overlay
    rows, cols, _ = img.shape
    overlay = np.zeros((rows, cols, 3), dtype='uint8')
    
    for i in range(rows):
        color = 255 - (i * 255 // rows)  # Gradient effect
        overlay[i, :] = [color // 2, color, color // 4]  # Blue-green overlay

    # Blend the overlay with the original image
    hologram = cv2.addWeighted(img, 0.6, overlay, 0.4, 0)

    # Simulate scan lines by adding horizontal lines
    for i in range(0, rows, 10):
        hologram[i:i+1, :] = hologram[i:i+1, :] // 2

    return hologram

# Apply the hologram effect
hologram_image = apply_hologram_effect(image)

# Display the result
cv2.imshow('Hologram Effect', hologram_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output
cv2.imwrite('hologram_output.jpg', hologram_image)
