import qrcode 
img = qrcode.make("helloe john doe!")
img.save("mycode.png")