# importing required modules
import sys 
from PyPDF2 import PdfReader

#check 3 arguments at least
if not len(sys.argv)==3:
    print("Need more arguments")
elif not sys.argv[1].endswith(".pdf"): #check bib file
    print("No bib file specified")
elif not sys.argv[2].endswith(".doc"): #check csv file
    print("No csv file specified")
else:
    # Migrating starts here....
    pdf_filename=sys.argv[1]
    doc_filename=sys.argv[2]

    # creating a pdf reader object 
    reader = PdfReader(pdf_filename) 

    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    # getting a specific page from the pdf file 
    page = reader.pages[0] 

    # extracting text from page 
    text = page.extract_text() 
    print(text) 