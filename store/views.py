from django.shortcuts import render

# Create your views here.
app_name = 'store'


def home_view(request):
    context = {

    }
    return render(request, 'store/dashboard.html', context=context)
