import os
import sys
from PyQt6.QtGui import QFontDatabase, QFont

def resource_path(relative_path):
    """Đường dẫn tuyệt đối, đúng khi build exe với PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def GetFont():
    font_path = resource_path("font/icomoon.ttf")
    if not os.path.exists(font_path):
        print("Font file not found:", font_path)
        return QFont("Arial", 17)

    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print("Failed to load font:", font_path)
        return QFont("Arial", 17)

    families = QFontDatabase.applicationFontFamilies(font_id)
    if not families:
        print("No font families found in:", font_path)
        return QFont("Arial", 17)

    font = QFont(families[0], 17)
    print("Loaded font family:", families[0])
    return font
