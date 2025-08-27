from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from time import strftime

def create_menubar():
    menubar = QMenuBar()
    menubar.setStyleSheet("""
        QMenuBar {
            font-size: 14px;
            padding: 4px 8px;
        }
    """)

    # gộp time + warning vào 1 widget
    corner = QWidget()
    layout = QHBoxLayout(corner)
    layout.setContentsMargins(5, 0, 5, 0)
    layout.setSpacing(15)

    time_label = QLabel()
    warning = QLabel("⚠️ Thông tin tham khảo, không đảm bảo chính xác 100%. Nguồn: vnstock, yfinance")

    layout.addWidget(warning)
    layout.addWidget(time_label)

    menubar.setCornerWidget(corner)
    menubar.setNativeMenuBar(False)

    # đồng hồ
    timer = QTimer(menubar)
    timer.timeout.connect(lambda: time_label.setText(strftime("%H:%M:%S")))
    timer.start(1000)
    time_label.setText(strftime("%H:%M:%S"))

    return menubar, time_label, warning
