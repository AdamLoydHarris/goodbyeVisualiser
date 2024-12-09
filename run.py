from goodbyeVisuals import Visualizer
from goodbyeVisuals.shapes import Polygon


if __name__ == "__main__":
    from goodbyeVisuals import Visualizer
    from goodbyeVisuals.shapes import Polygon, Circle
    
    # Create visualizer
    vis = Visualizer(800, 600)
    
    # Add shapes
    vis.add_shape(Polygon(400, 300, 100, 6, (0, 255, 255), 1.0))
    vis.add_shape(Circle(400, 300, 50, (255, 255, 255), pulse_speed=2.0))
    
    # Run visualization
    vis.run()