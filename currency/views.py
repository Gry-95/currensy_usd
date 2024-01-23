import requests
import time
from django.http import JsonResponse

currency_history = []


def get_current_usd(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    global currency_history
    currency_history.append({
        'date': time.strftime('%Y-%m-%d'),
        'rate': data['rates']['RUB'],
        'time': time.strftime('%H:%M:%S')
    })

    currency_history = currency_history[-10:]

    time.sleep(10)

    return JsonResponse({
        'current_rate': data['rates']['RUB'],
        'history': currency_history
    })
