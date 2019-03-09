from openpyxl import load_workbook
dataset = load_workbook('../dataset_TA/AI_EDOM_ganjil_18_19.xlsx')
ai_sjn = dataset['AI-SJN']

def importExcelDataSet():
    hasil = []
    labelManual = []
    for i in range(2, 100):
        if (ai_sjn.cell(row=i, column=7).value == None):
            break
        else:
            hasil.append(ai_sjn.cell(row=i, column=7).value)
            labelManual.append(ai_sjn.cell(row=i, column=8).value)
    return hasil, labelManual

a, b = importExcelDataSet()

print(a)