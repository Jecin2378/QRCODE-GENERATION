import pyqrcode


link = "https://5staruniversity.com"
qr = pyqrcode.create(link)
qr.png("qrcode.png", scale =6)

qrcode = image.save("qrcode.png")
