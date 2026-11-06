import os

class Ogrenci:
    def __init__(self, numara, ad, soyad, ortalama=None):  # None: Boş/Bilinmeyen/Atanmamış değer
        self.numara = numara
        self.ad = ad
        self.soyad = soyad
        self.ortalama = ortalama
    
    def not_gir(self, ortalama):
        if 0 <= ortalama <= 100:
            self.ortalama = ortalama
        else:
            print("Geçersiz not aralığı (0-100 olmalı)")
    
    def bilgileri_goster(self):   
        sonuc = (
                  f"{self.numara} - {self.ad} {self.soyad}, "
                  f"Ortalama: {self.ortalama if self.ortalama is not None else 'Henüz not girilmedi'}"
                )
        return sonuc

                  
def menu_goster():
    
    print("\nÖğrenci Bilgi Sistemi")
    print("- - - - - - - - - - -")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrencileri Listele")
    print("4. Öğrenci Not Gir")
    print("5. Öğrenci Bilgilerini Göster")
    print("6. Okuldaki Tüm Öğrencilerin Not Ortalamasını Göster")
    print("7. Çıkış")


def ogrencileri_dosyadan_yukle(dosya_yolu):
    ogrenciler = {}
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()  # readlines() ile tüm satırları liste olarak oku         
            for satir in satirlar:
                satir = satir.strip()     # Satır sonundaki boşlukları ve \n karakterlerini temizler
                numara, ad, soyad, ortalama = satir.split(",")
                if ortalama == "None":
                    ogrenciler[numara] = Ogrenci(numara, ad, soyad)
                else:
                    ogrenciler[numara] = Ogrenci(numara, ad, soyad, float(ortalama))
    return ogrenciler

def ogrencileri_dosyaya_kaydet(dosya_yolu, ogrenciler):
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        for ogrenci in ogrenciler.values():
            dosya.write(f"{ogrenci.numara},{ogrenci.ad},{ogrenci.soyad},{ogrenci.ortalama}\n")  
            

def okul_ortalama_hesapla(ogrenciler):
    if len(ogrenciler) == 0:
        print("Henüz öğrenci eklendmediği için ortalama hesaplanamaz!")
        return
    
    toplam = 0
    not_girilen_ogrenci_sayisi = 0

    for ogrenci in ogrenciler.values():
        if ogrenci.ortalama is not None:
            toplam += ogrenci.ortalama
            not_girilen_ogrenci_sayisi += 1
    
    if not_girilen_ogrenci_sayisi > 0:
        okul_ortalamasi = toplam / not_girilen_ogrenci_sayisi
    else:
        okul_ortalamasi = 0
    
    print(f"Okulun genel not ortalaması: {okul_ortalamasi}")

def main():
    dosya_yolu = "C:/Python/veriler.txt"
    ogrenciler = ogrencileri_dosyadan_yukle(dosya_yolu)

    while True:
        menu_goster()
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            numara = input("Öğrenci numarası girin: ")
            ad = input("Öğrenci adı girin: ")
            soyad = input("Öğrenci soyadı girin: ")
            if numara in ogrenciler:
                print("Bu öğrenci no zaten mevcut!")
            else:
                ogrenciler[numara] = Ogrenci(numara, ad, soyad)
                print(f"{ad} {soyad} eklendi.")

        elif secim == "2":
            numara = input("Silinecek öğrenci numarası: ")
            if numara in ogrenciler:
                del ogrenciler[numara]
                print(f"Öğrenci {numara} silindi")
            else:
                print("Öğrenci bulunamadı!")

        elif secim == "3":
            if len(ogrenciler) > 0:
                print("\nÖğrenci Listesi:")
                for ogrenci in ogrenciler.values():
                    print(ogrenci.bilgileri_goster())
            else:
                print("Henüz öğrenci eklenmemiş!")
                    
        elif secim == "4":
            numara = input("Notu girilecek öğrenci numarası: ")
            if numara in ogrenciler:
                try:
                    ortalama = float(input("Ortalama not girin (0-100): "))
                    ogrenciler[numara].not_gir(ortalama)
                    print("Not başarıyla eklendi!")
                except ValueError:
                    print("Geçersiz not! Lütfen sayı girin.")
            else:
                print("Öğrenci bulunamadı!")

        elif secim == "5":
            numara = input("Bilgilerini görmek istediğiniz öğrenci no: ")
            if numara in ogrenciler:
                print(ogrenciler[numara].bilgileri_goster())
            else:
                print("Öğrenci bulunamadı!")

        elif secim == "6":
            okul_ortalama_hesapla(ogrenciler)

        elif secim == "7":
            ogrencileri_dosyaya_kaydet(dosya_yolu, ogrenciler)
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen 1-7 arasında bir sayı giriniz.")


main()























