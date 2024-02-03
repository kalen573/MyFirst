# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:21:58 2024

@author: kalen
"""
import tkinter as tk
# ↓TOPページをインポート
from k_top import TopFrame
import locale
locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

# このクラスがベースのウィンドウ設定になる
class TestBaseWindow(tk.Tk):

    def __init__(self):

        super().__init__()
        self.iconfile = '.\img\gohan.ico'
        self.iconbitmap(default=self.iconfile)
        self.title("こんだて君")
        self.geometry("400x400")
        self.configure(bg="#ffebcd")

        self.top = TopFrame(self)
        # この記述が無いと配置がズレる
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.top.grid(row=0, column=0, sticky="nsew")
        
if __name__ == "__main__":

    app = TestBaseWindow()
    app.mainloop()