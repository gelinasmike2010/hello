import tkinter as tk
import math


def main():
    root = tk.Tk()
    root.title("Circle Drawing")

    width, height = 600, 600
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    # Circle parameters
    cx, cy = width // 2, height // 2  # center
    radius = 200
    num_points = 360

    # Calculate x, y coordinates around the circle
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))

    # Draw the circle by connecting consecutive points with lines
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    root.mainloop()


if __name__ == "__main__":
    main()
