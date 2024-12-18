import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import numpy as np
import datetime
from io import BytesIO
from PIL import Image, ImageTk

class BloodPressureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("血圧/体重管理")
        
        # Tkinter ウィジェット配置
        self.image_label = tk.Label(self.root)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        self.plot_button = ttk.Button(self.root, text="データをプロット", command=self.create_blood)
        self.plot_button.pack(pady=10)

    def get_json_data(self):
        # ダミーデータ（JSONのような構造）
        return {
            'date': ["2024-12-10", "2024-12-11", "2024-12-12", "2024-12-13", "2024-12-14"],
            'high': [140, 135, 130, 145, 138],
            'low': [85, 82, 80, 88, 84],
            'weight': [72.5, 73.0, 72.8, 72.6, 72.7],
            'pulse': [75, 78, 76, 80, 79]
        }

    def create_blood(self):
        data = self.get_json_data()

        blood_pressure_data_set1 = data['high']
        blood_pressure_data_set2 = data['low']
        weight_data = data['weight']
        pulse_data = data['pulse']
        dates = [date2num(datetime.datetime.strptime(date_string, "%Y-%m-%d").date()) for date_string in data['date']]

        # matplotlib Figure を作成
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        # 血圧プロット
        ax.plot_date(dates, blood_pressure_data_set1, marker='o', linestyle='--', label='最高血圧', color='crimson')
        ax.plot_date(dates, blood_pressure_data_set2, marker='o', linestyle='--', label='最低血圧', color='tomato')
        ax.plot_date(dates, pulse_data, marker='o', linestyle='--', label='心拍数', color='deeppink')

        for date, value in zip(dates, blood_pressure_data_set1):
            ax.annotate(str(value), (date, value), textcoords="offset points", xytext=(-10, 10), ha='center', color='crimson')

        for date, value in zip(dates, blood_pressure_data_set2):
            ax.annotate(str(value), (date, value), textcoords="offset points", xytext=(-10, 10), ha='center', color='tomato')

        for date, value in zip(dates, pulse_data):
            ax.annotate(str(value), (date, value), textcoords="offset points", xytext=(-10, 10), ha='center', color='deeppink')

        # 標準値ライン
        ax.axhline(y=135, color='crimson', linestyle='-', linewidth=1, alpha=0.5)
        ax.axhline(y=80, color='tomato', linestyle='-', linewidth=1, alpha=0.5)

        ax.legend(loc='upper left')
        ax.set_title('(血圧/体重)管理')
        ax.set_xlabel('日付')
        ax.set_ylabel('血圧(mmHg)')
        ax.set_ylim(60, 180)

        # 日付フォーマット
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator())
        fig.autofmt_xdate()

        # 右軸 (体重)
        ax2 = ax.twinx()
        ax2.plot_date(dates, weight_data, marker='o', linestyle='--', label='体重', color='g')
        for date, value in zip(dates, weight_data):
            ax2.annotate(str(value), (date, value), textcoords="offset points", xytext=(15, -10), ha='center')
        ax2.axhline(y=72, color='g', linestyle='-', linewidth=1, alpha=0.5)
        ax2.set_ylabel('体重(kg)', rotation=90, labelpad=15)
        ax2.set_ylim(71, 80)
        ax2.legend(loc='upper right')

        # matplotlib Figure を画像に変換
        buf = BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        img = Image.open(buf)
        photo = ImageTk.PhotoImage(img)

        # Tkinter Label に画像を設定
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 参照保持
        buf.close()

# Tkinter アプリ起動
if __name__ == "__main__":
    root = tk.Tk()
    app = BloodPressureApp(root)
    root.mainloop()
