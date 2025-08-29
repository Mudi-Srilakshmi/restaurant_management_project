from django.shortcuts import render

# New view for restaurant information page
def restaurant_info(request):
    # You can add static info here OR fetch from database later if needed
    context = {
        'restaurant_name': 'Spicy Delight',
        'history': 'Our restaurant was established in 2005 with the mission to bring authentic flavours to our customers.',
        'mission': 'To serve fresh, hygenic, and tasty food at affordable prices while ensuring great customer experience.'
    }
    return render(request, 'orders/restaurant_info.html', context)
    