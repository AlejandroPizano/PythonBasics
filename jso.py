
import requests 

api_key="d209958d12c9138c7c5f4ed74063a4e7"

def weather(city):
    
    try:
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
        request=requests.get(url)
        json1= request.json()
        temp_min=json1.get("main").get("temp_min")
        temp_max=json1.get("main").get("temp_max")
        description=json1.get("weather")[0].get("description")
        print("Todays weather for "+city+" is "+ description +" the minimum tempeture will be :"+ str(temp_min)+" and the maximun temperature will be "+str(temp_max),sep=
        "  ",end="\nSee you buddy!")

    except:
        print("Couldn´t find the city: "+city)

city=input("What city do you want to check?")
weather(city)

#solo estoy probando