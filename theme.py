import ctypes
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication
import winreg


def is_windows_dark_mode() -> bool:
    """Check Windows app theme (light/dark)."""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        )
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return value == 0  # 0 = dark, 1 = light
    except Exception:
        return False


def apply_palette(app: QApplication, dark: bool):
    """Apply Qt palette (light or dark)."""
    palette = QPalette()
    if dark:
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(20, 20, 20))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
    else:
        palette = app.style().standardPalette()

    app.setPalette(palette)


def set_dark_titlebar(hwnd: int, enable: bool):
    """Set Windows title bar theme (dark/light)."""
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    value = ctypes.c_int(1 if enable else 0)
    ctypes.windll.dwmapi.DwmSetWindowAttribute(
        hwnd,
        DWMWA_USE_IMMERSIVE_DARK_MODE,
        ctypes.byref(value),
        ctypes.sizeof(value)
    )


def apply_theme(app: QApplication, hwnd: int | None = None):
    """Apply both Qt palette + Windows title bar theme."""
    dark = is_windows_dark_mode()
    apply_palette(app, dark)
    if hwnd:
        set_dark_titlebar(hwnd, dark)
    return dark
