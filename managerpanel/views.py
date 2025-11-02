from django.shortcuts import render

# Create your views here.


def dashboard_manager(request):
    show_hotel_form = request.GET.get('r')
    
    if show_hotel_form == 'new-hotel':
        show_hotel_form = True
    else:
        show_hotel_form = False
    return render(request,"manager/dashboard.html",{'show_hotel_form':show_hotel_form})
