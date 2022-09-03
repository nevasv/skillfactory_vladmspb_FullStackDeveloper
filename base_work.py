data_base = {
1 : [
{
    "surname" : "Петров",
    "work" : "работа на станке",
    "time_work" : "8",
    "price_of_work_hours" : "30",
},
{
    "surname" : "Петров",
    "work" : "тех. обслуживание",
    "time_work" : "8",
    "price_of_work_hours" : "25",
},
{
    "surname" : "Иванов",
    "work" : "Обучение",
    "time_work" : "4",
    "price_of_work_hours" : "20",
},
{
    "surname" : "Сидоров",
    "work" : "работа на станке",
    "time_work" : "8",
    "price_of_work_hours" : "25",
},
],
2 : [
{
    "surname" : "Петров",
    "work" : "работа на станке",
    "time_work" : "8",
    "price_of_work_hours" : "30",
},
{
    "surname" : "Петров",
    "work" : "тех. обслуживание",
    "time_work" : "8",
    "price_of_work_hours" : "25",
},
{
    "surname" : "Иванов",
    "work" : "Обучение",
    "time_work" : "4",
    "price_of_work_hours" : "20",
},
{
    "surname" : "Сидоров",
    "work" : "работа на станке",
    "time_work" : "8",
    "price_of_work_hours" : "25",
},
]
}
import  json
#print(json.dumps(data_base, indent=2))
def save_data (data_base):
    with open("data_base.json", "w") as f:
        json.dump(data_base,f,indent=2)
def load_data ():
    with open("data_base.json") as f:
        data = json.load(f)
        return data
#save_data(data_base)
#print(load_data())
def show_time_work(surname, time_work, width = 50):
    fill = "x"
    empty = "_"
    bars = round(time_work * width)
    progress = fill * bars + empty * (width - bars)
    print(f"{surname:25} - {round(time_work * 100)} % | {progress}")
show_time_work("Петров", 0.6)


