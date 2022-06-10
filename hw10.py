import csv
import datetime











#задача 2
today = datetime.datetime.now().date()
one_day =  datetime.timedelta(days=1)
yesterday = today - one_day

class Mixin:

    @staticmethod
    def weater():
        with open('weather.csv', 'w') as csvf:
            fieldnames = ["date", "place", "degree", "wind speed"]
            write = csv.DictWriter(csvf, fieldnames=fieldnames)
            write.writeheader()
            write.writerow({"date": (today - one_day * 6), "place": "Minsk", "degree": 15, "wind speed": 8.5})
            write.writerow({"date": (today - one_day * 5), "place": "Minsk", "degree": 12, "wind speed": 5.6})
            write.writerow({"date": (today - one_day * 4), "place": "Minsk", "degree": 14, "wind speed": 7.2})
            write.writerow({"date": (today - one_day * 3), "place": "Minsk", "degree": 13, "wind speed": 6.9})
            write.writerow({"date": (today - one_day * 2), "place": "Minsk", "degree": 12, "wind speed": 6.9})
            write.writerow({"date": (today - one_day), "place": "Minsk", "degree": 13, "wind speed": 7.6})
            write.writerow({"date": today, "place": "Minsk", "degree": 17, "wind speed": 5.3})



    @staticmethod
    def mean():
        counter = 0
        val_temp = 0
        val_wind = 0

        with open('weather.csv', 'r') as csvf:
            read = csv.DictReader(csvf)
            for row in read:
                if "date" in row:
                    pass
                val_temp += int(row["degree"])
                val_wind += float(row["wind speed"])
                counter += 1
            mean_temp = round(val_temp / counter, 3)
            mean_wind = round(val_wind / counter, 3)
            print(f'Средняя температура за неделю {mean_temp} \n'
                  f'Средняя скорость ветра за неделю {mean_wind}')