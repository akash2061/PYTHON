import pyqrcode
import png
from pyqrcode import QRCode
url1="https://google.com"
url = pyqrcode.create(url1)
url.png('Google.png',scale=6)