import pytube

def indirme():

    link = input("Video yada müzik linkini giriniz : ")

    konum = "C:\\Users\\avsro\\Desktop"

    dosya = pytube.YouTube(link).streams.get_audio_only().download(konum)

    return dosya

try:
    while True:
        indirme()

except:
    print("Tekrar İndirmeyi Deneyiniz")
    indirme()