import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random
import qrcode

class InputData:
    def __init__(self, parent):
        self.root = parent.master
        self.font = parent.font

        self.entry_blood()


    def entry_blood(self):
        # フレーム
        self.label_frame = tk.LabelFrame(self.root, text='血圧データ入力', bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.label_frame.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")

        self.high_bld = ttk.Scale(self.label_frame, from_=0, to= 200, command=self.set_val_high, length=200)
        self.high_bld.grid(column=0,row=0,padx=10,pady=10)

        # ラベル
        self.label_high = tk.Label(self.label_frame, text="値: 0", font=self.font)
        self.label_high.grid(column=1, row=0, padx=10, pady=10)

    def set_val_high(self, val):
        # スライダーの値を更新
        self.label_high.config(text=f"値: {float(val):.0f}")


