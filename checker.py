from tkinter import *
import re
from util.document_parser import Parser
from util.tree import Tree

class AutocompleteEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)        
        self.lb_up = False
        lsWords = Parser.parse("library/daftar-kata.txt")
        self.dictionary = Tree()
        self.dictionary.generateRef(lsWords)

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.suggestion()        
            if not self.lb_up:
                self.lb = Listbox()
                self.lb.place(x = self.winfo_x(), y = self.winfo_y() + self.winfo_height())
                self.lb_up = True
            
            self.lb.delete(0, END)
            if words :
                self.lb.insert(END,"True")
            else :
                self.lb.insert(END,"False")
        
    def suggestion(self):
        return self.dictionary.check(self.var.get())
        

if __name__ == '__main__':
    root = Tk()
    root.title('Simple Translator')
    root.geometry('200x200')

    entry = AutocompleteEntry(root)

    entry.pack(expand=YES, fill = X)

    root.mainloop()