from django.shortcuts import render
import requests
import bs4


def index(request):
    value = []
    if request.method == 'POST':
        form = request.POST['your_url']
        r = requests.get(form)
        scrape_value = bs4.BeautifulSoup(r.text, 'html.parser')
        for data in scrape_value.find_all('img'):
            src_value = data.get('src')
            print(src_value)
            value.append(src_value)
    return render(request, 'index.html', {'value': value})
