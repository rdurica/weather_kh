from django.views import generic

# Create your views here.


class HomePage(generic.ListView):
    template_name: str = "weather/index.html"

    def get_queryset(self):
        # return super().get_queryset()
        return None
