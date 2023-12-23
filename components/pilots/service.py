import utils.json_service as json_service


def get_one_by_id():
    db = json_service.get_database()
    while True:
        id = input('Введите id:')
        try:
            proverka = int(id)
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")
    for elem in db["pilots"]:
        if elem["id"] == int(id):
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["pilots"]


def update_one_by_id(id):
    db = json_service.get_database()

    for elem in db["pilots"]:
        if elem["id"] == id:
            while True:
                name = input('Введите фамилию и имя пилота: ')
                if len(name.split()) > 0:
                    break
                else:
                    print('Введите корректный текст')
            while True:
                email = input('Введите email пилота: ')
                if len(email.split()) > 0:
                    break
                else:
                    print('Введите корректный текст')
            while True:
                phone = input('Введите номер телефона пилота: ')
                try:
                    phone = int(phone)
                    break
                except ValueError:
                    print("Ошибка ввода! Повторите попытку.")

            while True:
                airplanes_ids_input = input('Введите через запятую id самолетов, управляемых этим пилотом: ').split(',')
                try:
                    airplanes_id = [int(airplane_id.strip()) for airplane_id in airplanes_ids_input]
                    break
                except ValueError:
                    print("Ошибка ввода! Повторите попытку.")

            elem["name"] = name
            elem["info"]["email"] = email
            elem["info"]["phone"] = phone
            elem["airplanes_id"] = airplanes_id

            for airplane in db['airplanes']:
                if id in airplane['pilots_id']:
                    airplane['pilots_id'].remove(id)
            for airplane_id in airplanes_id:
                for airplane in db['airplanes']:
                    if airplane['id'] == airplane_id:
                        airplane['pilots_id'].append(id)

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["pilots"]):
        if elem["id"] == id:

            candidate = db["pilots"].pop(i)

            for j, elem in enumerate(db["pilots"]):
                elem["id"] = j + 1

            for airplane in db['airplanes']:
                if id in airplane['pilots_id']:
                    airplane['pilots_id'].remove(id)

            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one():
    db = json_service.get_database()

    last_pilot_id = get_all()[-1]["id"]
    while True:
        name = input('Введите фамилию и имя пилота: ')
        if len(name.split()) > 0:
            break
        else:
            print('Введите корректный текст')
    while True:
        email = input('Введите email пилота: ')
        if len(email.split()) > 0:
            break
        else:
            print('Введите корректный текст')
    while True:
        phone = input('Введите номер телефона пилота: ')
        try:
            phone = int(phone)
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")
    while True:
        airplanes_ids_input = input('Введите id самолета(-ов), к-рыми управляет пилот: ').split(',')
        try:
            airplanes_id = [int(airplane_id.strip()) for airplane_id in airplanes_ids_input]
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")
    pilot = {
        "id": last_pilot_id + 1,
        "name": name,
        "info": {"email": email, "phone": phone},
        "airplanes_id": airplanes_id
    }
    db["pilots"].append(pilot)

    for airplane_id in airplanes_id:
        for airplane in db['airplanes']:
            if airplane['id'] == airplane_id:
                airplane['pilots_id'].append(last_pilot_id+1)

    json_service.set_database(db)

    return pilot
