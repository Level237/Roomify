

def hotel_modal_context(request):
    show_hotel_form=False
    show_hotel_param=request.GET.get('r')
    
    if show_hotel_param == 'new-hotel' and request.user.is_authenticated:
        if hasattr(request.user,'role') and request.user.role.name == 'manager':
            show_hotel_form=True
    return {'show_hotel_form':show_hotel_form}
    
    