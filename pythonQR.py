import qrcode

def createQR(text, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(name)
    
text = input("Enter text: ")

name = "qr_code.png"

createQR(text, name)
print(f"QR code saved as {name}")