
# coding: utf-8

# # Assignment 4

# ##  Objective :To extract the keywords from the document shared in the link http://bit.ly/epo_keyword_extraction_document.

# **I am using following python libraries:**
# 
# * PyPDF2 (To convert simple, text-based PDF files into text readable by Python)
# * nltk (To clean and convert phrases into keywords)
# 

# In[1]:


# Importing the libraries
import PyPDF2 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


# In[2]:


# Read the file
pdfFile = open('JavaBasics-notes.pdf','rb')
# The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFile)
# to parse through all the pages
num_pages = pdfReader.numPages
count = 0
text = ""
# The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()


# In[3]:


# Run the following code if the pdf file is scanned or have images
'''
import textract
if text != "":
   text = text
# If the above returns as False, we run the OCR library textract to convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

'''


# In[4]:


text


# In[5]:


# The word_tokenize() function will break our text phrases into individual words
tokens = word_tokenize(text)
# we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',','/','.',"'",'`','©','-', ' ', '//', "''", '*/']
# We initialize the stopwords variable
stop_words = stopwords.words('english')
# We create a list comprehension which only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]


# In[6]:


keywords


# In[7]:


# Function to count the no. of keywords repeated
def word_count(str):
    counts = dict()
    words = str

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# In[8]:


key = word_count(keywords)


# In[9]:


key


# In[10]:


# Importing the keywords into csv file
import csv
w = csv.writer(open("output.csv", "w"))
for key, val in key.items():
    w.writerow([key, val])


# In[14]:


# Read the output file
import pandas as pd
Keywords = pd.read_csv('output.csv',  header = None)


# In[15]:


Keywords

