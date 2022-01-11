from django.shortcuts import render
# from .models import finches as finches


class Finch():
    def __init__(self, type, population, habitat):
        self.type = type
        self.population = population
        self.habitat = habitat


finches = [
    Finch('Evening Grosbeak', '3.4 million', 'Northern and montane forests'),
    Finch('Pine Grosbeak', '4.4 million', 'Open boreal forest'),
    Finch('Gray-crowned Rosy-Finch', '200,000', 'Alpine tundra'),
    Finch('Black Rosy-Finch', '20,000', 'Alpine tundra'),
    Finch('Brown-capped Rosy-Finch', '45,000', 'Alpine tundra'),
    Finch('House Finch', '31 million', 'Generalist'),
    Finch('Purple Finch', '5.9 million',
          'Mixed northern, montane, and boreal forests'),
]

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
