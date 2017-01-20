from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	return render(request, 'index.html', {'name': 'Ozan'})

def search(request):
	search_query = request.GET.get('squery')
	search_url = 'https://api.nal.usda.gov/ndb/search/?format=json&sort=n&max=100&offset=0&api_key=6P0TtTKUCWh2ZaJ6ahBG2HfCz5HUWlPpapkNZEyH&q={}'.format(search_query)
	search_results = requests.get(search_url)
	return render(request, 'search.html', {'search_query': search_query, 'search_results': search_results.json()})



