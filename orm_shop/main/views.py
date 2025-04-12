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
		raise Http404('Car not found')


def sales_by_car(request, car_id):
	try:
		# получите авто и его продажи
		car = Car.objects.get(pk=car_id)
		id_client = Sale.objects.filter(car_id=car_id).values_list("client", flat=True).get()
		buyer = Client.objects.get(id=id_client)
		sales = [{ 'client': {
		'last_name': buyer.last_name,
		'name': buyer.name,
		'middle_name': buyer.middle_name,
		'phone_number': buyer.phone_number,
		},
		'created_at': Sale.objects.filter(car_id=car_id).values_list("created_at", flat=True).get()
		}]
		context = {'car': car, 'sales': sales}
		template_name = 'main/sales.html'
		  # передайте необходимый контекст
	except Car.DoesNotExist:
		raise Http404('Car not found')
	return render(request, template_name, context)
