# Micropython Fontlib
A micropython library for displaying 1bit bitmaps as fonts,and displaying 1bit bitmaps sprites, it was first tested on a monocrome screen (pcd8544 nokia screen)  but you should work with any monocrome screen through [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html)

# How to use it
Add fontlib.py and a 1bit font .bmp (should follow the same formatting of the bmp files on the Bitmaps folder) file to your micropython device, then use the library to modify a framebuffer:
```python
import framebuf
import fontlib
import ssd1306
from machine import Pin,I2C

screen_width = 128
screen_height = 32

#ESP8266 scl=Pin(4),sda=Pin(5)
#ESP32 C3 scl=Pin(9),sda=Pin(8)
i2c = I2C(scl=Pin(9),sda=Pin(8))
oled = ssd1306.SSD1306_I2C(screen_width, screen_height, i2c)

spce = 1 # characters spacing
pos_x = 0 # X position on the frame buffer to print the text
pos_y = 0 # Y position on the frame buffer to print the text

five = fontlib.font("five (5,5).bmp") # Loads font to ram 

fbuf = framebuf.FrameBuffer(oled.buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)
fontlib.prt("The Quick Gray",pos_x,pos_y,spce,fbuf,five) # prints text using font
oled.show()
```
see the examples folder on how to use it with diferent displays.

# How create new fonts
Most image editors should be able to save files to 1bit bmp, I recommend [Paint.net](https://www.getpaint.net/), draw 1 pixel padding around each letters, the file name should include the character size, like the fonts found in the fonts folder. on paint.net if you "save as" and choose bmp it will prompt you with "saving configuration" choose the 1bit option. alternatively you can create the font as a normal bmp file and convert it using [Pillow](https://pypi.org/project/pillow/):

```python
from PIL import Image

img = Image.open('input_image.png')
img = img.convert('1')
img.save('output_1bit.bmp')
```

# TODO
- [x] Load fonts directly from 1bit bitmaps
- [x] Support for portuguese special characters (ç,á,é,í,ó,ú,â,ê,ô,ã,õ)(Ç,Á,É,Í,Ó,Ú,Â,Ê,Ô,Ã,Õ).
- [x] Support for color screens

# Available fonts:
[futuristic](https://opengameart.org/content/ascii-bitmap-font-futuristic) :\
<img src='./photos/futuristic.png' width='300'>
<img src='./fonts/futuristic (5,7).bmp' width='300' >\
five:\
<img src='./photos/five.png' width='300'>
<img src='./fonts/five (5,5).bmp' width='300'>\
[oldschool](https://opengameart.org/content/ascii-bitmap-font-oldschool) :\
<img src='./photos/oldschool.png' width='300'>
<img src='./fonts/oldschool (5,7).bmp' width='300'>\
[cellphone](https://opengameart.org/content/ascii-bitmap-font-cellphone) :\
<img src='./photos/cellphone.png' width='300'>
<img src='./fonts/cellphone (5,7).bmp' width='300'>\
icons:\
<img src='./photos/icons.png' width='300'>
<img src='./fonts/icons (5,7).bmp' width='300'>

[IBM BIOS](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_bios) :\
<img src='./photos/gc9a01.jpg' width='300'>
<img src='./fonts/IBM%20BIOS%20(8%2C8).bmp' width='300'>

# LICENSE:
this project is [MIT licensed](https://github.com/Rumidom/micropython_fontlib/blob/main/LICENSE)

# Support
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M41NQV7I)
