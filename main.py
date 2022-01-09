import os

import django
from django.db.models.fields import NullBooleanField


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
    print(unfinished_visits)
