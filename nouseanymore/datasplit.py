import json

json_open = open("scheduler_data122.json","r",encoding="utf-8")
json_load = json.load(json_open)

classes = [" ", " ",
           "3-1","3-2","3-3","3-4","3理探","3国探",
           "2-1","2-2","2-3","2-4","2理探","2国探",
           "1-1","1-2","1-3","1-4","1-5","1-6"]

result = []
for i in range(20):
    result.append({"class":f"{classes[i]}"})

#曜日処理
days = ["月","火","水","木","金"]
a = []
for i in days:
    a.append(i)
    for j in range(5):
        a.append(" ")
result[0]['null'] = a

#時限処理
b = []
for i in range(5):
    for j in range(6):
        b.append(str(j+1))
result[1]["null"] = b

#ファイル分割処理
for i in range(2,20):
    c = []
    for j in range(30,60):
        c.append(json_load[i]["null"][j])
    result[i]["null"] = c

with open('scheduler_data129.json','w',encoding="utf-8") as f:
    json.dump(result,f,indent=2,ensure_ascii=False)
