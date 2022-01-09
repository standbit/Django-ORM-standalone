import os

import django
from django.db.models.fields import NullBooleanField
from django.utils.timezone import localtime
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


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
        a = datetime.timedelta(hours, minutes, secs)
        print('Зашел в хранилище, время по Москве:\n', entered_time, '\n')
        print('Находится в хранилище:\n', f'{hours}:{minutes}:{secs}')
