import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # CSVファイルを読み込む
    with open(csv_file_path, 'r', encoding='cp932') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        # JSONファイルに書き込む
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_data = json.dumps([row for row in csv_reader], indent=1, ensure_ascii=False)
            json_file.write(json_data)

def json_edit(json_file_path,json_file_path_new): #表記揺れ対応
    conversion_dict = {'現代の':'現国',
                       '言語文':'言文',
                       '論理国':'論国',
                       '古典':'古典',
                        '実数A':'実数A',
                        '実数B':'実数B',
                        '理数E':'理数E',
                        '数学Ⅰ':'数Ⅰ',
                        '数ⅠⅡ':'数Ⅰ',
                        '数学Ａ':'数A',
                        '数Ａ':'数A',
                        '理数Ⅱα':'理数Ⅱα',
                        '理数Ⅱβ':'理数Ⅱβ',
                        '理数Ⅱ':'理数Ⅱ',
                        '理数数':'理数Ⅰ',
                        '数学Ⅲ':'数Ⅲ',
                        '数学Ⅱ':'数Ⅱ',
                        '数学Ｂ':'数B',
                        '応数':'応数',
                        'EW':'EW',
                        'ｴｯｾｲ':'EW',
                        '論理':'論表',
                        '論表':'論表',
                        '英語コ':'EC',
                        'EC':'EC',
                        'CⅢ':'EC',
                        '総合英':'総英',
                        '日地':'日地',
                        '地歴':'地歴β',
                        '世政経':'世政経',
                        '歴史':'歴史',
                        '地理':'地理',
                        '世界史':'世史',
                        '物理基':'物基',
                        '生物基':'生基',
                        '化学基':'化基',
                        '理物生':'理物生',
                        '物生':'物生',
                        '理化':'理化',
                        '理数物':'理物',
                        '理数生':'理生',
                        '理数化':'理化',
                        '化':'化学',
                        '自然科':'自科',
                        '情報':'情報Ⅰ',
                        '体':'体',
                        '保健':'保',
                        '家庭基':'家',
                        '芸':'芸',
                        '理数探究':'理数探究',
                        '国際探究':'国際探究',
                        '総合':'総合',
                        '公共':'公共',
                        'ﾃﾞｲﾍ':'DDI',
                        'ＬＨＲ':'LHR'
    }
    with open(json_file_path) as f:
        old_f = json.load(f)

    for i in range(len(old_f)):
       for j in range(len(old_f[1]['null'])):
            for k in conversion_dict:
                if k in old_f[i]['null'][j]:
                    old_f[i]['null'][j] = ' '+conversion_dict[k]
                    break

    
    with open(json_file_path_new, 'w', encoding='utf-8') as json_file:
            json_data = json.dumps(old_f, indent=1,ensure_ascii=False)
            json_file.write(json_data)
                

if __name__ == '__main__':
    csv_file_path = 'クラス一覧（探究用）.csv'    # 入力となるCSVファイルのパス
    json_file_path = 'schedule_data.json' # 出力するJSONファイルのパス
    json_file_path_new = 'schedule_data_new.json'
    
    csv_to_json(csv_file_path, json_file_path)
    json_edit(json_file_path, json_file_path_new)
