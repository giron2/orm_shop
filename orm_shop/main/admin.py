from django.contrib import admin
from .models import Car, Client, Sale


admin.site.register(Car)
admin.site.register(Sale)
admin.site.register(Client)
# зарегистрируйте необходимые модели
