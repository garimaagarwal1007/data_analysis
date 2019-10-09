import csv
from collections import defaultdict, Counter
import time

def school_Search(data, schools, cities, states, searched_query):
    matching = [data[key] for key, value in enumerate(schools) if searched_query.lower() in value]
    inverted_index = defaultdict(list)
    search_data = searched_query.lower().split()
    for index, item in enumerate(schools):
        for value in item.split(" "):
            if value not in inverted_index:
                inverted_index[value] = []
                inverted_index[value].append(index)
            else:
                inverted_index[value].append(index)

    for index, item in enumerate(cities):
        for value in item.split(" "):
            if value not in inverted_index:
                inverted_index[value] = []
                inverted_index[value].append(index)
            else:
                inverted_index[value].append(index)

    for index, item in enumerate(states):
        for value in item.split(" "):
            if value not in inverted_index:
                inverted_index[value] = []
                inverted_index[value].append(index)
            else:
                inverted_index[value].append(index)
    data_check = []
    min = 0
    # start_time = time.process_time()
    for item in search_data:
        if item in inverted_index:
            if min == 0:
                min = len(inverted_index[item])
            elif len(inverted_index[item]) < min:
                min = len(inverted_index[item])
            data_check.extend(inverted_index[item])

    data_check.sort()
    results = []
    i = len(search_data)
    while i > 0:
        temp_results = [item for item, count in Counter(data_check).items() if count == i]
        i -= 1
        if len(temp_results) > 3:
            results.extend(temp_results)
            break
        else:
            results.extend(temp_results)
    # end_time = time.process_time()
    # print(end_time-start_time)
    return matching, results[0:5]


if __name__ == "__main__":
    start_time = time.process_time()
    data = []
    included_cols = [3, 4, 5, 8]
    with open('school_data.csv', encoding="ISO-8859-1") as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        headers = next(data_reader, None)
        for row in data_reader:
            content = list(row[i] for i in included_cols)
            data.append(content)
    schools = [x[0].lower() for x in data]
    cities = set([x[1] for x in data])
    states = set([x[2] for x in data])
    result = school_Search(data, schools, states, cities, 'KUSKOKWIM')
    end_time = time.process_time()
    for value in result[0]:
        print(value)
    for value in result[1]:
        print(data[value])
    # print(end_time-start_time)