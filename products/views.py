from django.shortcuts import render
from .models import Product 
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	#obj = Product.objects.all()
	#context = {
	#	"title": obj.title,
	#	"description": obj.description
	#}
	context = {
		"objects" : obj
	}

	return render(request, "product/detail.html", context)

