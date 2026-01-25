import fontlib
import st7789 as st7789
import framebuf
from machine import Pin, SPI

screen_width = 240
screen_height = 240
screen_rotation = 3

textH = 8
textW = 240

spi = SPI(1,
          baudrate=31250000,
          polarity=1,
          phase=1,
          bits=8,
          firstbit=SPI.MSB,
          sck=Pin(4),
          mosi=Pin(5))

display = st7789.ST7789(
    spi,
    screen_width,
    screen_height,
    reset=Pin(9, Pin.OUT),
    #cs=Pin(9, Pin.OUT),
    dc=Pin(8, Pin.OUT),
    backlight=Pin(7, Pin.OUT),
    rotation=screen_rotation)

#Because the screen is larger 240x240 pixels creating a buffer for the whole
#screen is impratical as it would consume 240*240*2 = 115.2kb of ram
#we will only update a portion of the screen where the text will be written
textBuffer = bytearray(screen_width * textH * 2) #two bytes for each pixel
textfbuf = framebuf.FrameBuffer(textBuffer, textW, textH, framebuf.RGB565)
textfbuf.fill(0)
display.fill(0)
IBM_font = fontlib.font("IBM BIOS (8,8).bmp") # Loads font to ram
white = st7789.color565(255, 255, 255)

def PrintToScreen(font,text,x,y):
    textW = screen_width
    textH = 8
    textfbuf.fill(0)
    fontlib.prt(text,0,0,1,textfbuf,IBM_font,color=white)
    display.blit_buffer(textBuffer, x, y, textW, textH)

PrintToScreen(IBM_font,'Hello World',0,0)
