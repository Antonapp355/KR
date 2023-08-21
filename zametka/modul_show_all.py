import json

def all():
    with open("note_books.json", "r", encoding='utf-8') as read_file:
        data = list(json.load(read_file))
        for i in range(len(data)):
            print(f'\nID : {str(data[i]["ID"])}'
                f'\nЗаголовок: {str(data[i]["Heading"])}'
                f'\nТело заметки: {str(data[i]["Body"])}'
                f'\nДата создания: {str(data[i]["Date/Time"])}')