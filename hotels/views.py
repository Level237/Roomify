
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hotels.models import Hotel
# Create your views here.

@login_required
def dashboard(request):
    try:
        hotel=Hotel.objects.get(owner=request.user)
    except Hotel.DoesNotExist:
        hotel=None
        
    context={
        "hotel":hotel,
        "tenant_schema":request.tenant.schema_name,
    }
    return render(request, 'hotels/dashboard.html',context)