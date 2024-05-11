# https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# importing required modules
import PyPDF2
from polly import polly

file_to_parse = input("Enter PDF file to read: ")
print("Opening file")
try:
    # creating a pdf file object
    pdfFileObj = open(file_to_parse, 'rb')
except:
    print("Something went wrong with .pdf file")
    quit()

print("Getting pages...")
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print("Number of pages: {}".format(len(pdfReader.pages)))

print("Extracting text...")
text_to_convert = ""
for page in pdfReader.pages:
    temp = page.extract_text()
    if len(temp) > 0:
        text_to_convert = text_to_convert + temp + " "

# closing the pdf file object
pdfFileObj.close()

if (len(text_to_convert) > 0):
    print("Converting to speech...")
    # extracting text from page
    polly(text_to_convert)
else:
    print("No text found")