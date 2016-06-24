from django.shortcuts import render
from django.db.models import Max, Min
from django.db.models import Q
from django.utils import timezone

from pimeteo.models import Mesure, Live


def today(request):
    # on calcule les dates de référence
    now = timezone.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)  # la date à minuit
    yesterday = now - timezone.timedelta(days=1)  # la date 24h avant

    # on récupère tous les enregistrements pour les dernières 24h
    data = Mesure.objects.filter(time__range=(yesterday, now))

    # données minis/maxis
    today_data = data.filter(time__range=(midnight, now))  # on limite la recherche depuis minuit ce jour
    min_data = today_data.aggregate(Min('temp'), Min('press'), Min('moist'), Min('dew'))  # selectionne tous les minis
    max_data = today_data.aggregate(Max('temp'), Max('press'), Max('moist'), Max('dew'))  # selectionne tous les maxis

    # données pour le graphique
    graph_data = data.order_by('time')

    # données pour le tableau
    table_data = data.filter(Q(time__minute=0) | Q(time__minute=30)).order_by('-time')

    # on récupère l'heure de la dernière prise de vue qui correspond
    # à l'heure du dernier enregistrement pour les graphes (toutes les 10min)
    pict_time = graph_data.last()

    # données pour la situation actuelle
    now_data = Live.objects.last()

    # on vérifie l'état des services de la station
    data_status = False if now_data.time < now.replace(second=0, microsecond=0) else True
    cam_status = False if (now_data.time - timezone.timedelta(minutes=10)) < pict_time.time else True

    # on transmet toutes les données à la vue concernée
    context = {'min_data': min_data, 'max_data': max_data, 'table_data': table_data, 'now_data': now_data,
               'graph_data': graph_data, 'midnight': midnight, 'pict_time': pict_time,
               'data_status': data_status, 'cam_status': cam_status}
    return render(request, 'pimeteo/today.html', context)


def week(request):
    now = timezone.now()  # la date maintenant
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)  # la date à minuit
    week_start = now - timezone.timedelta(days=7)
    week_data = Mesure.objects.filter(time__range=(week_start, now)).filter(time__minute=0).order_by('time')
    context = {'week_data': week_data, 'midnight': midnight}
    return render(request, 'pimeteo/week.html', context)


def about(request):
    return render(request, 'pimeteo/about.html', )
