from PIL import Image
import numpy as np
import random

# Open the image file
input_image = Image.open("img1.png")
pixels = input_image.load()

# Print the color of a specific pixel (for demonstration purposes)
print(pixels[9, 8])

# Function to find the starting and ending points in the image
def find_start_and_end_points(image):
    image_array = np.array(image)
    # Define the colors for start and end points
    start_color = (254, 0, 0)
    end_color = (0, 9, 254)
    
    # Find the coordinates of the start and end points
    start_coordinates, _ = np.where(np.all(image_array == start_color, axis=2))
    end_coordinates, _ = np.where(np.all(image_array == end_color, axis=2))
    
    start_point = (start_coordinates[0], start_coordinates[0])
    end_point = (end_coordinates[0], end_coordinates[0])
    
    return start_point, end_point

# Function to display an image
def display_image(image):
    resized_image = image.resize((600, 600))
    resized_image.show()

# Function to search for a path from start to end point in the image
def find_path(start_point, end_point, image, pixels):
    is_path_found = False
    current_position = start_point
    image_array = np.array(image)
    path = []
    intersections = []
    
    while not is_path_found:
        possible_moves = []
        surrounding_positions = [
            (current_position[0] - 1, current_position[1]),
            (current_position[0] + 1, current_position[1]),
            (current_position[0], current_position[1] - 1),
            (current_position[0], current_position[1] + 1)
        ]

        for move in surrounding_positions:
            if end_point == move:
                is_path_found = True
            if (
                (pixels[move] >= (200, 200, 200) or pixels[move] == (0, 9, 254))
                and pixels[move] != (255, 255, 0)
                and move != start_point
            ):
                possible_moves.append(move)

        if len(possible_moves) >= 2:
            if current_position not in intersections:
                intersections.append(current_position)

        if len(possible_moves) == 0:
            reversed_intersections = intersections[::-1]
            for i in reversed_intersections:
                if i != current_position:
                    current_position = i
                    intersections.pop(intersections.index(i))
                    break
            path = path[:path.index(current_position)]
        else:
            current_position = random.choice(possible_moves)
        
        path.append(current_position)
        image_array[current_position[1], current_position[0]] = (255, 255, 0)
        image = Image.fromarray(image_array)
        pixels = image.load()

    for p in path:
        image_array[p[1], p[0]] = (0, 255, 0)
    image = Image.fromarray(image_array)
    image.save('output_image.png')

# Find the start and end points in the input image
start_point, end_point = find_start_and_end_points(input_image)

# Search for a path from start to end point and save the output image
find_path(start_point, end_point, input_image, pixels)
