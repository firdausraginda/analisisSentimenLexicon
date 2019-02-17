# -------------komentar-------------
# urutan praproses mikir sendiri

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