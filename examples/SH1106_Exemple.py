import machine
import sh1106_lt
import fontlib
import framebuf
 
screen_width = 128
screen_height = 64
 
i2c = machine.I2C(1,sda=machine.Pin(14), scl=machine.Pin(15))
oled = sh1106_lt.SH1106_I2C(screen_width, screen_height, i2c,flip=True)
oled.fill(1)
oled.show()
 
five = fontlib.font("five (5,5).bmp") # Loads font to ram

 
fbuf = framebuf.FrameBuffer(oled.buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)

fontlib.prt("The Quick Gray",0,0,1,fbuf,five) # prints text using font
fontlib.prt("Fox Jumped Over",0,10,1,fbuf,five) # prints text using font
fontlib.prt("The Lazy Dog",0,20,1,fbuf,five) # prints text using font
oled.show()
