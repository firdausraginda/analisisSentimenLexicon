# -------------komentar-------------
# urutan praproses berdasarkan rujukan paper utama

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
data = 'bapa ngajarnya kecepetan, kadang ga kedengeran, coba di pelankan lagi pa.'

# -------------3. stopword removal dan case conversion-------------
def stopwordRemoval(data):
    hasil = []
    hasil2 = []
    for kata in data:
        hasil.append(stopword.remove(kata))
    for kata in hasil:
        if kata != '':
            hasil2.append(kata) 
    return hasil2

# -------------4. punctuation removal-------------
def punctuationRemoval(data):
    hasil = []
    for kata in data:
        if kata not in punctuations:
            hasil.append(kata.lower())
    return hasil

# -------------5. stemming-------------
def stemmingWord(data):
    hasil = []
    for kata in data:
        hasil.append(stemmer.stem(kata))
    return hasil

# -------------6. tokenisasi-------------
def tokenization(data):
    hasil = word_tokenize(data)
    return hasil
    
# -------------7. main program-------------
hasilToken = tokenization(data)
hasilStem = stemmingWord(hasilToken)
hasilNoPuct = punctuationRemoval(hasilStem)
hasilStopWord = stopwordRemoval(hasilNoPuct)

print(hasilStopWord)