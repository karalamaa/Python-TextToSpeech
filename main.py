#Kullanıcının girdiği yazıyı seslendiren program.
#A program that speaks the text written by the user.

import pyttsx3

# Initialize the engine
engine = pyttsx3.init()
print("Girilen yazıyı seslendiren programa hoş geldiniz...")

file_name = 1 # oluşturulmak istenen txt ve mp3 dosyaları için isim olacak değişkenim.

# Kullanıcı tekrar denemek isterse diye döngü oluşturdum.
while True:
    text_input = input("Enter the text to be spoken: ")# kullanıcıdan yazı aldık

    # Konuşma hızının ayarlanması. Değer 150'den büyük olmalıdır.
    engine.setProperty(name='rate',value=160)

    # Konuşma ses seviyesinin ayarlanması. Değer 0 ile 1 arasında olmalıdır.
    engine.setProperty(name="volume",value=0.3)

    #Kullanıcının yazdığı yazıyı seslendiren kod.
    engine.say(text_input)

    engine.runAndWait()

    while True:
        kayit = input("Konuşmayı mp3 dosyası ve text olarak saklamak ister misiniz?(e/h): ")
        try:
            if kayit == "e":
                yer = input("Kayıt edilecek adresi giriniz: ")
                # Seslendirmenin kaydedilmesi. Girilen yazı seslendirildikten sonra mp3 formatında kaydedilir..
                engine.save_to_file(text_input, filename=f'{yer}\\{file_name}.mp3')
                engine.runAndWait()
                print("Konuşma mp3 dosyası olarak oluşturuluyor.....")
                with open(f"{yer}\\{file_name}.txt",mode="a") as dosya:
                    dosya.write(text_input)
                    print("Girilen text kaydediliyor.....")
                break
            elif kayit == "h":
                break
        except:
            print("Lütfen sadece e veya h harflerinden birini giriniz!!!")

    yeni_talep = input("Yeniden denemek ister misiniz?(e/h): ")
    if yeni_talep == "e":
        file_name = file_name+1
        pass
    elif yeni_talep == "h":
        break





