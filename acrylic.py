import ctypes

# --- struct ---
class ACCENT_POLICY(ctypes.Structure):
    _fields_ = [("AccentState", ctypes.c_int),
                ("AccentFlags", ctypes.c_int),
                ("GradientColor", ctypes.c_uint),
                ("AnimationId", ctypes.c_int)]

class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
    _fields_ = [("Attribute", ctypes.c_int),
                ("Data", ctypes.c_void_p),
                ("SizeOfData", ctypes.c_size_t)]

SetWindowCompositionAttribute = ctypes.windll.user32.SetWindowCompositionAttribute

# --- tiện ích gộp alpha + rgb thành ARGB ---
def make_argb(alpha, r, g, b):
    return (alpha << 24) | (r << 16) | (g << 8) | b

# --- hàm enable acrylic ---
def enable_acrylic(hwnd, alpha=0xCC, rgb=(0, 0, 0)):
    color = make_argb(alpha, *rgb)
    accent = ACCENT_POLICY()
    accent.AccentState = 4  # Acrylic blur
    accent.AccentFlags = 2  # Quan trọng để bật blur
    accent.GradientColor = color
    accent.AnimationId = 0

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19
    data.Data = ctypes.cast(ctypes.byref(accent), ctypes.c_void_p)
    data.SizeOfData = ctypes.sizeof(accent)

    SetWindowCompositionAttribute(hwnd, ctypes.byref(data))
