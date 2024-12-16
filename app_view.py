import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from data_config import Config_data

class InputData:
    def __init__(self, parent):
        self.root = parent.master
        self.font = parent.font

        self.entry_blood()


    def entry_blood(self):

        # フレーム
        self.label_frame = tk.LabelFrame(self.root, text='血圧データ入力', bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.label_frame.grid(column=1, row=0, padx=20, pady=10, sticky="nsew")

        row = 0

        # 収縮期
        self.high_bld = ttk.Scale(self.label_frame, from_=110, to= 180, value=140, command=self.set_val_high, length=140)
        self.high_bld.grid(column=0,row=row, padx=10,pady=10)

        # ラベル
        self.label_high = tk.Label(self.label_frame, text="収縮期血圧: 140", font=self.font)
        self.label_high.grid(column=1, row=row, padx=10, pady=10)

        row += 1
        # 拡張期血圧
        self.low_bld = ttk.Scale(self.label_frame, from_=70, to= 140, value=100, command=self.set_val_low, length=140)
        self.low_bld.grid(column=0,row=row,padx=10,pady=10)

        # ラベル
        self.label_low = tk.Label(self.label_frame, text="拡張期血圧: 100", font=self.font)
        self.label_low.grid(column=1, row=row, padx=10, pady=10)

        row += 1
        # 脈拍数
        self.pulse = ttk.Scale(self.label_frame, from_=60, to= 90, value=75, command=self.set_val_pulse, length=120)
        self.pulse.grid(column=0,row=row,padx=10,pady=10)

        # ラベル
        self.label_pulse = tk.Label(self.label_frame, text="脈拍数: 75", font=self.font)
        self.label_pulse.grid(column=1, row=row, padx=10, pady=10)

        row += 1

        # カレンダー
        self.dte = DateEntry(master=self.label_frame, font=self.font)
        self.dte.grid(column=0,row=row,padx=10,pady=10)

        # 登録
        self.regist_btn = tk.Button(self.label_frame, text='登録する', font=self.font, command=self.regist_data)
        self.regist_btn.grid(column=1, row=row, padx=50, pady=10)


    def set_val_high(self, val):
        # スライダーの値を更新
        self.label_high.config(text=f"収縮期血圧: {float(val):.0f}")

    def set_val_low(self, val):
        # スライダーの値を更新
        self.label_low.config(text=f"拡張期血圧: {float(val):.0f}")

    def set_val_pulse(self, val):
        # スライダーの値を更新
        self.label_pulse.config(text=f"脈拍数: {float(val):.0f}")

    def regist_data(self):
        # bld_high = int(self.label_high.cget('text').replace('収縮期血圧: ',''))
        # bld_low = int(self.label_low.cget('text').replace('拡張期血圧: ',''))
        # pulse = int(self.label_pulse.cget('text').replace('脈拍数: ',''))
        # print(f'high:{bld_high} low:{bld_low} pulse:{pulse}')
        # print(f'date:{self.dte.get_date()}')

        dict_data = {}
        dict_data['dt'] = self.dte.get_date().strftime("%Y-%m-%d")
        dict_data['high'] = int(self.label_high.cget('text').replace('収縮期血圧: ',''))
        dict_data['low'] = int(self.label_low.cget('text').replace('拡張期血圧: ',''))
        dict_data['pulse'] = int(self.label_pulse.cget('text').replace('脈拍数: ',''))
        ins = Config_data(dict_data)
        ins.add_new_data()
