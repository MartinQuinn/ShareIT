from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post , Club
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def create(request):
    if request.method =='POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return render(request, 'clubs/home.html')
        else:
            return render(request, 'clubs/create.html', {'error':'Sorry, You need to have both a title and a Url to create a post.'})

    else:
        return render(request, 'clubs/create.html')

def home(request):
    try:
        del request.session['query']
    except: 
        query = ""
        
    return render(request, 'clubs/home.html')
    
def listingCounties(request):
    try:
        if request.method =='POST':
            
            query = ""            
            query = request.POST.get('County', "")
            request.session['query'] = query
            clubs_list = Club.objects.filter(county__icontains= request.session['query'])
            
        else:
            
            clubs_list = Club.objects.filter(county__icontains= request.session['query'])
            
    except KeyError:
        
        query = ""
        clubs_list = Club.objects.order_by('name')

        
    paginator = Paginator(clubs_list, 15)
    page = request.GET.get('page')
    
    try:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(1)
        
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(paginator.num_pages)
        
    except query:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page()

    return render(request, 'clubs/county.html', {'clubs':clubs})
    

    

def listing(request):
    try:
        if request.method =='POST':
            
            query = request.POST.get('search_clubs', "")
            request.session['query'] = query
            clubs_list = Club.objects.filter(name__icontains= request.session['query'])
            
        else:
            
            clubs_list = Club.objects.filter(name__icontains= request.session['query'])
            
    except KeyError:
        
        query = ""
        clubs_list = Club.objects.order_by('name')

        
    paginator = Paginator(clubs_list, 15)
    page = request.GET.get('page')
    
    try:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(1)
        
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(paginator.num_pages)
        
    except query:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page()

    return render(request, 'clubs/club.html', {'clubs':clubs})
    

