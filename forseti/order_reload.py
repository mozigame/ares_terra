import requests
import time


def req_order_reload():
    token = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjYyNzEwOTQsInVzZXJfbmFtZSI6IlBMQVRfeHF0ZXN0fGZlbGl4IiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI3NGM3MTNlYy02NGM2LTRiZmEtOGIwZi0xZDI1Zjc2ZDViZTYiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.FIbb4NaljUa6N3uxn2sNDVFqGzggGh64axm6unOLVxXciECuOKNwLL2XnEiniKlF7D2-EV7Rf-xiQE_eMnoMlJO8qAq5s99lfZ7us3Yu8N_5xUQfv6D43JmBZsmNH9PRzCrWhWJs_pYj2100ckFN380ROvfIUgjUI2rR7YnxRqxU4HyNp9YK4O1tfW4yDfi7_WGbU-dJUKDl1vi6UohQl0ObTvWNDRow4P3XNjK0a7D_sKd5hIDFlRUNfOeJ75Dm323ZkNC81cPArD1lnmVssxBMG8utXxBXfilAefwKOy6pp901Gvoqq53Jc0tHKbQ614Ij3GbMUIbTcTTOflwXjg'
    headers = {'Authorization': token}
    file = open('order_reload_data', 'r')
    lists = file.readlines()
    count = 0
    for i in lists:
        count += 1
        print('request : ' + i)
        result = requests.post(url=i.strip(), headers=headers, timeout=30)
        print('result : ' + result.text)
        time.sleep(0.05)
        print(count)


req_order_reload()
