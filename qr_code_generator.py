import qrcode as qr

data = input("Enter your text or URL here: ").strip()
filename = input("Enter your filename here: ").strip()
your_QRCode  = qr.QRCode(box_size=10, border = 4)
your_QRCode.add_data(data)
image = your_QRCode.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"Your QR Code has saved as {filename}")
