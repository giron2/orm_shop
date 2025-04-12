from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    year  = models.IntegerField()
    color  = models.CharField(max_length=50)
    mileage  = models.IntegerField()
    volume  = models.DecimalField(max_digits=10, decimal_places=2)
    body_type  = models.CharField(choices=BODY_TYPE_CHOICES)
    drive_unit  = models.CharField(choices=DRIVE_UNIT_CHOICES)
    gearbox  = models.CharField(choices=GEARBOX_CHOICES)
    fuel_type  = models.CharField(choices=FUEL_TYPE_CHOICES)
    price = models.IntegerField()
    image  = models.ImageField()

    def __str__(self):
        return f'{self.model}-{self.price}p.'


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    client  = models.OneToOneField(Client, on_delete=models.CASCADE)
    car  = models.OneToOneField(Car, on_delete=models.CASCADE)
    created_at  = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.client}({self.car})'