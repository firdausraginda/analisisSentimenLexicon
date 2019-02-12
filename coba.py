# -------------komentar-------------
# untuk coba coba lib

# from stop_words import get_stop_words
# stop_words = get_stop_words('indonesian')
# print(stop_words)

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
getStopWord = factory.get_stop_words()

isiStopWord = getStopWord

nonStopWordArr = ['tidak', 'sementara', 'boleh', 'nggak', 'harus', 'amat', 'supaya', 'agar']
nonStopWordStr = 'tidak sementara boleh nggak harus amat supaya agar'
data = ['agi', 'yang', 'ganteng', 'itu', 'ada', 'aduh', 'tidak', 'tahan', 'tidak', 'yang', 'itu']

# for isi in isiStopWord:
#     for non in nonStopWordArr:
#         if isi == non:
#             isiStopWord.remove(isi)
# print(isiStopWord)
# print(len(isiStopWord))

stopwordCustom = []
for isi in isiStopWord:
    if isi not in nonStopWordArr:
        stopwordCustom.append(isi)
# print(stopwordCustom)
# print(len(stopwordCustom))

hasil = []
for kata in data:
    if kata not in stopwordCustom:
        hasil.append(kata)

print(hasil)