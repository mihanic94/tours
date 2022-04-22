from random import randint

from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

from tours.data import title, subtitle, description, departures, tours


def main_view(request):

    random_numbers = []
    while len(random_numbers) < 6:
        number = randint(1, 16)
        if number in random_numbers:
            continue
        else:
            random_numbers.append(number)

    tours_dict = {}
    for number in random_numbers:
        tours_dict[number] = tours[number]

    context = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': tours_dict,
    }

    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure_code):
    try:
        departure = departures[departure_code]
    except KeyError:
        raise Http404

    prices = []
    nights = []

    tours_dict = {}
    for tour_id in tours:
        if departure_code == tours[tour_id]["departure"]:
            tours_dict[tour_id] = tours[tour_id]
            prices.append(tours[tour_id]['price'])
            nights.append(tours[tour_id]['nights'])

    context = {
        'title': title,
        'departure': departure,
        'tours': tours_dict,
        'min_price': min(prices),
        'max_price': max(prices),
        'min_nights': min(nights),
        'max_nights': max(nights),

    }

    return render(request, 'tours/departure.html', context=context)


def tour_view(request, tour_id):
    try:
        tour = tours[tour_id]
    except KeyError:
        raise Http404
    departure = departures[tour['departure']]
    stars = int(tour['stars']) * '★'
    return render(request, 'tours/tour.html', {'title': title, 'tour': tour, 'departure': departure, 'stars': stars})


def page_not_found(request, exception):
    return HttpResponseNotFound('По указанному адресу страницы не существует!')


def server_error(request):
    return HttpResponseServerError('Простите, извините...у нас на сервере поломка!')
