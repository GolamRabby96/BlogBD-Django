from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Article,Author,Comment, Groups, GroupArticle,GroupComment, RequestGroup,Doner
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import CreateUser, Author_form, Article_form, RegisterDate, Contact_form, Comment_form, Create_group, Group_article_form, Group_comment_form,Doner_form
from django.utils import timezone
from django.db.models import Count
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from django.db.models import Count
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
# Create your views here.

def get_index(request):
    post=Article.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date').annotate(like_count=Count('likes'))
    search = request.GET.get('q')
    if search:
        post=post.filter(
            Q(post_title__icontains=search)|
            Q(post_categori__icontains=search)|
            Q(post_body__icontains=search)
        )
    if not post:
        messages.error(request,f'Not Found any article ({search}) ')
    paginator = Paginator(post, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    # catagory = Article.objects.filter(post_categori='post_categori')
    # catagory = Article.objects.all().values('post_categori').annotate(total=Count('post_categori'))
    # catagory = Article.objects.all().values('post_categori').distinct()
    catagory = Article.objects.values('post_categori').annotate(post_categori_count=Count('post_categori'))
    # getComment = Comment.objects.values('comment').annotate(comment_author_count=Count('comment_author'))
    # getComment = Comment.objects.all()
    # popular_section = Article.objects.annotate(Count('likes'))
    popular_section = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:10]
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked =True
    context ={
        "post":total_article,
        "cat":catagory,
        "popular":popular_section
    }
    return render(request,"index.html",context)


def get_post_create(request):
    if not request.user.is_authenticated:
        raise Http404
    form = Article_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        auth = get_object_or_404(Author, name= request.user.id)
        instance.article_author=auth
        abuse=['stupid','bastard','ass','arse','shit','whore','Son of bitch','asshole','rascal',]
        inputdata = instance.post_body.split()
        flag = True
        ab=[ ]
        for dt in inputdata:
            if dt in abuse:
                flag= False
                ab.append(dt)


        if flag == False:
            messages.error(request,ab)
            messages.error(request, 'Please Avoid Abuse Word:)')
        if flag == True:
            instance.save()
            messages.success(request, 'Post Create Successfully:)')
            return redirect('profile_view')
    context={"form":form}
    return render(request,'create_article.html',context)

def get_post_update(request, id):
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(Article, id=id)
    form = Article_form(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        if instance.post_image:
            ice = get_object_or_404(Article, id=id)
            oldname =ice.post_image.name
            newname = instance.post_image.name
            if oldname != newname:
               ice.post_image.delete()
        auth = get_object_or_404(Author, name= request.user.id)
        instance.article_author=auth
        instance.save()
        messages.success(request, 'Post Update Successfully:)')
        return redirect('profile_view')
    context={"form":form}
    return render(request,'create_article.html',context)

def get_post_delete(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Article, id=id)
        instance.post_image.delete()
        instance.delete()
        messages.success(request,'Post Delete Successful :)')
        print("..............",id,"...........................")
        return redirect('profile_view')
    else:
        messages.error(request,'Please Login First')
        return redirect('login')

def get_profile_view(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author = get_object_or_404(Author,name=user.id)
        if user:
            article = Article.objects.filter(article_author=author.id).order_by('-create_date').annotate(like_count=Count('likes'))
            joindgroup = Groups.objects.filter(group_member=author)
            mywongroup = Groups.objects.filter(super_auth=author)
            access=True
            context ={
                "user":user,
                "author":author,
                "article":article,
                'joindgroup':joindgroup,
                'mywongroup':mywongroup,
                'access':access
            }
            return render(request,'profile.html',context)
        else:
            raise Http404
    else:
        messages.error(request,'Please Login First')
        return redirect('login')


def get_user_profile_view(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        if request.user.id == user.id:
            return redirect('profile_view')

        author = get_object_or_404(Author,name=user.id)
        if user:
            article = Article.objects.filter(article_author=author.id).order_by('-create_date')
            access=False
            context ={
                "user":user,
                "author":author,
                "article":article,
                'access':access
            }
            return render(request,'profile.html',context)
        else:
            raise Http404
    else:
        messages.error(request,'Please Login First')
        return redirect('login')
# .................................

# .................................

def get_post_published(request, id):
    if request.user.is_authenticated:
        post= get_object_or_404(Article, id=id)
        post.publis_now()
        return redirect('profile_view')

    else:
        messages.error(request,'Please Login First')
        return redirect('login')


def get_profile_update(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        # author = Author.objects.filter(name=user.id)
        author=get_object_or_404(Author,name=user.id)
        form = Author_form(request.POST or None, request.FILES or None, instance=author)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.profile_picture:
                us = get_object_or_404(Author,name=user.id)
                oldname = us.profile_picture.name
                newname = instance.profile_picture.name
                if oldname != newname:
                    us.profile_picture.delete()
            if instance.cover_picture:
                cv = get_object_or_404(Author,name=user.id)
                oldname = cv.cover_picture.name
                newname = instance.cover_picture.name
                if oldname != newname:
                    cv.cover_picture.delete()
            instance.name = user
            instance.save()
            return redirect('profile_view')
        return render(request,'update_profile.html',{"form":form})
    else:
        messages.error(request,'Please Login First')
        return redirect('login')


def get_single_post(request, id):
    form = Comment_form(request.POST or None)
    if request.user.is_authenticated:
        getComment = Comment.objects.filter(comment_post=id).order_by('-create_date')
        auth = get_object_or_404(User, id=request.user.id)
        user = get_object_or_404(Author, name = auth.id)
        article = get_object_or_404(Article, id=id)
        if user in article.likes.all():
            userlike=True
        else:
            userlike=False
        likes = article.likes.count
        catagory = Article.objects.values('post_categori').annotate(post_categori_count=Count('post_categori'))
        popular_section = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:10]
        # post = get_object_or_404(Article, id=id)
        context={
                "post":article,
                "form":form ,
                "getComment":getComment,
                "likes":likes,
                "cat":catagory,
                "popular":popular_section,
                "userlike":userlike
            }
        return render(request, 'single_post.html', context)
    else:
        messages.error(request,'Please Login First')
        return redirect('login')


def get_contact (request):
    if request.user.is_authenticated:
        sup = get_object_or_404(User, id = request.user.id)
        auth = get_object_or_404(Author, name = sup.id)
        form = Contact_form(request.POST or None)

        # print(emails)
        if form.is_valid():
            user = form.save(commit=False)
            user.email_auth = auth
            user.email = request.user.email
            user.save()
            mail_subject = form.cleaned_data.get('subject')
            email_body = form.cleaned_data.get('email_body')
            user_id = request.user.id
            user_email =request.user.email
            message =render_to_string('thnq.html',{
                'user': user,
                'user_email':user_email,
                'mail_subject':mail_subject,
                'email_body':email_body,
            })
            # to_email = form.cleaned_data.get('email')
            # to_email =request.user.email
            to_email ='nisi884422@gmail.com'
            # to_email =User.objects.filter(id = request.user.id).exclude(email='')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            # >>>>>>>>>>>>>>>>> Auto Mail>>>>>>>>>>>>>>>>>>>>>>>
            message =render_to_string('automail.html',{
                'user': user,
                'mail_subject':mail_subject,
            })
            to_email =request.user.email
            # to_email =User.objects.filter(id = request.user.id).exclude(email='')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.info(request,'Thank You for your Information :)')
            return redirect('index')
        context={"sup":sup, "auth":auth, "form":form}
        return render(request,'contact.html', context)



def get_comment(request, id):
    form = Comment_form(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        auth = get_object_or_404(Author, name=request.user.id)
        article = get_object_or_404(Article, id=id)
        comment.comment_author = auth
        comment.comment_post = article
        comment.save()
        messages.success(request,'Comment Done')
        return redirect('single_post', id=id)



def get_like(request, id, name =''):
    if request.user.is_authenticated:
        auth = get_object_or_404(User, id=request.user.id)
        user = get_object_or_404(Author, name = auth.id)
        article = get_object_or_404(Article, id=id)
        if user in article.likes.all():
            article.likes.remove(user.id)
        else:
            article.likes.add(user.id)
        if name == 'likes':
            # post=Article.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date').annotate(like_count=Count('likes'))
            return redirect('single_post', id=id)
        return redirect('index')
    else:
        messages.error(request,'Please Login First')
        return redirect('login')

def get_category(request, name):
    if request.user.is_authenticated:
        catagory = Article.objects.values('post_categori').annotate(post_categori_count=Count('post_categori'))
        popular_section = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:10]
        post_cat = Article.objects.filter(post_categori = name).annotate(like_count=Count('likes'))
        context = {
            "post":post_cat,
            "cat":catagory,
            "popular":popular_section
        }
        return render(request,'category.html',context)
    else:
        messages.error(request,'Please Login First')
        return redirect('login')


# .................Group Section..........................
# .................Group Section..........................
# .................Group Section..........................


def getgroups(request):
    group = Groups.objects.all().order_by('-group_create_date')
    user = get_object_or_404(User, id=request.user.id)
    auth = get_object_or_404(Author, name = user.id)
    joindroup = Groups.objects.filter(group_member=auth)
    mywongroup = Groups.objects.filter(super_auth=auth)
    context={
        'group':group,
        'joindroup':joindroup,
        'mywongroup':mywongroup
    }
    return render(request,'groups.html',context)

def getgroups_search(request):
    if request.user.is_authenticated:
        groupname =''
        if request.method == 'POST':
            groupname = request.POST.get('gname')
        group = Groups.objects.filter(group_name__icontains=groupname)
        user = get_object_or_404(User, id=request.user.id)
        auth = get_object_or_404(Author, name = user.id)
        joindroup = Groups.objects.filter(group_member=auth)
        mywongroup = Groups.objects.filter(super_auth=auth)
        context={
            'group':group,
            'joindroup':joindroup,
            'mywongroup':mywongroup
        }
        return render(request,'groups.html',context)
    else:
        messages.error(request,'Please Login First')
        return redirect('login')


def getjoingroup(request,id):
    user = get_object_or_404(User, id=request.user.id)
    auth = get_object_or_404(Author, name = user.id)
    group = get_object_or_404(Groups, id=id)

    if auth in group.group_member.all():
        group.group_member.remove(auth.id)
        messages.error(request,'You Leave This Group Now')
    else:
        rrr = RequestGroup.objects.filter(whichgroup=group.id)
        check = False
        for jg in rrr:
            if auth.id == jg.who.id:
                messages.error(request,'Already Send')
                check = True

        if check is False:
            requestgroup = RequestGroup()
            requestgroup.whichgroup=group
            requestgroup.who=auth
            requestgroup.save()
            messages.info(request,'your Request is send. the admin is decided for you')
    return redirect('singlegroup', id=id)


def getsinglegroup(request, id):
    user = get_object_or_404(User, id=request.user.id)
    auth = get_object_or_404(Author, name = user.id)
    group = get_object_or_404(Groups, id=id)
    if auth in group.group_member.all():
        access=True
    else:
        access = False
    article = GroupArticle.objects.filter(group=group.id).annotate(like_count=Count('group_post_likes')).order_by('-group_post_create_date')
    joindroup = Groups.objects.filter(group_member=auth)
    if auth == group.super_auth:
        groupmodarator = True
    else:
        groupmodarator = False
    mywongroup = Groups.objects.filter(super_auth=auth)
    requestgroup = RequestGroup.objects.filter(whichgroup=group.id)

    requestmember = False
    for jg in requestgroup:
        if auth.id == jg.who.id:
            requestmember = True
        else:
            requestmember = False
    context={
        'group':group,
        'access':access,
        'article':article,
        'joindroup':joindroup,
        'groupmodarator':groupmodarator,
        'mywongroup':mywongroup,
        'groupid':id,
        'requestgroup':requestgroup,
        'requestmember':requestmember
    }
    return render(request, 'single_group.html', context)


def Getcreategroup(request):
    form = Create_group(request.POST or None, request.FILES or None)
    if form.is_valid():
        auth = get_object_or_404(User, id=request.user.id)
        user = get_object_or_404(Author, name = auth.id)
        group=form.save(commit=False)
        group.super_auth=user
        group.save()
        return redirect('groups')
    return render(request, 'creategroup.html',{'form':form})

def Getgroupdelete(request, id):
    group = get_object_or_404(Groups, id=id)
    group.group_photo.delete()
    group.delete()
    return redirect('groups')




def Getmemberadd(request, gid,mid):
    user = get_object_or_404(User, id=mid)
    author = get_object_or_404(Author,name=user.id)
    group = get_object_or_404(Groups, id=gid)
    reqgroup = get_object_or_404(RequestGroup, whichgroup=group.id)
    reqgroup.delete()
    if author in group.group_member.all():
        group.group_member.remove(author.id)
    else:
        group.group_member.add(author.id)
    #messages.success(request,'Successfully Add This user')
    return redirect('singlegroup', id=gid)


def Getmemberremove(request, gid,mid):
    user = get_object_or_404(User, id=mid)
    author = get_object_or_404(Author,name=user.id)
    group = get_object_or_404(Groups, id=gid)
    reqgroup = get_object_or_404(RequestGroup, whichgroup=group.id)
    reqgroup.delete()
    messages.info(request,'Successfully Removed This user')
    return redirect('singlegroup', id=gid)



# group article start
def Getcreategrouparticle(request,id):
    if not request.user.is_authenticated:
        raise Http404
    form = Group_article_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        auth = get_object_or_404(Author, name= request.user.id)
        instance.group_article_author = auth
        getgroup = get_object_or_404(Groups, id=id)
        instance.group=getgroup
        instance.save()
        #messages.success(request, 'Group Post Create Successfully:)')
        return redirect('singlegroup', id=id)
    context={"form":form}
    return render(request,'creategrouparticle.html',context)


def Getupdategrouparticle(request, gid,pid):
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(GroupArticle, id=pid)
    form = Group_article_form(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        auth = get_object_or_404(Author, name= request.user.id)
        instance.group_article_author = auth
        getgroup = get_object_or_404(Groups, id=gid)
        instance.group=getgroup
        if instance.group_post_image:
            gai=get_object_or_404(GroupArticle, id=pid)
            gai.group_post_image.delete()
        instance.save()
        messages.success(request, 'Update Successfully:)')
        return redirect('singlegroup', id=gid)
    context={"form":form}
    return render(request,'creategrouparticle.html',context)



def Getdeletegrouparticle(request, gid,pid):
    if request.user.is_authenticated:
        instance = get_object_or_404(GroupArticle, id=pid)
        instance.group_post_image.delete()
        instance.delete()
        messages.success(request,'Post Delete Successful :)')
        return redirect('singlegroup', id=gid)
    else:
        messages.error(request,'Please Login First')
        return redirect('login')



def Getsinglegrouparticle(request, gid, pid):
    form = Group_comment_form(request.POST or None)
    if request.user.is_authenticated:
        auth = get_object_or_404(Author, name = request.user.id)
        user = get_object_or_404(Author, name=auth.id)
        group = get_object_or_404(Groups, id=gid)
        joindroup = Groups.objects.filter(group_member=auth)
        mywongroup = Groups.objects.filter(super_auth=auth)
        article = get_object_or_404(GroupArticle, id=pid)
        getComment = GroupComment.objects.filter(group_comment_post=pid).order_by('-group_comment_date')
        if user in article.group_post_likes.all():
            group_user_like=True
        else:
            group_user_like=False

        likes = article.group_post_likes.count
        context={
            'group':group,
            'post':article,
            'joindroup':joindroup,
            'mywongroup':mywongroup,
            'groupid':gid,
            'like':likes,
            "glikes":group_user_like,
            "form":form,
            "getComment":getComment
        }
        return render(request, 'singlegroup_article.html', context)


def Getcommentgrouparticle(request, gid, pid):
    form = Group_comment_form(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        auth = get_object_or_404(Author, name= request.user.id)
        article = get_object_or_404(GroupArticle, id=pid)
        comment.group_comment_author = auth
        comment.group_comment_post = article
        comment.save()
        return redirect('single_grouparticle', gid=gid, pid=pid)



def Getlikegrouparticle(request, gid, pid,name=''):
    if request.user.is_authenticated:
        auth=get_object_or_404(User, id=request.user.id)
        user = get_object_or_404(Author, name= auth.id)
        article = get_object_or_404(GroupArticle, id=pid)
        if user in article.group_post_likes.all():
            article.group_post_likes.remove(user.id)
        else:
            article.group_post_likes.add(user.id)
        if name=='gplike':
            return redirect('single_grouparticle', gid=gid, pid=pid)
        return redirect('singlegroup', id=gid)

def Getshowgroupmeber(request, gid):
    # group = get_object_or_404(Groups, id=gid)
    group = Groups.objects.filter(id=gid)
    context={
        "member":group,
        "groupid":gid
    }
    return render(request,'remove_groupmember.html', context)



def Getremovegroupmeber(request, gid,id):
    user = get_object_or_404(User, id=id)
    author = get_object_or_404(Author,name=user.id)
    group = get_object_or_404(Groups, id=gid)

    if author in group.group_member.all():
        group.group_member.remove(author.id)
    messages.info(request,'Successfully remove This user')
    return redirect('singlegroup', id=gid)

# blood search section
def Getdivisions(request):
    return render(request,'divisions.html')

def Getsearchblood(request,name):
    doner = Doner.objects.filter(division=name)
    if name=='Khulna':
        dis=('Khulna','Satkhira','Narail','Bagerhat','Chuadanga','Jessore','Jhenaidah','Kushtia','Magura','Meherpur')
    if name=='Dhaka':
        dis=('Dhaka','Faridpur','Gazipur','Gopalganj','Kishoreganj','Madaripur','Manikganj','Narsingdi','Munshiganj','Rajbari','Shariatpur','Tangail','Narayanganj')
    if name=='Barisal':
        dis=('Barisal','Barguna','Bhola','Jhalokati','Patuakhali','Pirojpur')
    if name=='Sylhet':
        dis=('Sylhet','Habiganj','Moulvibazar','Sunamganj')
    if name=='Rangpur':
        dis=('Rangpur','Dinajpur','Gaibandha','Kurigram','Lalmonirhat','Nilphamari','Panchagarh','Thakurgaon')
    if name=='Mymensingh':
        dis=('Mymensingh','Jamalpur','Netrokona','Sherpur')
    if name=='Chittagong':
        dis=('Chittagong','Bandarban','Brahmanbaria','Chandpur','Comilla',"Cox's Bazar",'Feni','Khagrachhari','Lakshmipur','Noakhali','Rangamati')
    if name=='Rajshahi':
        dis=('Rajshahi','Bogra','Joypurhat','Naogao','Natore','Chapainawabganj','Pabna','Sirajganj')

    author = get_object_or_404(Author,name=request.user.id)
    find = Doner.objects.all()
    alreadyregister=False
    for uu in find:
        if author==uu.doner_auth:
            alreadyregister=True
        else:
            alreadyregister=False
    context={
        'doner':doner,
        'dis':dis,
        'alreadyregister':alreadyregister,
        'name':name
    }
    return render(request,'searchblood.html',context)


def Getsearchbloodresult(request,name):
    if name=='Khulna':
        dis=('Khulna','Satkhira','Narail','Bagerhat','Chuadanga','Jessore','Jhenaidah','Kushtia','Magura','Meherpur')
    if name=='Dhaka':
        dis=('Dhaka','Faridpur','Gazipur','Gopalganj','Kishoreganj','Madaripur','Manikganj','Narsingdi','Munshiganj','Rajbari','Shariatpur','Tangail','Narayanganj')
    if name=='Barisal':
        dis=('Barisal','Barguna','Bhola','Jhalokati','Patuakhali','Pirojpur')
    if name=='Sylhet':
        dis=('Sylhet','Habiganj','Moulvibazar','Sunamganj')
    if name=='Rangpur':
        dis=('Rangpur','Dinajpur','Gaibandha','Kurigram','Lalmonirhat','Nilphamari','Panchagarh','Thakurgaon')
    if name=='Mymensingh':
        dis=('Mymensingh','Jamalpur','Netrokona','Sherpur')
    if name=='Chittagong':
        dis=('Chittagong','Bandarban','Brahmanbaria','Chandpur','Comilla',"Cox's Bazar",'Feni','Khagrachhari','Lakshmipur','Noakhali','Rangamati')
    if name=='Rajshahi':
        dis=('Rajshahi','Bogra','Joypurhat','Naogao','Natore','Chapainawabganj','Pabna','Sirajganj')

    author = get_object_or_404(Author,name=request.user.id)
    find = Doner.objects.all()
    for uu in find:
        if author==uu.doner_auth:
            alreadyregister=True
        else:
            alreadyregister=False
    if request.method == 'POST':
        district = request.POST.get('district')
        bgrop = request.POST.get('bgrop')
    doner = Doner.objects.filter(district=district,blood_group=bgrop)
    context={
        'doner':doner,
        'dis':dis,
        'alreadyregister':alreadyregister,
        'name':name
    }
    return render(request,'searchblood.html',context)



def Getbecomedoner(request):
    form = Doner_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        auth = get_object_or_404(Author, name=request.user.id)
        instance.doner_auth=auth
        instance.save()
        return redirect('divisions')
    return render(request,'becomedoner.html',{'form':form})






#######################################

def get_register(request):
    # date_form = request.POST.get('date')
    date_form = RegisterDate(request.POST or None)
    form = CreateUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        date =date_form.save(commit=False)
        date.name = instance
        date.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('active_account.html', {
            'user': instance,
            'domain': current_site.domain,
            'uid':instance.id,
            'token':account_activation_token.make_token(instance),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
        email.send()
        messages.success(request,'Registraion Successfull Please Check Your Email And Active Your account')
        return redirect('index')
    context={"form":form,"date_form":date_form}
    return render(request,'register.html',context)

def activate(request, uid, token):
    try:
        user = get_object_or_404(User, id=uid)
    except:
        raise Http404("No user Found")
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request,'Thank you for your email confirmation.you are Login Now.')
        return redirect('index')
    else:
        return HttpResponse('Activation link is invalid!')


def get_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            auth = authenticate(request,username=username, password=password)
            if auth is not None:
                login(request,auth)
                return redirect('index')
            else:
                messages.error(request,'Username and password are not matching')
                return render(request,'login.html')
        return render(request,'login.html')

def get_logout(request):
    logout(request)
    messages.info(request,'you are Successfully logout now.. ')
    return redirect('index')
