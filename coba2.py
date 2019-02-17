# -------------komentar-------------
# untuk coba coba lib

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
getStopWord = factory.get_stop_words()

print(getStopWord)

data = ['agi', 'yang', 'ganteng', 'itu', 'ada', 'aduh', 'tidak', 'tahan', 'tidak', 'yang', 'itu']
hasil = []

for kata in data:
    hasil.append(stopword.remove(kata))

# print(hasil)