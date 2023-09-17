# Python-maze-solver-using-DFS
```
# Depth First Search (DFS) Path Finding in an Image

This Python script demonstrates the use of Depth First Search (DFS) algorithm to find a path from a starting point to an ending point in an image. The output image visually represents how the algorithm has worked, with the path highlighted in green.

## Dependencies

This code requires the following Python libraries to be installed:
- PIL (Python Imaging Library) for image manipulation
- NumPy for numerical operations

You can install these dependencies using pip:

```bash
pip install pillow numpy
```

## Usage

1. Make sure you have an image file named `img1.png` in the same directory as the script. This image should contain a start point (red) and an end point (blue).

2. Run the script using Python:

```bash
python dfs_image_path_finder.py
```

3. The script will find a path from the start point to the end point in the image using Depth First Search. The path will be highlighted in green, and the resulting image will be saved as `output_image.png` in the same directory.

4. You can view the output image to see how the algorithm has worked to find the path in the original image.

## How It Works

- The script reads the input image and identifies the start and end points based on their specified colors.
- It then performs a Depth First Search to find a path from the start to the end point while avoiding obstacles and keeping track of intersections.
- The path is highlighted in green in the output image to visualize the result.

## Example

Here is an example of how the output image might look:

![dfs](https://github.com/yumbiakyumu/Python-maze-solver-using-DFS/assets/100669436/618eb405-d101-44bc-ae28-f889a2287529)



The green line in the output image represents the path found by the Depth First Search algorithm from the start point (red) to the end point (blue) in the input image.

Feel free to use and modify this code for your own projects involving path finding in images.
```

This README file provides an overview of the code, its usage, and how it works, along with an example of the output image.
