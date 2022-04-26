from django.db import models
from django.urls import reverse


ISTOCHNIKI_CHOICES = (
    ("vsaunah", "Vsaunah"),
    ('bannik', 'Bannik'),
    ('101sauna', '101sauna'),
    ('banya', 'Banya'),
    ('dvhab', 'Dvhab'),
    ('sauna_rest', 'Sauna_rest'),
    ('vsaunu', 'Vsaunu'),
    ('zoon', 'Zoon')
)

OLD_CITY_CHOICES = (
    ("Москва", "Москва"),
    ("Абакан", "Абакан"),
    ("Екатеринбург", "Екатеринбург"),
    ("Магадан", "Магадан"),
    ("Магнитогорск", "Магнитогорск"),
    ("Ижевск", "Ижевск"),
    ("Набережные Челны", "Набережные Челны"),
    ("Сочи", "Сочи"),
    ("Йошкар-Ола", "Йошкар-Ола"),
    ("Балашиха", "Балашиха"),
    ("Барнаул", "Барнаул"),
    ("Белгород", "Белгород"),
    ("Казань", "Казань"),
    ("Иваново", "Иваново"),
    ("Мурманск", "Мурманск"),
    ("Симферополь", "Симферополь"),
    ("Ставрополь", "Ставрополь"),
    ("Сургут", "Сургут"),
    ("Калуга", "Калуга"),
    ("Нижний Новгород", "Нижний Новгород"),
    ("Тверь", "Тверь"),
    ("Тамбов", "Тамбов"),
    ("Благовещенск", "Благовещенск"),
    ("Новокузнецк", "Новокузнецк"),
    ("Новосибирск", "Новосибирск"),
    ("Новороссийск", "Новороссийск"),
    ("Томск", "Томск"),
    ("Тольятти", "Тольятти"),
    ("Тюмень", "Тюмень"),
    ("Одесса", "Одесса"),
    ("Омск", "Омск"),
    ("Орск", "Орск"),
    ("Хабаровск", "Хабаровск"),
    ("Пенза", "Пенза"),
    ("Краснодар", "Краснодар"),
    ("Петрозаводск", "Петрозаводск"),
    ("Чебоксары", "Чебоксары"),
    ("Череповец", "Череповец"),
    ("Челябинск", "Челябинск"),
    ("Псков", "Псков"),
    ("Пятигорск", "Пятигорск"),
    ("Красноярск", "Красноярск"),
    ("Самара", "Самара"),
    ("Рыбинск", "Рыбинск"),
    ("Ярославль", "Ярославль"),
    ("Якутск", "Якутск"),
    ("Южно-Сахалинск", "Южно-Сахалинск"),
    ("Липецк", "Липецк"),
    ("Саратов", "Саратов"),
    ("Ростов-на-Дону", "Ростов-на-Дону"),
    ("Санкт-Петербург", "Санкт-Петербург"),
)


class OldInfo(models.Model):
    url_istochnik = models.TextField(max_length=100, null=True)
    name = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    city = models.CharField(max_length=50, choices=OLD_CITY_CHOICES, null=True)
    adress = models.TextField(max_length=200, null=True)
    mail = models.CharField(max_length=100, null=True)
    phone_numbers = models.CharField(max_length=50, null=True)
    istochnik = models.CharField(max_length=50, choices=ISTOCHNIKI_CHOICES, null=True)
    discription = models.TextField(null=True)
    time = models.CharField(max_length=20, null=True)
    photos = models.CharField(max_length=1000, null=True)
    usligi = models.TextField(null=True)
    vmestimost = models.TextField(null=True)
    price = models.TextField(max_length=200, null=True)
    types = models.TextField( null=True)
    cite = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.name}, {self.adress}'


class NewInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    url_istochnik = models.TextField(max_length=300, null=True)
    name = models.TextField(null=True)
    date = models.DateField(null=True)
    city = models.CharField(max_length=50, choices=OLD_CITY_CHOICES, null=True)
    adress = models.TextField(unique=True)
    mail = models.CharField(max_length=100, null=True)
    phone_numbers = models.CharField(max_length=50, null=True)
    discription = models.TextField(null=True)
    time = models.CharField(max_length=20, null=True)
    photos = models.CharField(max_length=1000, null=True)
    usligi = models.TextField(null=True)
    vmestimost = models.TextField(null=True)
    price = models.TextField(max_length=200, null=True)
    types = models.TextField(null=True)
    cite = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.city}, {self.name}, {self.adress}'


class VsaunahUrls(models.Model):
    hrefs = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.hrefs}'


class ZoonUrls(models.Model):
    hrefs = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.hrefs}'


class BannikUrls(models.Model):
    hrefs = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.hrefs}'
