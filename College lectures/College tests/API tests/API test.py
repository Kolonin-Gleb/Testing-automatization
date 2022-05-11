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

################################################### GET ###################################################

# Тест Get запроса получения моего ключа +++
def get_key(email: str, passwd: str):
    headers = {'email': email, 'password': passwd}
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    result = res.text
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError
    return status, result

my_api_key = get_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga')
my_api_key = my_api_key[1]['key'] # Сохраняю только ключ из ответа


# Тест Get запроса получения списка моих питомцев +++
def get_pets(auth_key : str, filter: str):
    headers = {'auth_key': auth_key}
    params = {'filter': filter}

    res = requests.get('https://petfriends1.herokuapp.com/api/pets', headers=headers, params=params)
    status = res.status_code
    result = res.text
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError
    return status, result

my_pets = get_pets(auth_key=my_api_key, filter="my_pets")
print(my_pets)
#TODO: Почему-то возращает 1 животное

################################################### POST ###################################################

# Тест POST запроса для добавления питомца без фото +++
def post_create_pet_simple(auth_key: str, name: str, animal_type: str, age: int):
    headers = {'auth_key': auth_key}
    data = {'name': name, 'animal_type': animal_type, 'age': age}

    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    result = res.text
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError
    return status, result

# post_create_pet_simple(auth_key=my_api_key, name="Gogo", animal_type="Dog", age=5)


# Тест POST запроса для добавления питомца +++
def post_create_pet(name, animal_type, age, photo_name, auth_key):
    
    # Упаковка данных для отправки
    m = MultipartEncoder(
    fields={ 'name': name, 'animal_type': animal_type, 'age': age,
            'pet_photo': (photo_name, open(photo_name, 'rb'), 'text/plain')}
    )

    headers = {'auth_key': auth_key, 'Content-Type': m.content_type}

    res = requests.post('https://petfriends1.herokuapp.com/api/pets', headers=headers, data=m)
    status = res.status_code
    result = res.text
    try:
        result = res.json()
    except:
        json.decoder.JSONDecodeError
    return status, result


# post_create_pet("cute cat", "Cat", "2.5", "cat2.jpg", my_api_key)

################################################### PUT ###################################################

# Обновление информации о животном по его pet_id +++
def pet_add(key: str, name: str, animal_type: str, age: int, pet_id: str):
    headers = {'auth_key': key}
    data = {'name' : name, 'animal_type': animal_type, 'age': age}
    # $ - соединение строк
    res = requests.put('https://petfriends1.herokuapp.com/api/pets/' + pet_id, headers=headers, data=data) 
    status = res.status_code
    result = res.text
    try: 
        result = res.json() 
    except json.decoder.JSONDecodeError:
        result = res.text 
    return status, result

# pet_add(my_api_key, 'ugly cat', 'Cat', "3.5", '5d17309b-329e-4fbf-b438-4b766dbdf995')

################################################### DELETE ###################################################

