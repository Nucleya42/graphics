from PIL import Image
import matplotlib.pyplot as plt

# Function to pixelate an image
def pixelate_image(image_path, pixel_size):
    # Open the image
    img = Image.open(image_path)

    # Get the original size
    original_size = img.size

    # Resize image to a smaller size (pixelation step)
    img_small = img.resize(
        (original_size[0] // pixel_size, original_size[1] // pixel_size),
        resample=Image.NEAREST
    )

    # Scale back to original size (creating large blocky pixels)
    img_pixelated = img_small.resize(original_size, Image.NEAREST)

    return img_pixelated

# Path to your image (fix the file path here)
image_path = r'C:/Users/SUBHA/OneDrive/Pictures/Saved Pictures/5.jpg'  # Replace with your actual image file path

# Pixel size (the higher the number, the more pixelated the image will be)
pixel_size = 10

# Create pixelated image
pixelated_image = pixelate_image(image_path, pixel_size)

# Display the pixelated image
plt.imshow(pixelated_image)
plt.axis('off')  # Hide axes for better viewing
plt.show()
