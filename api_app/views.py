# api_app/views.py
from django.http import JsonResponse
import json
from .models import Person
from .decorators import require_api_password
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from openpyxl import load_workbook

@require_http_methods(["GET"])
@require_api_password
def get_persons(request):
    # Retrieve all Person records and convert to list of dictionaries
    persons = list(Person.objects.all().values())
    return JsonResponse(persons, safe=False)


@require_http_methods(["GET"])
def get_persons_FREE(request):
    # Retrieve all Person records and convert to list of dictionaries
    persons = list(Person.objects.all().values())
    return JsonResponse(persons, safe=False)


@csrf_exempt  # Exempt CSRF for testing purposes. In production, handle CSRF securely.
@require_http_methods(["POST"])
@require_api_password
def add_person_to_excel(request):
    try:
        # Parse the JSON payload from the request body
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        
        # Validate that both name and email are provided
        if not name or not email:
            return JsonResponse({"error": "Both 'name' and 'email' are required."}, status=400)
        
        # Define the path to your Excel file (adjust the path accordingly)
        file_path = r'C:\Users\Asus TUF\Desktop\Desktop\django_project\data_supply\persons.xlsx'
        
        # Open the Excel workbook and select the active worksheet
        wb = load_workbook(file_path)
        ws = wb.active  # Assumes your data is in the active worksheet
        
        # Append the new row with the provided name and email
        ws.append([name, email])
        
        # Save the workbook to persist the changes
        wb.save(file_path)
        
        return JsonResponse({"message": "Person added successfully."}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)