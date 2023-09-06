from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Michelle Angelica Santoso',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)