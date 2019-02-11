# -------------komentar-------------
# untuk coba coba lib

from nltk.tokenize import sent_tokenize, word_tokenize

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# kata = 'menyapu-nyapu lantai dengan sapu, seolah-olah semangatku berkobar-kobar'
kata = 'seharusnya setidaknya'
print(stemmer.stem(kata))