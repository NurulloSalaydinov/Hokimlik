from .models import Category


def context_pro_category(request):
    categories = Category.objects.all()
    return {'categories': categories}

