import pyqrcode

link = input("QR kod için sayfa urlsi giriniz :")

konum ="C:\\Users\\avsro\Desktop"

qr = pyqrcode.create(link)

qr.svg("kod.svg",scale=5)

