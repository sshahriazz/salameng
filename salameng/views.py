from django.shortcuts import render
from salameng.models import OurTeam, HeroPicture, Numbers, About, ClientReview


def index(request):
    image = HeroPicture.objects.first()
    numbers = Numbers.objects.first()
    team = OurTeam.objects.all()
    about = About.objects.first()
    review = ClientReview.objects.all()
    context = {
        'hero_image': image,
        'numbers': numbers,
        'team': team,
        'about': about,
        'review': review
    }
    print(image)
    return render(request, 'salameng/index.html', context)
