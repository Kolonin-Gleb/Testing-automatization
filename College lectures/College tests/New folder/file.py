# Сайт с которым буду взаимодействовать:
# https://petfriends1.herokuapp.com/all_pets
# Для взаимодействия с сайтом буду использовать их API:
# https://petfriends1.herokuapp.com/apidocs/#/

# Задача - написать код функций, для тестирования работы этого API
# Всех методов, что есть в документации

''' https://swagger.io/ - сайт, на котором хорошо писать свою документацию '''

import requests
import json

# Тест Get запроса получения моего ключа
def get_api_key(email: str, passwd: str):
    headers = {'email': email, 'password': passwd}
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

my_api_key = get_api_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga')
my_api_key = my_api_key[1]['key'] # Сохраняю только ключ из ответа

# Тест Get запроса получения списка моих питомцев
def get_pets(auth_key : str, filter: str):
    headers = {'auth_key': auth_key}
    params = {'filter': filter}

    res = requests.get('https://petfriends1.herokuapp.com/api/pets', headers=headers, params=params)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

my_pets = get_pets(auth_key=my_api_key, filter="my_pets")
# print(my_pets)

# Тест POST запроса для дообавления питомца
def post_pet(auth_key: str, name: str, animal_type: str, age: int):
    headers = {'auth_key': auth_key} # +
    data = {'name': name, 'animal_type': animal_type, 'age': age} # +

    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

post_pet(auth_key=my_api_key, name="Gogo", animal_type="Dog", age=5)
# https://toolbelt.readthedocs.io/en/latest/user.html - Полезная ссылка для отправки фотографии. МОЖНО БУДЕТ РАЗОБРАТЬСЯ
# Результат проверю на сайте


# Тест POST запроса для дообавления питомца
