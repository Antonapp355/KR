import json

def next_iD():
    list_numbers = []
    with open("note_books.json", "r", encoding='utf-8') as read_file:
        data = list(json.load(read_file))
        for i in range(len(data)):
            list_numbers.append(data[i]["ID"])
            list_numbers.sort()
            list_numbers.reverse()
        return int(list_numbers[0]+1)