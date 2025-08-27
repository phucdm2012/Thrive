import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer
from acrylic import enable_acrylic
from get_color import windows_color
from font.font import GetFont

from ui_tabs import create_tabs
from ui_menubar import create_menubar
from theme import apply_palette, is_windows_dark_mode


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thrive")
        self.setMinimumSize(1100, 600)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        font = GetFont()
        self.setFont(font)

        # Tabs
        self.tabs = create_tabs(font)

        # Menubar
        self.menubar, self.time_label, self.warning = create_menubar()

        # Layout
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.tabs)
        layout.addWidget(self.menubar)
        central.setLayout(layout)
        central.setStyleSheet("background: transparent;")
        self.setCentralWidget(central)

        # Theme init
        self.current_dark = is_windows_dark_mode()
        apply_palette(QApplication.instance(), self.current_dark)

        # ===== Vòng lặp check theme =====
        self.theme_timer = QTimer(self)
        self.theme_timer.timeout.connect(self.check_theme_update)
        self.theme_timer.start(100)  # check mỗi 1 giây

    def check_theme_update(self):
        dark_now = is_windows_dark_mode()
        if dark_now != self.current_dark:
            self.current_dark = dark_now
            apply_palette(QApplication.instance(), self.current_dark)

    def closeEvent(self, event):
        """App thoát thì dừng timer"""
        self.theme_timer.stop()
        super().closeEvent(event)

    def showEvent(self, e):
        hwnd = int(self.winId())
        enable_acrylic(hwnd, 0xFF, windows_color())
        super().showEvent(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec())
