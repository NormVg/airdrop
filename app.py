import pystray
from PIL import Image, ImageDraw
import threading


width, height = 200, 200
background_color = (0, 0, 0)  
image = Image.new("RGB", (width, height), background_color)


draw = ImageDraw.Draw(image)
center_x, center_y = width // 2, height // 2
radius = 95
circle_color = (255, 255, 255)  # Red

draw.ellipse([(center_x - radius, center_y - radius), 
              (center_x + radius, center_y + radius)], 
             fill=circle_color)






icon = pystray.Icon(
    'test name',
    icon=image)


icon.run()