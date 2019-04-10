from openpyxl import load_workbook
inSetLexicon = load_workbook('../../inset lexicon/InSet-Lexicon/inset.xlsx')
negatif = inSetLexicon['negatif']
positif = inSetLexicon['positif']

for i in range(2, 3611):
        if (positif.cell(row=i, column=1).value == 'ga'):
                print('ga: ', i)
        if (positif.cell(row=i, column=1).value == 'gak'):
                print('gak: ', i)
        if (positif.cell(row=i, column=1).value == 'nggak'):
                print('nggak: ', i)