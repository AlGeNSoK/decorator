from logger import logger

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

@logger
def get_name(doc_number):
    quantity = 0
    for document in documents:
        if document["number"] == doc_number:
            return document["name"]
    return 'Документ не найден'

    return result

@logger
def get_directory(doc_number):
    quantity = 0
    for shelves, numbers in directories.items():
        for number in numbers:
            if doc_number in number:
                return shelves
    return 'Полки с таким документом не найдено'

    return result

@logger
def add(document_type, number, name, shelf_number):
    documents.append({"type": document_type, "number": number, "name": name})
    quantity = 0
    for shelf, numbers in directories.items():
        if str(shelf_number) in shelf:
            numbers.append(number)
            quantity += 1

    if quantity == 0:
        directories.update([str(shelf_number), number])

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))