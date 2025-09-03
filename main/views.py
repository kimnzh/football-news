from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406399485',
        'name' : 'Muhamad Hakim Nizami',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)