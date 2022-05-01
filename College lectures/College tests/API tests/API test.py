# Задача - написать код функций, для тестирования работы этого API
# Всех методов, что есть в документации

# Сайт с которым буду взаимодействовать:
# https://petfriends1.herokuapp.com/all_pets
# Для взаимодействия с сайтом буду использовать их API:
# https://petfriends1.herokuapp.com/apidocs/#/
# https://toolbelt.readthedocs.io/en/latest/user.html - Как отправлять фотографии.

''' https://swagger.io/ - сайт, на котором хорошо писать свою документацию для API '''

import requests # Для составления HTTP-запросов в Python.
import json # Для работы с json форматом
from requests_toolbelt import MultipartEncoder # Для передачи изображения


# Тест Get запроса получения моего ключа
def get_key(email: str, passwd: str):
    headers = {'email': email, 'password': passwd}
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

my_api_key = get_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga')
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

# my_pets = get_pets(auth_key=my_api_key, filter="my_pets")
# print(my_pets)


# Тест POST запроса для добавления питомца без фото
def post_create_pet_simple(auth_key: str, name: str, animal_type: str, age: int):
    headers = {'auth_key': auth_key} # +
    data = {'name': name, 'animal_type': animal_type, 'age': age} # +

    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

# post_create_pet_simple(auth_key=my_api_key, name="Gogo", animal_type="Dog", age=5)


# Тест POST запроса для добавления питомца
def post_create_pet(data):
    headers = { 'Content-Type': data.content_type}

    res = requests.post('https://petfriends1.herokuapp.com/api/pets', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

# Сбор данных для отправки
m_data = MultipartEncoder(
    fields={'auth_key': my_api_key, 'name': "cute cat", 'animal_type': 'Cat', 'age': "2.52",
            'pet_photo ': ('cat2.jpg', open('cat2.jpg', 'rb'), 'text/plain')}
    )

# post_create_pet(data=m_data) #TODO: Не работает отправка фото


# Тест POST запроса на добавление фотографии
def post_set_photo(auth_key: str, m_data):
    headers = {'auth_key': auth_key, 'Content-Type': m_data.content_type}
    pet_id = 1

    res = requests.post(f'https://petfriends1.herokuapp.com/api/pets/set_photo/{pet_id}', headers=headers, data=m_data)
    status = res.status_code
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError: result = res.text
    return status, result

# Сбор данных для отправки
m_data = MultipartEncoder(
    fields={'pet_photo ': ('Octopus.jpg', open('Octopus.jpg', 'rb'), 'text/plain')}
    )

post_set_photo(auth_key=my_api_key, m_data=m_data)

