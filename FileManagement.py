import time
import json

def convert(charstr):
    if charstr == "Jan":
        return "Ocak"
    elif charstr == "Feb":
        return "Şubat"
    elif charstr == "Mar":
        return "Mart"
    elif charstr == "Apr":
        return "Nisan"
    elif charstr == "May":
        return "Mayıs"
    elif charstr == "Jun":
        return "Haziran"
    elif charstr == "Jul":
        return "Temmuz"
    elif charstr == "Aug":
        return "Ağustos"
    elif charstr == "Sep":
        return "Eylül"
    elif charstr == "Oct":
        return "Ekim"
    elif charstr == "Nov":
        return "Kasım"
    elif charstr == "Dec":
        return "Aralık"
    
variablex = time.localtime()
datentimex =time.strftime("%c", variablex)
day = datentimex[8:10]
month = datentimex[4:7]
monthstr = convert(month)
year = datentimex[20:24]
hournminx = datentimex[11:16]
hour = int(hournminx[0:2])
min = int(datentimex[14:16])

def display_menu():
    print("╔═════════════════════════════════════╗")
    print("║         PERSONEL  YÖNETİMİ          ║")
    print("╠═════════════════════════════════════╣")
    print("║  1. İşe Alım                        ║")
    print("║  2. İş Akdinin Feshi                ║")
    print("║  3. Personel Bilgisi Alma           ║")
    print("║  4. Personel Listeleme              ║")
    print("║  5. Mesai                           ║")
    print("║  6. İzin                            ║")
    print("║  7. Avans                           ║")
    print("║  8. Prim                            ║")
    print("║  9. Ekipman-Kıyafet                 ║")
    print("║ 10. Yemek Ticket                    ║")
    print("║ 11. Departman Güncelleme            ║")
    print("║ 12. Maaş Güncelleme                 ║")
    print("║ 13. Vardiya Güncelleme              ║")
    print("║ 14. Davalı Personeller              ║")
    print("║[EOT] Programı Sonlandırmak          ║")
    print("╚═════════════════════════════════════╝")

def save_to_file(employeedict, filename="datas.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(employeedict, file, ensure_ascii=False, indent=4)
            print("Çalışan verileri başarıyla kaydedildi.")
    except Exception as e:
        print("Veriler kaydedilirken bir hata oluştu:", e)

def load_from_file(filename="datas.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Kayıtlı çalışan verisi bulunamadı. Yeni bir dosya oluşturulacak.")
        return {}
    except json.JSONDecodeError:
        print("Dosya okunamadı. Boş bir çalışan listesiyle başlayacağız.")
        return {}
    
def ise_alim():
    while True:
        print("╔═══════════════════════╗")
        print("║        İşe Alım       ║")
        print("╠═══════════════════════╣")
        print("║ 1 - Personel Alım     ║")
        print("║ 2 - Çıkış             ║")
        print("╚═══════════════════════╝")

        secim = input("\n➤ Yapmak İstediğiniz İşlemi Seçiniz (1 veya 2) : ")

        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı - Soyadı : ")
            departman = input("\n➤ Çalıştığı Departman : ")
            maas = int(input("\n➤ Maaşı : "))
            sube = input("\n➤ Çalıştığı Şube : ")
            vardiya = input("\n➤ Vardiya Saati (giriş saati - çıkış saati) : ")

            new_employee = employee_template.copy()
            new_employee["maaş"] = maas
            new_employee["departman"] = departman
            new_employee["şube"] = sube
            new_employee["işe_alım_tarihi"] = day + " " + monthstr + " " + year
            new_employee["vardiya"] = vardiya
            new_employee["durum"] = "Aktif"

            employeedict[adSoyad] = new_employee
            save_to_file(employeedict)
        elif secim == "2":
            print("\nÇıkış yapılıyor...")
            break
        else: print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyiniz.")

def is_akdinin_feshi():
    while True:
        print("╔═════════════════════════╗")
        print("║   1 - İş Akdinin Feshi  ║")
        print("║        2 - Çıkış        ║")
        print("╚═════════════════════════╝")

        secim = input("\n➤ Yapmak İstediğiniz İşlemi Seçin (1 veya 2) : ")

        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad in employeedict:
                fesihSebebi = input("\n➤ İşten Ayrılma Sebebi : ")
                fesihTarihi = input("\n➤ İşten Ayrılma Tarihi : ")
                employeedict[adSoyad]["durum"] = "Çıkış"
                employeedict[adSoyad]["fesih_sebebi"] = fesihSebebi
                employeedict[adSoyad]["fesih_tarihi"] = fesihTarihi
                save_to_file(employeedict)

            else: print(f"{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyin.")
        elif secim == "2":
            print("\nÇıkış yapılıyor...")
            break
        else: print("\nHatalı seçim yaptınız. Lütfen tekrar deneyiniz.")

def personel_bilgisi_alma():
    adSoyad = input("\n➤ Personelin Adı - Soyadı : ")
    if adSoyad in employeedict:
        print("\n" + "═" * 50)
        print(f"        ÇALIŞAN BİLGİLERİ: {adSoyad.upper()}")
        print("═" * 50)

        print(f"Adı-Soyadı       : {adSoyad}")
        print(f"Maaş             : {employeedict[adSoyad]['maaş']} ₺")
        print(f"Departman        : {employeedict[adSoyad]['departman']}")
        print(f"Şube             : {employeedict[adSoyad]['şube']}")
        print(f"İşe Alım Tarihi  : {employeedict[adSoyad]['işe_alım_tarihi']}")
        print(f"Vardiya          : {employeedict[adSoyad]['vardiya']}")
        print(f"Durum            : {employeedict[adSoyad]['durum']}")

        if employeedict[adSoyad]["durum"] == "Çıkış":
            print(f"İş Çıkış Tarihi  : {employeedict[adSoyad].get('fesih_tarihi', 'Belirtilmemiş')}")
        
        print("\n" + "═" * 50)

        if "mesai" in employeedict[adSoyad]:
            print("\n   ➤ Mesai Bilgisi : ")
            for ay, toplam_dakika in employeedict[adSoyad]["mesai"].items():
                saat = dakika // 60
                dakika = toplam_dakika % 60
                print(f"     - {ay.capitalize()}: {saat} saat, {dakika} dakika")
        else: print("\n   ➤ Mesai Bilgisi : Yok")

        if employeedict[adSoyad]["izin"]:
            print("\n   ➤ İzin Bilgisi : ")
            for key, value in employeedict[adSoyad]["izin"].items():
                print(f"     - {key.capitalize()}: {value}")
        else: print("\n   ➤ İzin Billgisi : Yok")

        if employeedict[adSoyad]["avans"]:
            print("\n   ➤ Avans Bilgisi:")
            for key, value in employeedict[adSoyad]["avans"].items():
                print(f"     - {key.capitalize()}: {value}")
        else:
            print("\n   ➤ Avans Bilgisi: Yok")

        if any(employeedict[adSoyad]["prim"].values()):
            print("\n   ➤ Prim Bilgisi:")
            for key, value in employeedict[adSoyad]["prim"].items():
                print(f"     - {key.capitalize()}: {value}")
        else:
            print("\n   ➤ Prim Bilgisi: Yok")

        if employeedict[adSoyad]["ekipman_kiyafet"]:
            print(f"\n   ➤ Ekipman ve Kıyafet Bilgisi: {employeedict[adSoyad]['ekipman_kiyafet']}")
        else:
            print("\n   ➤ Ekipman ve Kıyafet Bilgisi: Yok")

        if employeedict[adSoyad]["yemek_ticket"]:
            print(f"\n   ➤ Yemek Ticket Bilgisi: {employeedict[adSoyad]['yemek_ticket']} ₺")
        else:
            print("\n   ➤ Yemek Ticket Bilgisi: Yok")

        print("\n" + "═" * 50)
    else:
        print(f"\n{adSoyad} bulunamadı.")
    
def personel_listeleme():
    while True:
        print("╔═════════════════════════════════════════════════════╗")
        print("║                 Listeleme İşlemleri                 ║")
        print("╠═════════════════════════════════════════════════════╣")
        print("║ 1 - Tüm Personelleri Listele                        ║")
        print("║ 2 - Belirli Bir Departmandaki Personelleri Listele  ║")
        print("║ 3 - Çıkış                                           ║")
        print("╚═════════════════════════════════════════════════════╝")
        islem = input("\n➤ Yapmak İstediğiniz İşlemi Seçin (1, 2 veya 3): ")

        if islem == "1":
            print("\nTüm Çalışanlar : ")
            print("-" * 40)
            for adSoyad, bilgiler in employeedict.items():
                print(f"Adı-Soyadı : {adSoyad}")
                print(f"Departman  : {bilgiler['departman']}")
                print(f"Maaş       : {bilgiler['maaş']} ₺")
                print(f"Şube       : {bilgiler['şube']}")
                print(f"Durum      : {bilgiler['durum']}")
                print("-" * 40)
        
        elif islem == "2":
            departman_adi = input("\n➤ Lütfen departman adı giriniz : ")
            print(f"\n{departman_adi} Departmanındaki Çalışanlar:")
            print("-" * 40)
            found = False
            for adSoyad, bilgiler in employeedict.items():
                if bilgiler["departman"] == departman_adi:
                    print(f"Adı-Soyadı : {adSoyad}")
                    print(f"Maaş       : {bilgiler['maaş']} ₺")
                    print(f"Şube       : {bilgiler['şube']}")
                    print(f"Durum      : {bilgiler['durum']}")
                    print("-" * 40)
                    found = True
            if not found:
                print(f"{departman_adi} departmanında hiçbir çalışan bulunamadı.")

        elif islem == "3":
            print("\nÇıkış yapılıyor...")
            break



def mesai():
    while True:
        print("╔════════════════════════════════╗")
        print("║         Mesai İşlemleri        ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - Mesai Ekleme               ║")
        print("║ 2 - Mesaiye Kalan Personeller  ║")
        print("║ 3 - Çıkış                      ║")
        print("╚════════════════════════════════╝")
        islem = input("\n➤ Yapmak İstediğiniz İşlemi Seçin (1, 2 veya 3): ")

        if islem == "1":
            adSoyad = input("\n➤ Mesaiye Kalan Personelin Adı-Soyadı : ")
            if adSoyad in employeedict:
                mesaiSaat = int(input("\n➤ Mesaiye Kaldığı Süre (Saat) : "))
                mesaiDakika = int(input("\n➤ Mesaiye Kaldığı Süre (Dakika) : "))
                mesaiTarihi = input("\n➤ Mesai Tarihi (Gün-Ay-Yıl) : ")

                toplam_mesai = mesaiSaat * 60 + mesaiDakika

                if "mesai" not in employeedict[adSoyad]:
                    employeedict[adSoyad]["mesai"] = {}

                mesai_ay = mesaiTarihi.split("-")[1]

                if mesai_ay in employeedict[adSoyad]["mesai"]:
                    employeedict[adSoyad]["mesai"][mesai_ay] += toplam_mesai
                else:
                    employeedict[adSoyad]["mesai"][mesai_ay] = toplam_mesai

                print(f"\n{adSoyad} adlı personelin {mesai_ay} ayı için toplam mesai saati: {employeedict[adSoyad]['mesai'][mesai_ay]} dakika.")

                save_to_file(employeedict)

            else:
                print(f"\n{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")

        elif islem == "2":
            print("\n   ➤ Mesaiye Kalan Personeller:")
            for adSoyad, bilgiler in employeedict.items():
                if "mesai" in bilgiler and bilgiler["mesai"]:
                    print(f"   - {adSoyad}: {sum(bilgiler['mesai'].values())} dakika mesai yapmış.")
            print()

        elif islem == "3":
            print("Çıkış yapılıyor...")
            break

        else: print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

        save_to_file(employeedict)

def izin():
    while True:
        print("╔═══════════════════════╗")
        print("║     İzin İşlemleri    ║")
        print("╠═══════════════════════╣")
        print("║ 1 - İzin verme        ║")
        print("║ 2 - Çıkış             ║")
        print("╚═══════════════════════╝")

        secim = input("\n➤ Yapmak istediğiniz işlemi seçin (1 veya 2) : ")

        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı-Soyadı : ")
            if adSoyad in employeedict:
                raporlu_mu = input("\n➤ Personelin sağlık raporu bulunuyor mu? (evet/hayır) : ")
                if raporlu_mu == "evet":
                    izinSuresi = input("\n➤ İzin Süresi (yıl-ay-gün) : ")
                    izinTarihi = input("\n➤ İzine Çıktığı Tarih (gg-aa-yyyy) : ")
                    employeedict[adSoyad]["izin"] = {"sebep": "Sağlık Raporlu", "süre": izinSuresi, "tarih": izinTarihi}
                    save_to_file(employeedict)
                elif raporlu_mu == "hayır":
                    izinSebebi = input("\n➤ İzin Sebebi : ")
                    izinSuresi = input("\n➤ İzin Süresi (yıl-ay-gün) : ")
                    izinTarihi = input("\n➤ İzine Çıktığı Tarih (gg-aa-yyyy) : ")
                    employeedict[adSoyad]["izin"] = {"sebep": "Sağlık Raporlu", "süre": izinSuresi, "tarih": izinTarihi}
                    save_to_file(employeedict)
                else: print("Hatalı bilgi girdiniz. Lütfen tekrar deneyin.")
            elif adSoyad not in employeedict:
                print(f"{adSoyad} adlı personel bulunamadi. Lütfen tekrar deneyiniz.")
        elif secim == "2":
            print("\nÇıkış yapılıyor.")
            break

def avans():
    while True:
        print("╔════════════════════════╗")
        print("║     Avans İşlemleri    ║")
        print("╠════════════════════════╣")
        print("║ 1 - Avans verme        ║")
        print("║ 2 - Çıkış              ║")
        print("╚════════════════════════╝")

        secim = input("\n➤ Yapmak istediğiniz işlemi seçin (1 veya 2) : ")
        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad in employeedict:
                avansMiktari = int(input("\n➤ Avans Mikatrı (₺) : "))
                avansTarihi = input("\n➤ Avans Verilen Tarih (gg-aa-yyyy) : ")
                employeedict[adSoyad]["avans"] = {"miktar": avansMiktari, "tarih": avansTarihi}
                save_to_file(employeedict)
            else: print(f"{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")
        elif secim == "2":
            print("\Çıkış yapılıyor...")
            break

def prim():
    while True:
        print("╔══════════════════════╗")
        print("║     Prim İşlemleri   ║")
        print("╠══════════════════════╣")
        print("║   1 - Prim Verme     ║")
        print("║      2 - Çıkış       ║")
        print("╚══════════════════════╝")

        secim = input("\n➤ Yapmak istediğiniz işlemi seçin (1 veya 2) : ")

        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad in employeedict:
                primYuzdesi = int(input("\n➤ Prim Yüzdesi : "))
                primMiktari = (employeedict[adSoyad]["maaş"]) / 100 * primYuzdesi  # Prim miktarını yüzdeye göre hesapla
                print(f"\n{adSoyad} adlı personelin prim miktarı aylık {primMiktari} ₺ olarak hesaplanmıştır.")
                
                employeedict[adSoyad]["prim"] = {"yüzde": primYuzdesi, "miktar": primMiktari}
                save_to_file(employeedict)
            else:
                print(f"\n{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")
        elif secim == "2":
            print("Çıkış yapılıyor...")
            break


def ekipman_kiyafet():
    while True:
        print("╔═══════════════════════╗")
        print("║   Ekipman İşlemleri   ║")
        print("╠═══════════════════════╣")
        print("║ 1 - Ekipman Verme     ║")
        print("║ 2 - Ekipman Silme     ║")
        print("║ 3 - Mevcut Ekipmanlar ║")
        print("║ 4 - Çıkış             ║")
        print("╚═══════════════════════╝")

        secim = input("\n➤ Yapmak istediğiniz işlemi seçin (1, 2, 3 veya 4): ")
        
        if secim == "1":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad not in employeedict: print(f"\n{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")
            if adSoyad in employeedict:
                yeni_ekipman = input("\n➤ Yeni Ekipmanlar/Kıyafetler : ")
                if employeedict[adSoyad]["ekipman_kiyafet"]:
                    employeedict[adSoyad]["ekipman_kiyafet"].append(yeni_ekipman)
                else:
                    employeedict[adSoyad]["ekipman_kiyafet"] = [yeni_ekipman]
                print(f"\n{adSoyad} için ekipman bilgisi başarıyla eklendi.")
        elif secim == "2":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad not in employeedict: print(f"\n{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")
            if adSoyad in employeedict:
                if not employeedict[adSoyad]["ekipman_kiyafet"]:
                    print(f"\n{adSoyad} için mevcut ekipman bilgisi bulunmamaktadır.")
                print("\nMevcut Ekipmanlar : ")
                for i, ekipman in enumerate(employeedict[adSoyad]["ekipman_kiyafet"], 1):
                    print(f"{i}.{ekipman}")
                
                silinecek = input("\n➤ Silmek istediğiniz ekipmanların numaralarını girin (virgül ile ayırın) : ")

                try:
                    silinecek = [int(num.strip()) for num in silinecek.split(',')]

                    for numara in sorted(silinecek, reverse = True):
                        if 1 <= numara <= len(employeedict[adSoyad]["ekipman_kiyafet"]):
                            silinen_ekipman = employeedict[adSoyad]["ekipman_kiyafet"].pop(numara - 1)
                            print(f"\n{silinen_ekipman} ekipman bilgisi başarıyla silindi.")
                        else: print(f"\nGeçersiz numara : {numara}")
                except ValueError:
                    print("Lütfen geçerli numaralar girin (örneğin: 1, 2, 3).")

        elif secim == "3":
            adSoyad = input("\n➤ Personelin Adı Soyadı : ")
            if adSoyad not in employeedict: print(f"\n{adSoyad} adlı personel bulunamadı. Lütfen tekrar deneyiniz.")
            if adSoyad in employeedict:
                if not employeedict[adSoyad]["ekipman_kiyafet"]:
                    print(f"\n{adSoyad} için mevcut ekipman bilgisi bulunmamaktadır.")
                print("\nMevcut Ekipmanlar : ")
                for i, ekipman in enumerate(employeedict[adSoyad]["ekipman_kiyafet"], 1):
                    print(f"{i}.{ekipman}")
        
        elif secim == "4":
            print("\nÇıkış yapılıyor...")
            break

        else: print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.")

def yemek_ticket():
    biletler = {}

    while True:
        print("╔════════════════════════════════╗")
        print("║    Yemek Ticket İşlemleri      ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - Ticket Verme               ║")
        print("║ 2 - Ticket Limitini Güncelleme ║")
        print("║ 3 - Ticket Silme               ║")
        print("║ 4 - Çıkış                      ║")
        print("╚════════════════════════════════╝")
        islem = input("\n➤ Yapmak İstediğiniz İşlemi Seçin (1, 2, 3 veya 4): ")

        if islem == "1":
            kisi_adi = input("➤ Ticket verilecek kişinin adını girin: ")
            if kisi_adi in biletler:
                print(f"{kisi_adi} zaten kayıtlı. Mevcut limit: {biletler[kisi_adi]:.2f} TL")
            else:
                limit = float(input(f"➤ {kisi_adi} için bilet limiti (TL) belirleyin: "))
                biletler[kisi_adi] = limit
                print(f"{kisi_adi} için {limit:.2f} TL limitli ticket oluşturuldu.")

        elif islem == "2":
            kisi_adi = input("➤ Limiti güncellenecek kişinin adını girin: ")
            if kisi_adi in biletler:
                yeni_limit = float(input(f"➤ {kisi_adi} için yeni bilet limitini girin: "))
                biletler[kisi_adi] = yeni_limit
                print(f"{kisi_adi} için bilet limiti {yeni_limit:.2f} TL olarak güncellendi.")
            else:
                print(f"{kisi_adi} adına kayıtlı bir bilet bulunamadı!")

        elif islem == "3":
            kisi_adi = input("➤ Silinecek kişinin adını girin: ")
            if kisi_adi in biletler:
                del biletler[kisi_adi]
                print(f"{kisi_adi} adına kayıtlı bilet limiti silindi.")
            else:
                print(f"{kisi_adi} adına kayıtlı bir bilet bulunamadı!")

        elif islem == "4":
            print("İşlem sonlandırılıyor... Teşekkürler!")
            break

        else:
            print("Hatalı seçim! Lütfen 1, 2, 3 veya 4 arasında bir değer girin.")

def departman_guncelleme():
    adSoyad = input("\n➤ Personelin Adı-Soyadı : ")
    if adSoyad in employeedict:
        eski_departman = employeedict[adSoyad]["departman"]
        print(f"Eski Departman: {eski_departman}")
        yeni_departman = input("\n➤ Yeni Departmanı : ")
        employeedict[adSoyad]["departman"] = yeni_departman
        save_to_file(employeedict)
    else:
        print(f"{adSoyad} bulunamadı.")

def maas_guncelleme():
    adSoyad = input("\n➤ Personelin Adı-Soyadı : ")
    if adSoyad in employeedict:
        eski_maas = employeedict[adSoyad]["maaş"]
        print(f"Eski Maaş: {eski_maas}")
        yeni_maas_str = input("➤ Yeni Maaşı (₺) : ")
        yeni_maas = int(yeni_maas_str)
        employeedict[adSoyad]["maaş"] = yeni_maas
        save_to_file(employeedict)
    else:
        print(f"{adSoyad} bulunamadı.")
        
def vardiya_guncelleme():
    adSoyad = input("\n➤ Personelin Adı-Soyadı : ")
    if adSoyad in employeedict:
        eski_vardiya = employeedict[adSoyad]["vardiya"]
        print(f"\nEski Vardiya Saati: {eski_vardiya}")
        yeni_vardiya = input("\n➤ Yeni Vardiya Saati (giriş saati-çıkış saati) : ")
        employeedict[adSoyad]["vardiya"] = yeni_vardiya
        save_to_file(employeedict)
    else:
        print(f"{adSoyad} bulunamadı.")

def davali_personeller():
    while True:
        print("╔═══════════════════════════════════╗")
        print("║    Davalı Personel İşlemleri      ║")
        print("╠═══════════════════════════════════╣")
        print("║ 1 - Davalı Personel Ekle          ║")
        print("║ 2 - Davalı Personel Listele       ║")
        print("║ 3 - Davalı Personel Bilgisi Sil   ║")
        print("║ 4 - Çıkış                         ║")
        print("╚═══════════════════════════════════╝")
        secim = input("\n➤ Yapmak istediğiniz işlemi seçin (1, 2, 3 veya 4): ")

        if secim == "1":
            adSoyad = input("\n➤ Davalı Personelin Adı-Soyadı : ")

            if adSoyad not in employeedict:
                print(f"{adSoyad} isimli personel bulunamadı. Önce personeli işe alın.")
                continue

            dava_detaylari = input("\n➤ Dava Detayları : ")
            dava_tarihi = input("\n➤ Dava Açılma Tarihi (gg-aa-yyyy): ")

            if "davalar" not in employeedict[adSoyad]:
                employeedict[adSoyad]["davalar"] = []

            employeedict[adSoyad]["davalar"].append({
                "dava_detaylari": dava_detaylari,
                "dava_tarihi": dava_tarihi
            })
            print(f"{adSoyad} için dava bilgisi başarıyla eklendi.")

        elif secim == "2":
            print("\nDavalı Personel Listesi")
            for adSoyad, bilgiler in employeedict.items():
                if "davalar" in bilgiler and bilgiler["davalar"]:
                    print(f"\n{adSoyad}:")
                    for i, dava in enumerate(bilgiler["davalar"], 1):
                        print(f"  {i}. Dava Detayları: {dava['dava_detaylari']}")
                        print(f"     Dava Tarihi: {dava['dava_tarihi']}")

        elif secim == "3":
            adSoyad = input("\n➤ Davalı Personelin Adı-Soyadı : ")

            if adSoyad not in employeedict or "davalar" not in employeedict[adSoyad] or not employeedict[adSoyad]["davalar"]:
                print(f"{adSoyad} isimli personelin dava bilgisi bulunamadı.")
                continue

            print("\nMevcut Davalar:")
            for i, dava in enumerate(employeedict[adSoyad]["davalar"], 1):
                print(f"  {i}. Dava Detayları: {dava['dava_detaylari']}")
                print(f"     Dava Tarihi: {dava['dava_tarihi']}")

            dava_no = input("\n➤ Silmek istediğiniz dava numarasını girin (Örn: 1, 2, ...): ")
            try:
                dava_no = int(dava_no)
                if 1 <= dava_no <= len(employeedict[adSoyad]["davalar"]):
                    silinen_dava = employeedict[adSoyad]["davalar"].pop(dava_no - 1)
                    print(f"Dava bilgisi başarıyla silindi: {silinen_dava['dava_detaylari']}")
                    if not employeedict[adSoyad]["davalar"]:
                        del employeedict[adSoyad]["davalar"]
                else:
                    print("Geçersiz dava numarası.")
            except ValueError:
                print("Lütfen geçerli bir numara girin.")

        elif secim == "4":
            print("İşlem sonlandırılıyor... Teşekkürler!")
            break

        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

        save_to_file(employeedict)



employee_template = {
    "maaş": 0,
    "departman": "",
    "şube": "",
    "işe_alım_tarihi": "",
    "vardiya": "",
    "durum": "",
    "mesai": {},
    "izin": {},
    "avans": 0,
    "prim": {},
    "ekipman_kiyafet": "",
    "yemek_ticket": "",
    "dava_durumu": {
        "dava_var_mı": False,
        "dava_aciklamasi": "",
        "dava_tarihi": ""
    }
}

employeedict = load_from_file("datas.json")
finish = False

while not finish:
    display_menu()
    islem = input("\n➤ Bir İşlem Seçiniz : ")

    if islem == "EOT":
        finish = True
        print("Program Sonlandırılıyor...")
    elif islem == "1":
        ise_alim()
    elif islem == "2":
        is_akdinin_feshi()
    elif islem == "3":
        personel_bilgisi_alma()
    elif islem == "4":
        personel_listeleme()
    elif islem == "5":
        mesai()
    elif islem == "6":
        izin()
    elif islem == "7":
        avans()
    elif islem == "8":
        prim()
    elif islem == "9":
        ekipman_kiyafet()
    elif islem == "10":
        yemek_ticket()
    elif islem == "11":
        departman_guncelleme()
    elif islem == "12":
        maas_guncelleme()
    elif islem == "13":
        vardiya_guncelleme()
    elif islem == "14":
        davali_personeller()
    else: print("\n Hatalı işlem seçtiniz. Lütfen tekrar deneyiniz.")

print("Programdan çıkılıyor, çalışan verileri kaydedildi.")
