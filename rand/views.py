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


def dice_throw(request):
    rolls = []
    req = request.GET
    print(req)
    def roll_many(sides, times):
        for _ in range(times):
            roll = randint(1, sides)
            rolls.append(roll)
            print(roll)
    if req:
        sides = int(req['how many sides'])
        times = int(req['how many times'])
        roll_many(sides, times)
    else:
        sides = 6
        times = 2
        roll_many(sides, times)
    return render(request, 'generators/dice_throw.html',{'how many sides':sides, 'how many times':times})


def group_randomizer(request):
    people = []
    to_add = ''
    req = request.GET
    print(req)
    if req:
        while to_add != 'NO':
            to_add = str(req['Add person. To stop write NO'])
            people.append(to_add)
        print(people)
        people = people[:-1]
        number_of_teams = int(req['How many teams?'])
        number_people = len(people)
        while number_people > 0 and number_of_teams > 0:
            team = random.sample(people, int(number_people/number_of_teams))
            for x in team:
                people.remove(x)
                number_people -= int(number_people / number_of_teams)
                number_of_teams -= 1
                print(team)

    else:
        people = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        number_of_teams = 3
        number_people = len(people)
        team = random.sample(people, int(number_people/number_of_teams))
        for x in team:
            people.remove(x)
            number_people -= int(number_people/number_of_teams)
            number_of_teams -= 1
            print(team)
    return render(request, 'generators/group_randomizer.html',{'Add person. To stop write NO':to_add,'How many teams?':number_of_teams})


def elements_draw(request):
    req = request.GET
    print(req)
    items = []
    add_item = ''
    if req:
        while add_item != 'NO':
            add_item = str(req['Add person. To stop write NO'])
            items.append(add_item)
        number_of_items = int(req["How many items?"])
        random_items = random.sample(items, number_of_items)
        print(random_items)
    else:
        items = ["koc", "termos", "kawa", "sitko", "zabawka", "nóż"]
        number_of_items = 2
        random_items = random.sample(items, number_of_items)
        print(random_items)
    return render(request, 'generators/elements_draw.html',{'Add item. To stop write NO':add_item,"How many items?":number_of_items})


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


def coin(request):
    req = request.GET
    print(req)
    if req:
        coin_q = int(req['coin_q'])
        coins = random.choices(['O', 'R'], k=coin_q)
    else:
        coin_q = 1
        coins = ''
    return render(request, 'generators/coin.html', {'coin_q': coin_q, 'coins': coins})