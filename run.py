from goodbyeVisuals import Visualizer
from goodbyeVisuals.shapes import Polygon

if __name__ == "__main__":
    vis = Visualizer()
    vis.add_shape(Polygon(400, 300, 100, 6, (0, 255, 255), 1.0))
    vis.run()

