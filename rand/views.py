import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from rand.models import Person


def index(request):
    """View function for home page of site."""

    # # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    #
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #
    # # The 'all()' is implied by default.
    # num_authors = Author.objects.count()
    #
    # context = {
    #     'num_books': num_books,
    #     'num_instances': num_instances,
    #     'num_instances_available': num_instances_available,
    #     'num_authors': num_authors,
    # }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def randint(request):
    req = request.GET
    print(req)
    if req:
        lower_bound = int(req['lower_bound_field'])
        upper_bound = int(req['upper_bound_field'])
        rand_int = random.randint(lower_bound, upper_bound)
    else:
        lower_bound = 0
        upper_bound = 10
        rand_int = ''
    return render(request, 'generators/randint.html', {'lower_bound': lower_bound, 'upper_bound': upper_bound,
                                                       'rand_int': rand_int})


def lottery(request):
    req = request.GET
    print(req)
    if req:
        total_balls = int(req['total_balls'])
        drawn_balls = int(req['drawn_balls'])
        rand_balls = sorted(random.sample(list(range(1, total_balls + 1)), drawn_balls))
        rand_balls = ', '.join(str(n) for n in rand_balls)
    else:
        total_balls = 49
        drawn_balls = 6
        rand_balls = ''
    return render(request, 'generators/lottery.html', {'total_balls' : total_balls, 'drawn_balls': drawn_balls,
                                                       'rand_balls': rand_balls})


@csrf_exempt
def group(request):
    people = None
    person = None
    if request.method == 'POST':
        p = request.POST
        print(p)
        if 'name' in p and 'nick' in p:
            if p['name'] and p['nick']:
                print(p['name'])
                person = Person(name=p['name'], nick=p['nick'])
                person.save()
        else:
            Person.objects.all().delete()
        return HttpResponseRedirect(request.path_info)

    elif request.method == 'GET':
        print(request.GET)
        if people:
            person = random.choice(people)
        else:
            person = None

    people = Person.objects.all()
    if (not person) and people:
        person = random.choice(people)

    return render(request, 'generators/person.html', {'people': people, 'person': person})
