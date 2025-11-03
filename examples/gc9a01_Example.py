import random
from machine import Pin, SPI
import gc9a01
import framebuf
import fontlib

spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
tft = gc9a01.GC9A01(
    spi,
    dc=Pin(21, Pin.OUT),
    cs=Pin(17, Pin.OUT),
    reset=Pin(20, Pin.OUT),
    #backlight=Pin(14, Pin.OUT),
    rotation=0)

screen_width = 240
screen_height = 240
bytebuffer = bytearray(screen_width * screen_height * 2) #two bytes for each pixel
fbuf = framebuf.FrameBuffer(bytebuffer, screen_width, screen_height, framebuf.RGB565)

IBM_font = fontlib.font("IBM BIOS (8,8).bmp") # Loads font to ram
five = fontlib.font("five (5,5).bmp")
color0 = gc9a01.color565((255,255,255))
color1 = gc9a01.color565((255,0,0))
fbuf.fill(0)
fontlib.prt("the quick brown fox",10,80,0,fbuf,IBM_font,invert = False,color=color0)
fontlib.prt("jumped over the lazy dog",10,90,0,fbuf,IBM_font,invert = False,color=color1)
# prints text using font
tft.blit_buffer(bytebuffer,0,0,screen_width,screen_height)

#bytearray(b'\x00\x00\x00\x00\xff\xff\xff\xff')
#bytearray(b'\xff\xff\xff\xff\x00\x00\x00\xff')