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
    for elem in db["airplanes"]:
        if elem["id"] == int(id):
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()
    return db["airplanes"]


def update_one_by_id(id):
    db = json_service.get_database()

    for elem in db["airplanes"]:
        if elem["id"] == id:
            while True:
                model = input('Введите модель самолета: ')
                if len(model.split()) > 0:
                    break
                else:
                    print('Введите корректный текст')
            while True:
                year = input('Введите год выпуска: ')
                try:
                    year = int(year)
                    break
                except ValueError:
                    print("Ошибка ввода! Повторите попытку.")
            while True:
                company = input('Введите авиакомпанию, которой принадлежит самолет: ')
                if len(company.split()) > 0:
                    break
                else:
                    print('Введите корректный текст')
            while True:
                pilots_ids_input = input('Введите id пилотов, управляющих этим самолетом (через запятую): ').split(',')
                try:
                    pilots_id = [int(pilot_id.strip()) for pilot_id in pilots_ids_input]
                    break
                except ValueError:
                    print("Ошибка ввода! Повторите попытку.")

            elem["model"] = model
            elem["info"]["year"] = year
            elem["info"]["company"] = company
            elem["pilots_id"] = pilots_id

            for pilot in db['pilots']:
                if id in pilot['airplanes_id']:
                    pilot['airplanes_id'].remove(id)
            for pilot_id in pilots_id:
                for pilot in db['pilots']:
                    if pilot['id'] == pilot_id:
                        pilot['airplanes_id'].append(id)

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["airplanes"]):
        if elem["id"] == id:

            candidate = db["airplanes"].pop(i)

            for j, elem in enumerate(db["airplanes"]):
                elem["id"] = j + 1

            for pilot in db['pilots']:
                if id in pilot['airplanes_id']:
                    pilot['airplanes_id'].remove(id)
            for passenger in db['passengers']:
                if id in passenger['airplanes_id']:
                    passenger['airplanes_id'].remove(id)

            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one():
    db = json_service.get_database()

    last_airplane_id = get_all()[-1]["id"]

    while True:
        model = input('Введите модель самолета: ')
        if len(model.split()) > 0:
            break
        else:
            print('Введите корректный текст')

    while True:
        year = input('Введите год выпуска: ')
        try:
            year = int(year)
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")

    while True:
        company = input('Введите авиакомпанию, которой принадлежит самолет: ')
        if len(company.split()) > 0:
            break
        else:
            print('Введите корректный текст')

    while True:
        pilots_ids_input = input('Введите id пилотов, управляющих этим самолетом (через запятую): ').split(',')
        try:
            pilots_id = [int(pilot_id.strip()) for pilot_id in pilots_ids_input]
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")
    while True:
        passengers_ids_input = input('Введите id пассажиров этого самолета (через запятую): ').split(',')
        try:
            passengers_id = [int(passenger_id.strip()) for passenger_id in passengers_ids_input]
            break
        except ValueError:
            print("Ошибка ввода! Повторите попытку.")

    airplane = {
        "id": last_airplane_id + 1,
        "model": model,
        "info": {"year": year, "company": company},
        "passengers_id": passengers_id,
        "pilots_id": pilots_id
    }

    db["airplanes"].append(airplane)

    for pilot_id in pilots_id:
        for pilot in db['pilots']:
            if pilot['id'] == pilot_id:
                pilot['airplanes_id'].append(last_airplane_id+1)

    for passenger_id in passengers_id:
        for passenger in db['passengers']:
            if passenger['id'] == passenger_id:
                passenger['airplanes_id'].append(last_airplane_id+1)

    json_service.set_database(db)

    return airplane







