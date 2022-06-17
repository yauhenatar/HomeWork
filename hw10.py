import csv
import datetime
import zipfile

#задача 1

class Filework:

    @staticmethod
    def add_new_csv_file():
        if 'new csv file.csv':
            with open('new csv file.csv', 'a') as csvfile:
                fieldnames = ["name", "surname", "age"]
                write = csv.DictWriter(csvfile, fieldnames=fieldnames)
                write.writeheader()
                name = input('Введите имя: ')
                surname = input('Введите фамилию: ')
                age = input('Введите возраст: ')
                write.writerow(map(f'"name": {name}, "surname": {surname}, "age": {age}'))
        with open('new csv file.csv', 'w') as csvfile:
            fieldnames = ["name", "surname", "age"]
            write = csv.DictWriter(csvfile, fieldnames=fieldnames)
            write.writeheader()
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            age = input('Введите возраст: ')
            write.writerow(map(f'"name": {name}, "surname": {surname}, "age": {age}'))


    @staticmethod
    def get_report():
        counter12 = 0
        counter18 = 0
        counter25 = 0
        counter40 = 0
        counterelse = 0
        with open('new csv file.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['age'] <= 12:
                    counter12 += 1
                elif 12 < row['age'] <= 18:
                    counter18 += 1
                elif 18 < row['age'] <= 25:
                    counter25 += 1
                elif 25 < row['age'] <= 40:
                    counter40 += 1
                else:
                    counterelse += 1
        with open('report file.txt', 'w') as txtf:
            txtf.write(f'Количество записей в возрастной группе до 12 лет: {counter12}')
            txtf.write(f'Количество записей в возрастной группе до 18 лет: {counter18}')
            txtf.write(f'Количество записей в возрастной группе до 25 лет: {counter25}')
            txtf.write(f'Количество записей в возрастной группе до 40 лет: {counter40}')
            txtf.write(f'Количество записей в возрастной группе более 40 лет: {counterelse}')


#задача 2

today = datetime.datetime.now().date()
one_day =  datetime.timedelta(days=1)
yesterday = today - one_day

class Filework2:

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


#задача 3



#задача 4

class Filework4:

    @staticmethod
    def func():
        date = datetime.date.today().strftime('%d.%m.%Y')
        with open('newtxt.txt', 'w') as txtfile:
            txtfile.write(date)

        newzip = zipfile.ZipFile(f'{date}.zip', 'w')
        newzip.write('newtxt.txt')
        newzip.close()