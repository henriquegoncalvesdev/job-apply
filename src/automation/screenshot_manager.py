import pyautogui
from PIL import Image
import numpy as np
import io

class ScreenshotManager:
    @staticmethod
    def take_screenshot(region=None):
        screenshot = pyautogui.screenshot(region=region)
        return screenshot

    @staticmethod
    def screenshot_to_np(screenshot):
        return np.array(screenshot)

    @staticmethod
    def save_screenshot(screenshot, path):
        screenshot.save(path)
