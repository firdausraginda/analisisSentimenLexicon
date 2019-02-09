from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

data = 'semangat pak, cara mengajarnya memotivasi, memberikan hadiah bagi yang nilainya 100, tapi kadang saya merasa bapak menjelaskannya terlalu cepat, atau mungkin karena durasi perkuliahannya yang hanya 2 jam yaa.'

hasil = stopword.remove(data.lower())

print(hasil)