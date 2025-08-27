from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class HighlightedTab(QTabWidget):
    def __init__(self, font):
        super().__init__()
        self.setTabShape(QTabWidget.TabShape.Rounded)
        self.setStyleSheet("""
            QTabWidget {
                font-size: 17px;
                background: transparent;
            }

            QTabWidget::pane {
                border: 1px solid #555;
                margin: 0;
                top: -1px;
                background: transparent;
            }

            QTabBar::tab {
                padding: 3px 18px;
                margin: 0px 1px 0px 0px;
                border-top: 1px solid #555;
                border-left: 1px solid #555;
                border-right: 1px solid #555;
                border-radius: 0px;
                height: 25px;
            }

            QTabBar::tab:selected {
                background: transparent;
                border-left: 1px solid #555;
                border-top: 3px solid #55FF74;
                border-right: 1px solid #555;
                height: 25px;
            }
        """)
        self.tabBar().setFont(font)

        # highlight bar
        self.highlight = QWidget(self.tabBar())
        self.highlight.setFixedHeight(3)
        self.highlight.setStyleSheet("background-color: #55FF74;")
        self.highlight.raise_()
        self.highlight.hide()

        # animation
        self.anim = QPropertyAnimation(self.highlight, b"geometry")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.currentChanged.connect(self.animate_highlight)

    def animate_highlight(self, index):
        rect = self.tabBar().tabRect(index)
        new_geom = QRect(rect.left(), 0, rect.width(), self.highlight.height())
        self.highlight.show()
        self.highlight.raise_()

        if not self.highlight.geometry().isValid() or self.highlight.width() == 0:
            self.highlight.setGeometry(new_geom)
            return

        self.anim.stop()
        self.anim.setStartValue(self.highlight.geometry())
        self.anim.setEndValue(new_geom)
        self.anim.start()


def create_tabs(font):
    tab = HighlightedTab(font)

    # ----- Tab: bảng giá -----
    bang_gia = QWidget()
    bang_gia.setLayout(QVBoxLayout())
    tab.addTab(bang_gia, "\ue901")

    # ----- Tab: biểu đồ -----
    bieu_do = QWidget()
    bieu_do.setLayout(QVBoxLayout())
    tab.addTab(bieu_do, "\ue900")
    
    # ----- Tab: máy tính -----
    caculator = QWidget()
    caculator.setLayout(QVBoxLayout())
    tab.addTab(caculator, "\ue902")

    tab.setCurrentIndex(0)
    tab.animate_highlight(0)  # khởi tạo highlight ở tab đầu
    return tab
