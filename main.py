import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    #print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    #print('Активных пропусков:', len(Passcard.objects.filter(is_active=True)))
    print(Visit.objects.all())
