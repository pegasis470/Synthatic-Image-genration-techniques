#     pip install pillow

import numpy as np
from PIL import Image, ImageDraw

def generate_synthetic_image(original_image_path, output_image_path):
    # Load the original image
    original_image = Image.open(original_image_path)

    # Create a copy of the original image
    synthetic_image = original_image.copy()

    # Get image size
    width, height = synthetic_image.size

    # Create a pattern with random colors
    pattern_image = create_random_pattern(width, height)

    # Set blending ratio (0.0 to 1.0)
    alpha = 0.2

    # Blend the original image and the pattern image
    synthetic_image = Image.blend(synthetic_image, pattern_image, alpha)

    # Save the synthetic image
    synthetic_image.save(output_image_path)

def create_random_pattern(width, height):
    # Create a blank image
    pattern_image = Image.new("RGB", (width, height))

    # Create a draw object to draw on the image
    draw = ImageDraw.Draw(pattern_image)

    # Draw random rectangles with random colors
    for _ in range(50):
        color = (np.random.randint(256), np.random.randint(256), np.random.randint(256))
        x0, y0 = np.random.randint(width), np.random.randint(height)
        x1, y1 = np.random.randint(width), np.random.randint(height)
        draw.rectangle([x0, y0, x1, y1], fill=color)

    return pattern_image



if __name__ == "__main__":
    # Replace 'path/to/original/image.jpg' with the path to your original image
    original_image_path = "cat.jpg"

    # Replace 'path/to/output/image.jpg' with the desired output path for the synthetic image
    output_image_path = "synthetic1.jpg"

    generate_synthetic_image(original_image_path, output_image_path)
