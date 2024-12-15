import os,json, datetime,re 
import pandas as pd


class Config_data():
    
    def __init__(self, dict_data) -> None:
        
        # 体重、血圧を管理するJson
        self.blood_pressure_info = os.path.join(os.getcwd(), f'blood_pressure_info.json')

        self.dt = dict_data.get('dt', '2024-01-01') 
        self.high_value = dict_data.get('high', 130) 
        self.low_value = dict_data.get('low', 80) 
        self.pulsation = dict_data.get('pulse', 75)
        self.weight_value = dict_data.get('weight', 60)
       
    def get_json_info(self):
        with open(self.blood_pressure_info, mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    
    def add_new_data(self):
        exist_data = self.get_json_info()
        new_data = {
            'date': self.dt,
            'high': self.high_value,
            'low': self.low_value,
            'pulse': self.pulsation,
            'weight': self.weight_value
        }

        # 既存のデータのdateフィールドを抽出してリストに格納
        existing_dates = [item['date'] for item in exist_data]

        # 新しいデータのdateフィールドが既存のdateフィールドリストに含まれていない場合のみ、追加
        if new_data['date'] not in existing_dates:
            exist_data.append(new_data)

        # 更新されたデータをJSONファイルに書き込み
        with open(self.blood_pressure_info, 'w', encoding='cp932') as json_file:
                json.dump(exist_data, json_file, indent=4)
        
if __name__ == '__main__':
    # 単体テスト
    # create_data()
    ins = Config_data({})
    print(ins.get_json_info())
