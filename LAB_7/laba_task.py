import requests
import json # common libraries
import flickrapi # using for the second part of the task, 2 variant 
from datetime import datetime #formatting unix format to basic

API_KEY_WEATHER = "19865cebf540d09c3aaceda97face9b7"
API_KEY_FLIKR = "d3fb683fb4f53f8603017b3ffd902b47"
API_SECRET_FLIKR = "ded70a9d6a921c7c"

# The fisrt part of the task
def get_weather(city_name): 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY_WEATHER}"

    response = requests.get(url)
    data = response.json()  

    return data["weather"][0]["description"], data["main"]["pressure"], data["main"]["humidity"]


if __name__ == '__main__':
    city_name = input('Type the name of city:')
    weather, pressure, humidity = get_weather(city_name)

    print(f' Weather forecast in {city_name}: \n Weather - {weather} \n Pressure - {pressure} hectopascal  \n Humidity - {humidity}%')

# The second part of the task

if __name__ == '__main__':
    flickr = flickrapi.FlickrAPI(API_KEY_FLIKR, API_SECRET_FLIKR, format='json') 
    sets   = flickr.photosets.getList(user_id='73509078@N00')
    parsed = json.loads(sets.decode('utf-8'))
    # with open("flikr_data.json", "w") as outfile:
    #     json.dump(parsed, outfile)

    count = 0
    while count < 7:
        photo_info = parsed["photosets"]["photoset"][count]
        photo_title, photo_des = photo_info["title"]["_content"], photo_info["description"]["_content"]
        photo_date = datetime.fromtimestamp(int(photo_info["date_create"])).strftime("%Y-%m-%d %H:%M:%S")
        print(f'{photo_title}{" "*(30-len(photo_title))}| {photo_des}{" "*(50-len(photo_des))}| {photo_date}')
        count += 1