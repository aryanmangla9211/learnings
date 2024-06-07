import requests
import time

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

    if data:
        print("data retrived from the api")
        print(data)
    else:
        print('Failed to fetch data from API.')

if __name__ == '__main__':
    main()
