from django.shortcuts import render
from django.http import HttpResponse
from.models import Restaurant

def restaurant_list(request):
    """
    This view responsible for fetching and displaying the list of restaurants from the database.
    """

    try:
        # Try to get all restaurant records from the database
        restaurants = Restaurant.objects.all()

        # Handle the case where no restaurants exist
        if not restaurants:
            return HttpResponse("No restaurants available at the moment.", status=404)

        # If successful, render them inside the 'restaurant_list.html' template
        return render(request, "restaurant_list.html", {"restaurants": restaurants})
    except Exception as e:
        # This block handles any other unexpected errors (e.g., DB connection issue)
        # str(e) will give the actual error message for debugging
        return HttpResponse(f"An unexpected error occured: {str(e)}", status=500)
        
