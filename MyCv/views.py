from xml.dom.minidom import Document

from django.shortcuts import render, redirect, get_object_or_404
from MyCv.models import GeneralSetting, Skills, Experience, Education


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    about_text = GeneralSetting.objects.get(name="about_text").parameter
    facts_text = GeneralSetting.objects.get(name="facts_text").parameter
    skills_text = GeneralSetting.objects.get(name="skills_text").parameter
    portfolio_text = GeneralSetting.objects.get(name="portfolio_text").parameter

    title_items = GeneralSetting.objects.get(name="title_items").parameter

    about_birthday = GeneralSetting.objects.get(name="about_birthday").parameter
    about_phone = GeneralSetting.objects.get(name="about_phone").parameter
    about_city = GeneralSetting.objects.get(name="about_city").parameter
    about_age = GeneralSetting.objects.get(name="about_age").parameter
    about_degree = GeneralSetting.objects.get(name="about_degree").parameter
    about_email = GeneralSetting.objects.get(name="about_email").parameter

    facts_game_project = GeneralSetting.objects.get(name="facts_game_project").parameter
    facts_web_project = GeneralSetting.objects.get(name="facts_web_project").parameter

    # skills
    skills = Skills.objects.all().order_by('order')

    # experience
    experiences = Experience.objects.all()

    # Education
    educations = Education.objects.all()

    context = {
        'page_title': 'Selin Suvancıoğlu - home',

        'site_title': site_title,
        'about_text': about_text,
        'facts_text': facts_text,
        'skills_text': skills_text,
        'portfolio_text': portfolio_text,
        'title_items': title_items,

        'about_birthday': about_birthday,
        'about_phone': about_phone,
        'about_city': about_city,
        'about_age': about_age,
        'about_degree': about_degree,
        'about_email': about_email,

        'facts_game_project': facts_game_project,
        'facts_web_project': facts_web_project,

        'skills': skills,

        'experiences': experiences,

        'educations': educations,
    }

    return render(request, 'index.html', context=context)




def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug),
    return redirect(doc.File.url)
