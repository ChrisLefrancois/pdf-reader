import tkinter
from tkinter import *
from tkinter import filedialog
import os
import pyttsx3
import PyPDF2

path = ""

def find_pdf():
    file = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title= "Select a PDF File")

    if file:
        file_name = os.path.basename(file)
        file_label = Label(window, text=f"PDF {file_name}", font=("Arial", 10, "bold"))
        file_label.place(x=170, y=100)
        file_label.config(fg="white", bg="black",highlightthickness=0)

        pdf = open(file, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf)

        engine = pyttsx3.init()

        for page_num in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page_num].extract_text()
            engine.say(text)
            engine.runAndWait()



window = tkinter.Tk()
window.geometry("600x400")
window.config(bg="black")

search_button = Button(window, text="Search Pdf to Read", command=find_pdf, bg="grey", font=("arial", 24))
search_button.grid(row=2, column=1, padx=100, pady=200)


window.mainloop()