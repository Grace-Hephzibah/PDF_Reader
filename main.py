import pyttsx3
import PyPDF2

# Book path input
path = input("Please Enter the Path of the book: \n")
book = open(path,'rb')

# Initialize the book
PDF_Reader = PyPDF2.PdfFileReader(book)
pages = PDF_Reader.numPages

# Initialize the speaker
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')

# Set your speed
speed = int(input("Set a speed value: "))
speaker.setProperty('rate', speed)

# Voice - no input
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id) # voices[1].id you can change between (0,1)

# Volume - Don't fiddle with this
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# #printing current volume level
speaker.setProperty('volume',1)    # setting up volume level  between 0 and 1

# Enter your page number here
page_number = int(input("Set your page number: "))

# Last page input
print("Enter -1 if you want the program to read till the end")
last_page = int(input("Set the last page: "))

if last_page == -1 :
    last_page = pages

# Running till the end
for i in range(page_number-1,last_page):
    page = PDF_Reader.getPage(i) # should be one less than the actual page number
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
