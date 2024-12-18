import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from data_config import Config_data
from matplotgraphics import MatGrapics

class Graph:
    def __init__(self, parent):
        self.root = parent.master
        self.font = parent.font
        self.create_gui()

    def create_gui(self):
        # フレーム
        self.label_frame = tk.LabelFrame(self.root, text='データ表示', bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.label_frame.grid(column=1, row=0, padx=20, pady=10, sticky="nsew")

        # 登録
        self.regist_btn = tk.Button(self.label_frame, text='グラフ表示', font=self.font, command=self.view_data)
        self.regist_btn.grid(column=0, row=0, padx=10, pady=10)

    def view_data(self):
        self.gr = MatGrapics()
        self.gr.create_blood()