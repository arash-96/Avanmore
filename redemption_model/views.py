from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import calculate_total_interest

# Create your views here.
def total_interest_calculator(request):
    return render(request, 'interest-calculator.html')

def calculate_interest(request):
    if request.method == 'POST':        
        # Extract form data
        facility_a = request.POST.get('facilityInput')
        contractual_rate = request.POST.get('contractualInput')
        beginning_date = request.POST.get('beginningDate')
        end_date = request.POST.get('endDate')

        result = calculate_total_interest(facility_a, contractual_rate, beginning_date, end_date)

        #Return a JSON Response
        return JsonResponse({'result': round(result)})
    else:
        return HttpResponse('Invalid request method.')
        

