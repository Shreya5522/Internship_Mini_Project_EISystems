import qrcode

url = "https://www.google.com/"

qr = qrcode.make(url)

qr.save("qrcodemine.png")

print("QR code generated successfully!")