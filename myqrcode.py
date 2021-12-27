import qrcode
data = input("Enter URL or Text:")
img = qrcode.make(data)
img.save("data.jpg")