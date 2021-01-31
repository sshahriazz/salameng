from django.shortcuts import render
from salameng.models import OurTeam, HeroPicture, Numbers, About, ClientReview, ContactUs
from salameng.forms import ClientQueryForm

def index(request):
    image = HeroPicture.objects.first()
    numbers = Numbers.objects.first()
    team = OurTeam.objects.all()
    about = About.objects.first()
    review = ClientReview.objects.all()
    contact = ContactUs.objects.first()

    client_query_form = ClientQueryForm(request.POST)
    if client_query_form.is_valid():
        client_query_form.save()
    context = {
        'hero_image': image,
        'numbers': numbers,
        'team': team,
        'about': about,
        'review': review,
        'contact': contact,
        'client_query_form': client_query_form
    }
    print(image)
    return render(request, 'salameng/index.html', context)
