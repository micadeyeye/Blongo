# Create your views here.
# created by micadeyeye
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post, Section, Profile
import time
#import cgi
from time import mktime
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
#from django.contrib.auth import login, User
from django.contrib.auth.decorators import login_required
#from mongoengine.queryset import DoesNotExist

def index(request):
    # Get all posts from DB
    posts = Post.objects 
    sections = Section.objects
    profiles = Profile.objects.limit(1)

    return render_to_response('index.html', {'Posts': posts, 'Sections': sections, 'Profile': profiles},
                              context_instance=RequestContext(request))


@login_required
def publications(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       authors = request.POST['authors']
       publisher = request.POST['publisher']
       papertype = request.POST['papertype']
       page_num = request.POST['page_num']
       additional_info = request.POST['additional_info']
#       selectedpublication = request.POST['selectedpublication']
       str_date_published = request.POST['date_published']

       post = Post(title=title)
#       post.date_published = datetime.datetime.now() 
       post.date_published = datetime.fromtimestamp(mktime(time.strptime(str_date_published, "%b %d %Y")))
       post.authors = authors
       post.papertype = papertype
       post.page_num = page_num
       post.additional_info = additional_info
       post.publisher = publisher
       if request.POST.get('selectedpublication', True):
           post.selectedpublication = True;
       post.save()

    # Get all posts from DB
    posts = Post.objects

    return render_to_response('admin/publications.html', {'Posts': posts},
                              context_instance=RequestContext(request))                              
                              
                              
                             
@login_required
def sections(request):
    if request.method == 'POST':
       # save new post
       heading = request.POST['heading']
       content = request.POST['content']
       
       section = Section(heading=heading)
       section.heading = heading
#       section.content = cgi.escape(content).encode("ascii", "xmlcharrefreplace")
       section.content = content
       section.save()

    # Get all sections from DB
    sections = Section.objects

    return render_to_response('admin/index.html', {'Sections': sections},
                              context_instance=RequestContext(request))
                              
@login_required
def profile(request):
    if request.method == 'POST':
       # save new post
       details = request.POST['profile']
       profile = Profile(details=details)
       profile.details = details
       profile.save()

    # Get all sections from DB
    profiles = Profile.objects.limit(1)

    return render_to_response('admin/index.html', {'Profile': profiles},
                              context_instance=RequestContext(request))
                              
                              
@login_required
def update(request):
    id = eval("request." + request.method + "['id']")
    if Post.objects(id=id):
        post = Post.objects(id=id)[0]
        if request.method == 'POST':
            template = 'admin/index.html'
            # update field values and save to mongo
            post.title = request.POST['title']
            #str_date_published = request.POST['date_published']
            #post.date_published = datetime.fromtimestamp(mktime(time.strptime(str_date_published, "%b %d %Y")))
            post.publisher = request.POST['publisher']
            post.papertype = request.POST['papertype']
            post.authors = request.POST['authors']
            #post.additional_info = request.POST['additional_info']
            #post.page_num = request.POST['page_num']
            #if request.POST.get('selectedpublication', True):
            #    post.selectedpublication = True;
            post.save()
            params = {'Posts': Post.objects} 

        elif request.method == 'GET':
            template = 'admin/update.html'
            params = {'post':post}
    
    elif Section.objects(id=id):
        section = Section.objects(id=id)[0]
        if request.method == 'POST':
            template = 'admin/index.html'
            # update field values and save to mongo
            section.heading = request.POST['heading']
            section.content = request.POST['content']
            section.save()
            params = {'Sections': Section.objects} 

        elif request.method == 'GET':
            template = 'admin/update.html'
            params = {'section':section}
            
    elif Profile.objects(id=id):
        profile = Profile.objects(id=id)[0]
        if request.method == 'POST':
            template = 'admin/index.html'
            # update field values and save to mongo
            profile.details = request.POST['profile']
            profile.save()
            params = {'Profile': Profile.objects.limit(1)} 

        elif request.method == 'GET':
            template = 'admin/update.html'
            params = {'Profile': Profile.objects.limit(1)}

    return render_to_response(template, params, context_instance=RequestContext(request))

                                  
@login_required
def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        template = 'admin/index.html'
        if Post.objects(id=id):
            post = Post.objects(id=id)[0]
            post.delete()
            params = {'Posts': Post.objects, 'Sections': Section.objects, 'Profile': Profile.objects.limit(1)} 
        elif Section.objects(id=id):
            section = Section.objects(id=id)[0]
            section.delete()            
            params = {'Sections': Section.objects, 'Posts': Post.objects, 'Profile': Profile.objects.limit(1)} 
        elif Profile.objects(id=id):
            profile = Profile.objects(id=id)[0]
            profile.delete()            
            params = {'Profile': Profile.objects.limit(1), 'Sections': Section.objects, 'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'admin/delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))




@login_required
def admin_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    # Get all posts from DB
    posts = Post.objects
    sections = Section.objects
    profiles = Profile.objects.limit(1)

    return render_to_response('admin/index.html', {'Posts': posts, 'Sections': sections, 'Profile': profiles},
                              context_instance=RequestContext(request))

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
    
def committee_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    # Get all posts from DB
    posts = Post.objects

    return render_to_response('committee.html', {'Posts': posts},
                              context_instance=RequestContext(request))

@login_required
def committee_admin_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       authors = request.POST['authors']
       publisher = request.POST['publisher']
       papertype = request.POST['papertype']
       """
       page_num = request.POST['page_num']
       additional_info = request.POST['additional_info']
#       selectedpublication = request.POST['selectedpublication']
       str_date_published = request.POST['date_published']
       """
       post = Post(title=title)
#       post.date_published = datetime.datetime.now() 
       """
       post.date_published = datetime.fromtimestamp(mktime(time.strptime(str_date_published, "%b %d %Y")))
       post.page_num = page_num
       post.additional_info = additional_info
       if request.POST.get('selectedpublication', True):
           post.selectedpublication = True;
       """
       post.authors = authors
       post.papertype = papertype
       post.publisher = publisher
       post.save()

    # Get all posts from DB
    posts = Post.objects

    return render_to_response('admin/committee.html', {'Posts': posts},
                              context_instance=RequestContext(request))                              

