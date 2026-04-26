from django.shortcuts import render
from .models import Product, Review
from django.shortcuts import render, get_object_or_404, redirect

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'core/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        if author and text and rating:
            Review.objects.create(
                product=product,
                author=author,
                text=text,
                rating=rating
            )
            return redirect('product_detail', pk=pk)


    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'core/product_detail.html', context)
