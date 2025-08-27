from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QIcon

def Theme(light_icon: str, dark_icon: str) -> QIcon:
    palette = QApplication.palette()
    bg_color = palette.color(QPalette.ColorRole.Window)

    brightness = (bg_color.red() * 299 + bg_color.green() * 587 + bg_color.blue() * 114) / 1000

    if brightness < 128:
        return QIcon(light_icon)
    else:
        return QIcon(dark_icon)
