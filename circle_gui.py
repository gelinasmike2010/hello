import tkinter as tk
import math

WIDTH, HEIGHT = 600, 600
CX, CY = WIDTH // 2, HEIGHT // 2
RADIUS = 200
NUM_LAT = 12
NUM_LON = 24
POINTS_PER_LINE = 60
ROTATION_SPEED = 0.02
FRAME_MS = 33


def generate_sphere_lines():
    latitudes = []
    for i in range(1, NUM_LAT):
        phi = math.pi * i / NUM_LAT
        ring = []
        for j in range(POINTS_PER_LINE):
            theta = 2 * math.pi * j / POINTS_PER_LINE
            x = RADIUS * math.sin(phi) * math.cos(theta)
            y = RADIUS * math.cos(phi)
            z = RADIUS * math.sin(phi) * math.sin(theta)
            ring.append((x, y, z))
        latitudes.append(ring)

    longitudes = []
    for i in range(NUM_LON):
        theta = 2 * math.pi * i / NUM_LON
        arc = []
        for j in range(POINTS_PER_LINE):
            phi = math.pi * j / (POINTS_PER_LINE - 1)
            x = RADIUS * math.sin(phi) * math.cos(theta)
            y = RADIUS * math.cos(phi)
            z = RADIUS * math.sin(phi) * math.sin(theta)
            arc.append((x, y, z))
        longitudes.append(arc)

    return latitudes + longitudes


def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return (x * cos_a + z * sin_a, y, -x * sin_a + z * cos_a)


def project(point):
    x, y, z = point
    focal = 800
    scale = focal / (focal + z)
    return (CX + x * scale, CY - y * scale)


def main():
    root = tk.Tk()
    root.title("Spinning Globe")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    lines = generate_sphere_lines()
    angle = 0.0

    def draw():
        nonlocal angle
        canvas.delete("all")

        for line in lines:
            rotated = [rotate_y(p, angle) for p in line]

            for i in range(len(rotated) - 1):
                p1 = rotated[i]
                p2 = rotated[i + 1]

                if p1[2] > 0 and p2[2] > 0:
                    color = "#4488ff"
                elif p1[2] > 0 or p2[2] > 0:
                    color = "#223366"
                else:
                    continue

                sx1, sy1 = project(p1)
                sx2, sy2 = project(p2)
                canvas.create_line(sx1, sy1, sx2, sy2, fill=color, width=1)

        angle += ROTATION_SPEED
        canvas.after(FRAME_MS, draw)

    draw()
    root.mainloop()


if __name__ == "__main__":
    main()
