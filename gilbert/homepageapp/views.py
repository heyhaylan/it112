from django.shortcuts import render

# Create your views here.


def home(request):
    user_name = request.GET.get('user_name', None)
    return render(request, 'homepageapp/base.html', {'user_name': user_name})
