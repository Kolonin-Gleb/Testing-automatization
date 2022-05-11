import requests # Для составления HTTP-запросов в Python.
import json # Для работы с json форматом


# Тест Get запроса получения моего ключа
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

keykekw = get_key('koloninGS20@st.ithub.ru','RwAWCy2AKsxWTga')
keykekw = keykekw[1]['key'] # Сохраняю только ключ из ответа

#------------PUT------------ 
 


#--------------------DELETE-------------------- 
 
def pet_del(key: str, pet_id: str): 
    headers = {'auth_key': key} 
    res = requests.delete('https://petfriends1.herokuapp.com/api/pets/' + pet_id, headers=headers) 
    status = res.status_code 
    try: 
        result = res.json() 
    except json.decoder.JSONDecodeError:
        result = res.text 
    return status, result
 
print(pet_del(keykekw,"565699e9-e43f-4925-a7f2-99cb80010853"))