import pytest
import pygame
from goodbyeVisuals.shapes import Polygon

def test_polygon_creation():
    polygon = Polygon(100, 100, 50, 6, (255, 255, 255))
    assert polygon.x == 100
    assert polygon.y == 100
    assert polygon.radius == 50
    assert polygon.sides == 6
    assert polygon.color == (255, 255, 255)
