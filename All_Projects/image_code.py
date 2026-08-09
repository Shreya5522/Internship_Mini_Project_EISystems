import qrcode

url = "https://drive.google.com/file/d/1w2-fmVBzXLFFSsvaVNiH09gQcrHtLDpF/view?usp=sharing"
qr = qrcode.make(url)
qr.save("images.png")
print("QR code generated successfully!")