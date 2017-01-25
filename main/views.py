from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def search(request):
	search_query = request.GET.get('squery')
	search_url = 'https://api.nal.usda.gov/ndb/search/?format=json&sort=n&max=100&offset=0&api_key=6P0TtTKUCWh2ZaJ6ahBG2HfCz5HUWlPpapkNZEyH&q={}'.format(search_query)
	search_results = requests.get(search_url)
	return render(request, 'search.html', {'search_query': search_query, 'search_results': search_results.json()})

def food_detail(request):
	nut_id = request.GET.get('ndbno')
	nut_url = 'https://api.nal.usda.gov/ndb/reports/?&type=b&format=json&api_key=6P0TtTKUCWh2ZaJ6ahBG2HfCz5HUWlPpapkNZEyH&ndbno={}'.format(nut_id)
	nut_results = requests.get(nut_url)
	data = nut_results.json()
	qty = data['report']['food']['nutrients'][0]['measures'][0]['qty']
	error_message = None
	try:
		amount = float(request.GET.get('amount', qty)) #helps not to see an empty text box
	except:
		error_message = "Please enter only a number"
		amount = qty
	return render(request, 'food_detail.html', {'nut_results': nut_results.json(), 'qty' : qty, 'amount' : amount, "error_message": error_message })


