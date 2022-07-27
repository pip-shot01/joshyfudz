from . models import Product

def readcart(request):
    cart = Product.objects.filter()
    
    cartcount = 0
    for count in cart:
        cartcount += count.max_quantity
        context = {
            'cartcount':cartcount,
        }
        return context