import requests
import googlemaps
import geocoder
from urllib.parse import urlencode
from datetime import datetime
api_key = "AIzaSyCuHDX4fYSfrvMNIngrRfXMXmQkMNAQcSM"
gmaps = googlemaps.Client(key=api_key)

def wiki_response(subject):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
 
    response = requests.get(url, params=params)
    data = response.json()
    page = next(iter(data['query']['pages'].values()))
    text = str(page['extract'][:150]).replace('\n',"") + "..."
    if text == "...":
        text = "No information found. Try capitalizing letters or checking your spelling"
    return text

def get_latlng():
    g = geocoder.ip('me').latlng
    latlng = " ".join([str(elem) for elem in g]) 
    return latlng

def get_address():
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {"latlng": get_latlng() , "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    cursor = requests.get(url)
    data = cursor.json()
    return data["results"][0]["formatted_address"]

def get_directions(destination):
    now = datetime.now()
    directions_result = ""
    try:
        directions_result = gmaps.directions(get_address(),destination,mode="driving", departure_time=now)
    except:
        return "no suitable directions found"
    #this is hacky but it works. 
    i = 0;  
    purge = ['<b>','</b>','<wbr/>','<div style="font-size:0.9em">','</div>','<br>']
    results = ""
    try:
        while(True):
            words = directions_result[0]["legs"][0]["steps"][i]['html_instructions']
            for item in purge:
                words = words.replace(item,"")
            results += words + "\n"
            i += 1
    except:  
        results += "Navigation Complete!"
    return results
        
def check_if_directions(query):
    str_approved = ["directions", "to", "for"]
    i = 0
    for word in str_approved:
        if word in query:
            i += 1
            print(word)
    print(i)
    if i > 1: return True;
    else: return False;

check_if_directions("directions to home")
