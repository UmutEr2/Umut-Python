dosya_adı = "topla.txt"


dosya = open(dosya_adı, "r")
satırlar = dosya.readlines()
dosya.close()


toplam = 0
for satır in satırlar:
    toplam += int(satır.strip())


dosya = open(dosya_adı, "a")
dosya.write("\ntoplam: " +
            str(toplam))
dosya.close()

print("toplam eklendi")
