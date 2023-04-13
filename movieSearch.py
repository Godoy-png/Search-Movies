import requests
import json

def reque(title):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=yourKey' + title + '&type=movie')
        dict = json.loads(req.text)
        return dict
    except:
        print('Error')
        return None

def print_details(movie):
    print('Title:', movie['Title'])
    print('Year:', movie['Year'])
    print('Director:', movie['Director'])
    print('Actors:', movie['Actors'])
    print('Rating:', movie['imdbRating'])
    print('Awards:', movie['Awards'])
    print('Poster:', movie['Poster'])
    print('')

exi = False
while not exi:
    op = input('Type a movie name or EXIT to close: ')

    if op == 'EXIT':
        exi = True
        print('Leaving...')
    else:
        movie = reque(op)
        if movie['Response'] == 'False':
            print('Movie not found')
        else:
            print_details(movie)
            
