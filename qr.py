import pyqrcode 
from pyqrcode import QRCode 
s = str(input())
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 