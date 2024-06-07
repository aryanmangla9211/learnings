import requests
import time
import redis
import json

def get_data():
    url = 'https://dummy.restapiexample.com/api/v1/employees'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            number_of_retries = 0
            sleep_time = 1
            while response.status_code != 200 and number_of_retries < 3:
                print('Error status code is not 200:', response.status_code)
                time.sleep(sleep_time)
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    return data
                number_of_retries += 1
                sleep_time += sleep_time
                
            return None
            
    except Exception as e:
        print('Error occured while retrieving the data:', e)
        return None

def main():
    data = get_data()
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    if data:
        print("data retrived from the api")
        print(data)
        r.set
    else:
        print('Failed to fetch data from API.')

    data = {
            "id": 1,
            "employee_name": "Tiger Nixon",
            "employee_salary": 320800,
            "employee_age": 61,
            "profile_image": ""
        }
    
    r.set("data", json.dumps(data))
    print(r.get("data"))

if __name__ == '__main__':
    main()
