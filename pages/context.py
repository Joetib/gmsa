from .models import Image, Configuration

def get_context(request):
    return {
        "config": Configuration.object(),
        "gallery_images": Image.objects.all()[:6]
    }