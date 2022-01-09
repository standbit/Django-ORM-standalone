import os

import django
from django.db.models.fields import NullBooleanField
from django.utils.timezone import localtime
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


def get_duration(visit):
    now = localtime().replace(microsecond=0)
    entered_time = localtime(visit.entered_at)
    leaved_time = localtime(visit.leaved_at)
    if not visit.leaved_at:
        delta = now - entered_time
    else:
        delta = leaved_time - entered_time
    return delta


def is_visit_long(visit, minutes=60):
    visit_time_in_min = (int(get_duration(visit).total_seconds()))/60
    if visit_time_in_min > minutes:
        return True
    return False


def get_strange_visits(visits):
    strange_visits = []
    for visit in visits:
        if is_visit_long(visit, minutes=100):
            strange_visits.append(visit)
    return strange_visits


if __name__ == '__main__':
    # Программируем здесь
    #print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    #print('Активных пропусков:', len(Passcard.objects.filter(is_active=True)))
    all_visits = Visit.objects.all()
    unfinished_visits = []
    for visit in all_visits:
        if not visit.leaved_at:
            unfinished_visits.append(visit)
    now = localtime().replace(microsecond=0)
    for visit in unfinished_visits:
        entered_time = localtime(visit.entered_at)
        delta = now - entered_time
        seconds = int(delta.total_seconds())
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = (seconds % 3600) % 60
        # print(visit.passcard)
        # print('Зашел в хранилище, время по Москве:\n', entered_time, '\n')
        # print('Находится в хранилище:\n', f'{hours}:{minutes}:{secs}')
    all_cards = Passcard.objects.all()
    test_card = all_cards[7]
    test_visits = Visit.objects.filter(passcard=test_card)
    print("Визиты дольше 100 минут:", get_strange_visits(test_visits)) 
