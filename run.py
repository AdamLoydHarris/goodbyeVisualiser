from goodbyeVisuals import Visualizer
from goodbyeVisuals.shapes import Polygon


if __name__ == "__main__":
    from goodbyeVisuals import Visualizer
    from goodbyeVisuals.shapes import Polygon, Circle
    
    # Create visualizer
    vis = Visualizer(800, 600)
    
    # Add shapes
    # for i in range(5, 9):
    #     vis.add_shape(Polygon(400, 300, i*50, i, (0, 255, 255), 5-i))
    
    # vis.add_shape(Circle(400, 300, 50, (255, 255, 255), pulse_speed=3.0))
    for i in range(15):
        vis.add_shape(Circle(400, 300, i*15, (255, 255, 255), pulse_speed=10-i/2))
    
    # Run visualization
    vis.run()