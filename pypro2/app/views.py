from django.shortcuts import render

# Create your views here.
from .models import user
def index(request):
	users_list=user.objects.all()
	context = {"users_list":users_list}
	return render(request, 'index.html', context=context)