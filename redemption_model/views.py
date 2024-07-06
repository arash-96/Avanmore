from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, JsonResponse

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

        result = float(facility_a) * float(contractual_rate)

        print(result)
        
        return JsonResponse({'result': result})
    else:
        return HttpResponse('Invalid request method.')
        

