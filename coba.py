# -------------komentar-------------
# untuk coba coba lib

tokenTemp = ['jalan', 'bebas', 'hambat']
hasilNGram1 = ['aku', 'jalan', 'bebas', 'hambat', 'hambat', 'tarik', 'napas', 'habis', 'buat', 'orak', 'senyum', 'jalan']
hasilNGram2 = ['aku jalan', 'jalan bebas', 'bebas hambat', 'hambat tarik', 'tarik napas', 'napas habis', 'habis buat', 'buat orak', 'orak senyum', 'senyum jalan']

for kata in tokenTemp:
    for kataParam in hasilNGram1:
        if kataParam == kata:
            hasilNGram1.remove(kataParam)
            break
    for kataParam in hasilNGram2:
        if kataParam == kata:
            hasilNGram2.remove(kataParam)
            break

print(hasilNGram1)
