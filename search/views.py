from django.shortcuts import render
from . import models

# Create your views here.

def search(request):

  if request.method == 'GET':
    query = request.GET.get('q', '')
    if query:
      # results = models.Dish.objects.filter(item__icontains=query)
        results = models.Dish.objects.filter(item__icontains=query).select_related('restaurant').order_by('price')[:5]

    else:
      return render(request, 'index.html')

    data = {
            'results': [
                {
                    'item': result.item,
                    'price': result.price,
                    'restaurant': result.restaurant.name
                }
                for result in results
            ]
        }
    # print(data)
  return render(request, 'index.html', context=data)