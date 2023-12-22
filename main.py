import components.passengers.service as passenger
import components.pilots.service as pilot
import components.airplanes.service as airplane
import utils.json_service as json_service


def airport_database():
    db = json_service.get_database()
    while True:
        print('\nС какой категорией вы хотите работать?')
        print('\t1. Пассажиры')
        print('\t2. Самолеты')
        print('\t3. Пилоты')
        print('\t4. Выход')

        category_choice = input('Выберите категорию: ')
        if category_choice == '1':
            while True:
                print('\nДействия с пассажирами:')
                print('\t1. Добавить пассажира')
                print('\t2. Показать всех пассажиров')
                print('\t3. Показать пассажира по id')
                print('\t4. Обновить информацию о пассажире')
                print('\t5. Удалить пассажира')
                print('\t6. Вернуться к выбору категории')

                action_choice = input('Выберите действие: ')
                if action_choice == '1':
                    passenger.create_one()
                elif action_choice == '2':
                    print(passenger.get_all())
                elif action_choice == '3':
                    print(passenger.get_one_by_id())
                elif action_choice == '4':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(passenger.update_one_by_id(id))
                elif action_choice == '5':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(passenger.delete_one_by_id(id))
                elif action_choice == '6':
                    break
                else:
                    print('Некорректный ввод!')
        elif category_choice == '2':
            while True:
                print('\nДействия с самолетами:')
                print('\t1. Добавить самолет')
                print('\t2. Показать все самолеты')
                print('\t3. Показать самолет по id')
                print('\t4. Обновить информацию о самолете')
                print('\t5. Удалить самолет')
                print('\t6. Вернуться к выбору категории')

                action_choice = input('Выберите действие: ')
                if action_choice == '1':
                    airplane.create_one()
                elif action_choice == '2':
                    print(airplane.get_all())
                elif action_choice == '3':
                    print(airplane.get_one_by_id())
                elif action_choice == '4':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(airplane.update_one_by_id(id))
                elif action_choice == '5':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(airplane.delete_one_by_id(id))
                elif action_choice == '6':
                    break
                else:
                    print('Некорректный ввод!')

        elif category_choice == '3':
            while True:
                print('\nДействия с пилотами:')
                print('\t1. Добавить пилота')
                print('\t2. Показать всех пилотов')
                print('\t3. Показать пилота по id')
                print('\t4. Обновить информацию о пилоте')
                print('\t5. Удалить пилота')
                print('\t6. Вернуться к выбору категории')

                action_choice = input('Выберите действие: ')
                if action_choice == '1':
                    pilot.create_one()
                elif action_choice == '2':
                    print(pilot.get_all())
                elif action_choice == '3':
                    print(pilot.get_one_by_id())
                elif action_choice == '4':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(pilot.update_one_by_id(id))
                elif action_choice == '5':
                    while True:
                        id = int(input("Введите id: "))
                        try:
                            proverka = int(id)
                            break
                        except ValueError:
                            print("Ошибка ввода! Повторите попытку.")
                    print(pilot.delete_one_by_id(id))
                elif action_choice == '6':
                    break
                else:
                    print('Некорректный ввод!')

        elif category_choice == '4':
            break

        else:
            print('Некорректный ввод!')


airport_database()
