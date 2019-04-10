import glob
import os
import spacy

# Writing to an excel sheet
import xlwt 
from xlwt import Workbook 
# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
# Specifying style 
style = xlwt.easyxf('font: bold 1') 

sheet1.write(0, 0, 'Filename',style)
sheet1.write(0, 1, 'People',style)
sheet1.write(0, 2, 'Place',style)
sheet1.write(0, 3, 'Organization',style)

#Variables for iterating over xls sheet cells
row = 0
col = 0

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")


path = 'Media-Files-Test2/'
tem = ""
#opening text files
for filename in glob.glob(os.path.join(path, '*.txt')):
    #print(filename[18:36])
    
    tem = filename
    
    f = open(tem, "r")
    text = f.read()

    doc = nlp(text[13:])

    personBox = ''
    gpeBox = '' #general PLACE entity
    orgBox = '' #organization box

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        if(entity.label_ == 'PERSON'):
            personBox += (entity.text)
            personBox += ', '
        if(entity.label_ == 'GPE'):
            gpeBox += (entity.text)
            gpeBox += ', '
        if(entity.label_ == 'ORG'):
            orgBox += (entity.text)
            orgBox += ', '
        #print(entity.text, entity.label_)

    row += 1
    col = 0
    sheet1.write(row, col, tem[18:])
    sheet1.write(row, col+1, personBox)
    sheet1.write(row, col+2, gpeBox)
    sheet1.write(row, col+3, orgBox)
wb.save('NERsorted.xls') 
