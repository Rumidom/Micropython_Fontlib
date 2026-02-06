import machine
import ssd1306
import fontlib
import framebuf
 
screen_width = 128
screen_height = 64
 
i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(screen_width, screen_height, i2c)
oled.fill(1)
oled.show()
 
five = fontlib.font("five (5,5).bmp") # Loads font to ram
futuristic = fontlib.font("futuristic (5,7).bmp") # Loads font to ram
icons = fontlib.font("icons (5,7).bmp") # Loads font to ram
oldschool = fontlib.font("oldschool (5,7).bmp") # Loads font to ram
 
FontList = [five,icons,futuristic,oldschool]
i = 0
 
fbuf = framebuf.FrameBuffer(oled.buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)
fontlib.prt("The Quick Gray",0,0,1,fbuf,FontList[i]) # prints text using font
fontlib.prt("Fox Jumped Over",0,10,1,fbuf,FontList[i]) # prints text using font
fontlib.prt("The Lazy Dog",0,20,1,fbuf,FontList[i]) # prints text using font
oled.show()
