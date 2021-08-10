# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "linkedin.com/in/jayasakthi-j-r-45aa4a205"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqrforlinkedin.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqrforlinkedin.png', scale = 6)
