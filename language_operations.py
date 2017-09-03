
# coding: utf-8

# ### Make a program that can
# #### 1. auto translate,
# #### 2. get the sentiment (polarity/subjectivity),
# #### 3. correct grammar,
# #### 4. detect a language,
# #### 5. count words and characters,
# #### 6. capitalize,
# #### 7. detect readability

# In[12]:

from textblob import TextBlob
from titlecase import titlecase
from functools import partial

import readability
from tkinter import *
import tkinter.scrolledtext as tkst


# In[15]:

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid(row=0)
        
        self.selectInfo = Label(frame, text="Select your program.")
        self.selectInfo.grid(row=1)
        
        self.selectProgram = Listbox(frame)
        self.selectProgram.grid(row=2)
             
        for item in ["Auto Translation", 
                     "Language Detection", 
                     "Sentiment Detection",
                     "Grammar Correction", 
                     "Word/character Counter",
                     "Readability Counter",
                     "Title Capitalization"]:
            self.selectProgram.insert(END, item)
            
        self.select_button = Button(frame, text="SELECT", command = lambda: self.select(frame))
        self.select_button.grid(row=3)
        
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=9, column=0, sticky=N+S+E+W)
        
    def select(self, frame):
        selection = self.selectProgram.curselection()
        value = self.selectProgram.get(selection[0])
        
        if value == "Auto Translation":
            
            self.languageInfo = Label(frame, text="Choose the language to translate into.")
            self.languageInfo.grid(row=1, column=1)
            
            self.languageSelection = Listbox(frame)
            self.languageSelection.grid(row=2, column=1)
            
            for item in ["af", "sq", "am", "ar", "hy", "az", "eu", "bn", "bs", "bg", "ca", "ceb", "zh-CN",
                         "zh-TW", "co", "hr", "cs", "da", "nl", "et", "fi", "fr", "gl", "ka", "de", "el",
                         "gu", "iw", "hi", "hu", "is", "id", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku",
                         "lv", "lt", "mk", "ms", "ml", "mt", "mr", "mn", "no", "ny", "ps", "fa", "pl", "pt",
                         "pa", "ro", "ru", "sr", "st", "sn", "sd", "si", "sk", "sl", "es", "sw", "sv", "tl",
                         "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "xh", "zu"]:
                self.languageSelection.insert(END, item)
                
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="TRANSLATE!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
            
        if value == "Language Detection":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="DETECT LANGUAGE!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
            
        if value == "Sentiment Detection":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="DETECT SENTIMENT!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
            
        if value == "Grammar Correction":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="CORRECT GRAMMAR!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
            
        if value == "Word/character Counter":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="COUNT WORDS AND CHARACTERS!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
            
        if value == "Readability Counter":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="GET READABILITY GRADES!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
        
        if value == "Title Capitalization":
            self.selectInfo.grid(row=1, columnspan=2)
            self.selectProgram.grid(row=2, columnspan=2)
            self.select_button.grid(row=3, columnspan=2)
            
            self.text = Label(frame, text="Enter your text below.")
            self.text.grid(row=5, columnspan=2)
            self.entryfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.entryfield.grid(row=6, columnspan=2)
            
            self.submit_button = Button(frame, text="CAPITALIZE INTO A TITLE!", fg="blue", command = lambda: self.submit(frame, value))
            self.submit_button.grid(row=7, columnspan=2, sticky=N+S+E+W)
            
            self.reset_button = Button(frame, text="RESET", fg="blue", command = lambda: self.reset(frame))
            self.reset_button.grid(row=9, column=1, sticky=N+S+E+W)
        
    def submit(self, frame, value):
        entry_text = self.entryfield.get('1.0', END)
        text = TextBlob(entry_text)
        
        if value == "Auto Translation":
            lang_selection = self.languageSelection.curselection()
            lang_value = self.languageSelection.get(lang_selection[0])         
            
            try:
                output = text.translate(to=lang_value)
            except:
                output = text
            
            self.resultfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Language Detection":
            try:
                output = text.detect_language()
                output = "Detected language: {}".format(output)
            except:
                output = "Language could not be detected. Try longer sentences."
                
            self.resultfield = tkst.ScrolledText(frame, height=1, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Sentiment Detection":
            try:
                sentiment = text.sentiment
                if sentiment.polarity < -0.7:
                    output = "POLARITY: Very negative."
                elif sentiment.polarity < -0.4:
                    output = "POLARITY: Negative."
                elif sentiment.polarity < -0.2:
                    output = "POLARITY: Somewhat negative."
                elif sentiment.polarity < 0.2:
                    output = "POLARITY: Neutral."
                elif sentiment.polarity < 0.4:
                    output = "POLARITY: Somewhat positive."
                elif sentiment.polarity < 0.7:
                    output = "POLARITY: Positive."
                else:
                    output = "POLARITY: Very positive."
                    
                if sentiment.subjectivity < 0.2:
                    output = output + "\n" + "SUBJECTIVITY: Very objective."
                elif sentiment.subjectivity < 0.4:
                    output = output + "\n" + "SUBJECTIVITY: Somewhat objective."
                elif sentiment.subjectivity < 0.6:
                    output = output + "\n" + "SUBJECTIVITY: Neutral."
                elif sentiment.subjectivity < 0.8:
                    output = output + "\n" + "SUBJECTIVITYY: Somewhat subjective."
                else:
                    output = output + "\n" + "SUBJECTIVITY: Very subjective."
                
            except:
                output = "Sentiment could not be detected. Try longer sentences."
            
            self.resultfield = tkst.ScrolledText(frame, height=2, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Grammar Correction":        
            try:
                output = text.correct()
            except:
                output = text
            
            self.resultfield = tkst.ScrolledText(frame, height=10, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Word/character Counter":
            try:
                output = "WORDS COUNT: {}".format(len(text.words))
                output = output + "\n" + "CHARACTERS COUNT: {}".format(len(text))
            except:
                output = "Words/characters could not be counted. Try longer sentences."
                
            self.resultfield = tkst.ScrolledText(frame, height=2, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Readability Counter":
            try:
                readability_grades = readability.getmeasures(text.words, lang='en', merge=True)
                output = "Due to how the scores are calculated, some scores might show abnormal numbers."
                output = output + "\n" + "Those are not related to the program itself." + "\n"
                output = output + "\n" + "Kincaid (normally 0-12): {}".format(readability_grades.get('Kincaid'))
                output = output + "\n" + "GunningFogIndex (6-17): {}".format(readability_grades.get('GunningFogIndex'))
                output = output + "\n" + "Coleman-Liau (1-12): {}".format(readability_grades.get('Coleman-Liau'))
                output = output + "\n" + "FleschReadingEase (1-100) : {}".format(readability_grades.get('FleschReadingEase'))
                output = output + "\n" + "SOMGIndex (5-18): {}".format(readability_grades.get('SMOGIndex')) + "\n"
                output = output + "\n" + "Normally, 7th-8th grade can capture more than 80% of the U.S."
            except:
                output = "Readability could not be detected. Try longer sentences."
                
            self.resultfield = tkst.ScrolledText(frame, height=11, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
        if value == "Title Capitalization":
            try:
                output = titlecase(entry_text)
            except:
                output = "Title capitalization cannot be done. Try longer sentences."
                
            self.resultfield = tkst.ScrolledText(frame, height=2, wrap=tk.WORD)
            self.resultfield.grid(row=8, columnspan=2)
            self.resultfield.insert('1.0', output)
            
    def reset(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()
            
        self.selectInfo = Label(frame, text="Select your program.")
        self.selectInfo.grid(row=1)

        self.selectProgram = Listbox(frame)
        self.selectProgram.grid(row=2)

        for item in ["Auto Translation", 
                     "Language Detection", 
                     "Sentiment Detection",
                     "Grammar Correction", 
                     "Word/character Counter",
                     "Readability Counter",
                     "Title Capitalization"]:
            self.selectProgram.insert(END, item)

        self.select_button = Button(frame, text="SELECT", command = lambda: self.select(frame))
        self.select_button.grid(row=3)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=9, column=0, sticky=N+S+E+W)
        
root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below


# In[ ]:



