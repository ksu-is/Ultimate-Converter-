#for both repository and CalGUI
import tkinter as tk
from tkinter import filedialog
import os
from pikepdf import Pdf



#PDF Merger 
class DragDropListbox(tk.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = tk.SINGLE
        tk.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i


class pdfMergerApp():
    def __init__(self):

        self.pdfFolder = ""

        self.root = tk.Tk()
        self.root.title("PDF Merger")

        self.folderSelectButton = tk.Button(self.root, text="Choose a folder", command=self.folderSelect, height=4)
        self.folderSelectButton.grid(row=0, column=0, sticky="WE")

        self.pdfListbox = DragDropListbox(self.root, width=60, font=('Arial', 15))
        self.pdfListbox.grid(row=1, column=0, columnspan=2)

        self.pdfMergeButton = tk.Button(self.root, text="Merge into PDF", command=self.pdfMergeFunction, height=4)
        self.pdfMergeButton.grid(row=0, column=1, sticky="WE")

        self.root.mainloop()

    def folderSelect(self):
        self.pdfFolder = filedialog.askdirectory()

        myFiles = [fileName for fileName in os.listdir(self.pdfFolder) if os.path.splitext(fileName)[1] == '.pdf']

        itemNumber = self.pdfListbox.size()
        self.pdfListbox.delete(0, itemNumber)
        self.pdfListbox.insert('end', *myFiles)

        newItemNumber = len(myFiles)
        if newItemNumber <= 20:
            self.pdfListbox.config(height=newItemNumber)
        else:
            self.pdfListbox.config(height=20)

        print(f"Listbox updated with pdf files in folder {self.pdfFolder}")


    def pdfMergeFunction(self):
        if self.pdfFolder == "":
            itemNumber = self.pdfListbox.size()
            self.pdfListbox.delete(0, itemNumber)
            self.pdfListbox.insert('end', 'You need to choose a folder first!')
            return

        itemAmount = self.pdfListbox.size()
        fileList = self.pdfListbox.get(0, itemAmount - 1)

        fileList = list(fileList)
        files = [self.pdfFolder + "/" + fileName for fileName in fileList]

        pdf = Pdf.new()

        for file in files:
            src = Pdf.open(file)
            pdf.pages.extend(src.pages)

        try:
            os.remove(self.pdfFolder + "/merged/OUTPUT.pdf")
        except:
            pass

        try:
            os.makedirs(self.pdfFolder + '/merged')
        except:
            pass

        pdf.save(self.pdfFolder + '/merged/OUTPUT.pdf')

        print('Success!')

        itemNumber = self.pdfListbox.size()
        self.pdfListbox.delete(0, itemNumber)
        self.pdfListbox.insert('end', 'Merge Successful!')
        self.pdfFolder = ""

pdfMergerApp()



##GUI Creation##

class Calculator(Frame):
    """
    An example of a calculator app developed using the 
    Tkinter GUI.
    """

    def merge_pdf():
        pdfMergerApp()
        
    def  heic_to_jpg():
         #pending on working code
   
    def jpg_to_PDF():
         #pending on working code

    def bind_buttons(self, master):
        """
        Binds keys to their appropriate input
        :param master: root.Tk()
        :return: None
        """
        master.bind("3", lambda event, char="3", btn=self.three_bttn: self.add_chr(char, btn))
        master.bind("2", lambda event, char="2", btn=self.two_bttn: self.add_chr(char, btn))
        master.bind("1", lambda event, char="1", btn=self.one_bttn: self.add_chr(char, btn))
        
    
    def create_widgets(self):
        """
        Creates the widgets to be used in the grid.
        :return: None
        """
        self.one_bttn = Button(self, text="1", width=9, height=3, command=lambda: self.add_chr(1))
        self.one_bttn.grid(row=3, column=0)

        self.two_bttn = Button(self, text="2", width=9, height=3, command=lambda: self.add_chr(2))
        self.two_bttn.grid(row=3, column=1)

        self.three_bttn = Button(self, text="3", width=9, height=3, command=lambda: self.add_chr(3))
        self.three_bttn.grid(row=3, column=2)

       

root = Tk()
root.title("Final Project - Daniel Medina")
root.mainloop()
