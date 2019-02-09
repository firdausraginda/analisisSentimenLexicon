# -------------1. register lib-------------

# tokenization
from nltk.tokenize import sent_tokenize, word_tokenize

# stemming
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

#stopword removal
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

# -------------2. global variable-------------
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
data = 'Pak andit kalau mengajar bicaranya cepat sekali jadi sulit untuk memahami materi pelajaran dikelas. Lebih baik saat mengajar jangan terlalu cepat karena materinya sulit dan akan lebih sulit untuk dipahami yang jika penjelasannya terlalu cepat yang.'

# -------------3. stopword removal dan case conversion-------------
def stopwordRemoval(data):
    hasil = stopword.remove(data.lower())
    return hasil

# -------------4. punctuation removal-------------
def punctuationRemoval(data):
    hasil = ''
    for char in data:
        if char not in punctuations:
            hasil = hasil + char
    return hasil

# -------------5. stemming-------------
def stemmingWord(data):
    hasil = stemmer.stem(data)
    return hasil

# -------------6. tokenisasi-------------
def tokenization(data):
    hasil = word_tokenize(data)
    return hasil
    
# -------------7. main program-------------
hasilStopwordCaseConv = stopwordRemoval(data)
hasilNoPunct = punctuationRemoval(hasilStopwordCaseConv)
hasilStem = stemmingWord(hasilNoPunct)
hasilToken = tokenization(hasilStem)

print(hasilToken)