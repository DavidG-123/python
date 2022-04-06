from email.mime import image
from turtle import width
import pytest
import os
import cv2
import numpy as n
from pytest import approx
from face_photobooth import main
from face_photobooth import loadIt


def test_main():
    file = cv2.imread("test/test.png")
    try:
        cv2.imshow("test/test.png", file)
        cv2.imwrite("test/complete.png", file)
    except FileNotFoundError:
        assert f"File could not save; path does not exist."
    os.remove("test/complete.png")
    assert f"Success, file is saved."

def test_preset():
    presets = ["BEACH", "BEACH 2", "BEACH 3", "CABANA", "DESERT", "OUTER SPACE", "VOLCANO"]
    try:
        loadIt(641,0)
    except:
        pass
    assert presets == ["BEACH", "BEACH 2", "BEACH 3", "CABANA", "DESERT", "OUTER SPACE", "VOLCANO"]
    try:
        x=0
        y=0
        loadIt(x, y)
    except IndexError:
        assert f"The x or y arguement is out of range."
        

pytest.main(["-v", "--tb=line", "-rN", __file__])
