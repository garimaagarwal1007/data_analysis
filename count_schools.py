import csv
import operator
from itertools import groupby


def school_by_state(data):
    print("schools by state : ")
    for key, items in groupby(data, operator.itemgetter(2)):
        count = 0
        for subitem in items:
            count += 1
        print(key + ": " + str(count))


def school_by_metrolocale(data):
    print("schools by metro centric locale : ")
    for key, items in groupby(data, operator.itemgetter(3)):
        count = 0
        for subitem in items:
            count += 1
        print(key + ": " + str(count))


def school_by_city(data):
    city_count = 0
    max = 0
    city = None
    for key, items in groupby(data, operator.itemgetter(1)):
        count = 0
        for subitem in items:
            count += 1
        if count > max:
            max = count
            city = key
        city_count += 1
    print("the city with most schools in it is : " + city + " with " + str(max) + " schools")
    print("no of unique cities with atleast one school are : " + str(city_count))


if __name__ == "__main__":
    data = []
    included_cols = [3, 4, 5, 8]
    with open('school_data.csv', encoding="ISO-8859-1") as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        headers = next(data_reader, None)
        for row in data_reader:
            content = list(row[i] for i in included_cols)
            data.append(content)

    print("total schools:" + str(len(data)))
    school_by_state(data)
    school_by_metrolocale(data)
    school_by_city(data)
