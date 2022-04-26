import os
import django
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bani.settings")
django.setup()
import re
from parse.models import NewInfo, OldInfo


def change_info():
    objects_new = NewInfo.objects.all()
    objects_old = OldInfo.objects.all()
    for i in objects_old:
        try:
            adress = i.adress
            city = i.city
            new = NewInfo.objects.get(adress=adress, city=city)
            if len(i.phone_numbers) > len(new.phone_numbers):
                new.objects.update(phone_numbers=i.phone_numbers)
                print('Zamena')
            elif len(i.discription) > len(new.discription):
                new.objects.update(discription=i.discription)
                print('Zamena')
        except Exception:
            try:
                NewInfo.objects.create(
                    adress=i.adress,
                    name=i.name,
                    city=i.city,
                    phone_numbers=i.phone_numbers,
                    url_istochnik=i.url_istochnik,
                    price=i.price,
                    types=i.types,
                    cite=i.cite,
                    vmestimost=i.vmestimost,
                    usligi=i.usligi,
                    photos=i.photos,
                    discription=i.discription,
                    date=i.date,
                    time=i.time,
                    mail=i.mail
                )
            except django.db.utils.IntegrityError:
                print('what')


if __name__ == '__main__':
    change_info()
