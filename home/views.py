# Import APIView class to create class-based views in Django REST Framework
from rest_framework.views import APIView

# Import Response class to send back JSON responses to clients
from rest_framework.response import Response

# Define a class-based view for the Menu API endpoint
class MenuView(APIView):
    # Handle GET requests to retrieve the menu
    def get(self, request):
        # Hardcoded list of menu items - each item is a dictionary with name, description, and price
        menu = [
            {
                "name": "Chicken Biryani",
                "description": "Aromatic basmati rice with tender chicken and spices.",
                "price": 250
            },
            {
                "name": "Paneer Butter Masala",
                "description": "Paneer cubes in creamy tomato gravy.",
                "price": 200
            },
            {
                "name": "Masala Dosa",
                "description": "Crispy dosa stuffed with spicy potato filling.",
                "price": 80
            }

        ]

        # Return the menu data as a JSON response to the client
        return Response(menu)

