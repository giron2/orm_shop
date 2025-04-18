from django.http import Http404
from django.shortcuts import render


from main.models import Car, Client, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    # получите список авто
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
	# получите авто, если же его нет, выбросьте ошибку 404
	try:
		car = Car.objects.get(pk=car_id)
		context = {'car': car}
		template_name = 'main/details.html'
		return render(request, template_name, context)  # передайте необходимый контекст
	except Car.DoesNotExist:
		raise Http404('Автомобиль не найден')


def sales_by_car(request, car_id):
	try:
		car = Car.objects.get(pk=car_id)
		sales = Sale.objects.filter(car_id=car_id)
		context = {'car': car, 'sales': sales}
		template_name = 'main/sales.html'
		  # передайте необходимый контекст
	except Car.DoesNotExist:
		raise Http404('Нет данных о продаже этого автомобиля :(')
	return render(request, template_name, context)
