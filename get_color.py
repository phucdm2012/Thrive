import winreg

def is_dark_mode():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        )
        val, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return val == 0  # 0 = Dark, 1 = Light
    except:
        return True  # mặc định dark nếu lỗi

def windows_color():
    """Trả về tuple RGB màu nền window gần giống Taskbar theo theme"""
    if is_dark_mode():
        return (32, 32, 32)      # xám tối cho Dark theme
    else:
        return (249, 249, 249)   # xám sáng cho Light theme
