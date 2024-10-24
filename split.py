from PIL import Image, ImageDraw

# Function to split the image and combine into one frame with a grid
def split_image_in_frame(image_path, rows, cols, grid_color=(0, 0, 0), grid_thickness=2):
    # Open the image
    img = Image.open(image_path)
    
    # Get the dimensions of the original image
    width, height = img.size
    
    # Calculate the size of each tile (sub-image)
    tile_width = width // cols
    tile_height = height // rows
    
    # Create a new blank image with a white background and space for the grid lines
    new_image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(new_image)
    
    # Loop through the image and paste sub-images into the new image
    for row in range(rows):
        for col in range(cols):
            # Define the box for the sub-image (left, upper, right, lower)
            left = col * tile_width
            upper = row * tile_height
            right = (col + 1) * tile_width
            lower = (row + 1) * tile_height
            
            # Crop the image to the box
            sub_image = img.crop((left, upper, right, lower))
            
            # Paste the sub-image into the new canvas
            new_image.paste(sub_image, (left, upper))
            
            # Draw the grid line between tiles
            draw.line([(left, upper), (left, lower)], fill=grid_color, width=grid_thickness)  # Vertical line
            draw.line([(left, upper), (right, upper)], fill=grid_color, width=grid_thickness)  # Horizontal line
    
    # Draw the right and bottom border of the grid
    draw.line([(width - 1, 0), (width - 1, height)], fill=grid_color, width=grid_thickness)  # Right border
    draw.line([(0, height - 1), (width, height - 1)], fill=grid_color, width=grid_thickness)  # Bottom border

    return new_image

# Path to your image (replace with your image path)
image_path = r'C:/Users/SUBHA/OneDrive/Pictures/Saved Pictures/5.jpg'  # Update with your image path

# Number of rows and columns to split the image into
rows = 10
cols = 10

# Split the image and combine it in a frame
combined_image = split_image_in_frame(image_path, rows, cols, grid_color=(0, 0, 0), grid_thickness=10)

# Save or display the combined image with grid
combined_image.save('split_image_with_grid.jpg')  # Save the combined image
combined_image.show()  # Display the combined image
