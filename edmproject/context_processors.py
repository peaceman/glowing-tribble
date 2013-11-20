from edmproject.models import ProjectFileCategory


def categories(request):
    return {'categories': ProjectFileCategory.objects.all()}