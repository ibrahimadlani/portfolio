"""Views for the API."""
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def index(request):
    """Index view."""
    print(request)
    return JsonResponse({"message": "Hello, world!"})
