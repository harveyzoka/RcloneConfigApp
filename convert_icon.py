from PIL import Image
import sys

try:
    img_path = sys.argv[1]
    img = Image.open(img_path)
    # Ensure it supports transparency if needed
    img = img.convert("RGBA")
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save("app_icon.ico", format="ICO", sizes=icon_sizes)
    print("Icon converted successfully to app_icon.ico!")
except Exception as e:
    print(f"Error converting icon: {e}")
