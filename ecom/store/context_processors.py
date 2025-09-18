from .models import Category

def categories(request):
	cats = Category.objects.all().order_by('name')
	return {'nav_categories': cats}


