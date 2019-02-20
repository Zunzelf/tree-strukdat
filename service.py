from tkinter import *
import re
from util import kamus

class AutocompleteEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)        
        self.lb_up = False
        self.dictionary = kamus.Reader("kamus-raw.csv")

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.suggestion()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.place(x = self.winfo_x(), y = self.winfo_y() + self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def suggestion(self):
        return [self.dictionary.translate(self.var.get(), True)]
        

if __name__ == '__main__':
    root = Tk()
    root.title('Simple Translator')
    root.geometry('200x200')

    entry = AutocompleteEntry(root)

    entry.pack(expand=YES, fill = X)

    root.mainloop()