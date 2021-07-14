from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('register', views.get_register, name='register'),
    path('login', views.get_login, name='login'),
    path('logout', views.get_logout, name='logout'),


    path('post_create', views.get_post_create, name='post_create'),
    path('post_update/<int:id>', views.get_post_update, name='post_update'),
    path('post_delete/<int:id>', views.get_post_delete, name='post_delete'),
    path('profile_view', views.get_profile_view, name='profile_view'),
    path('user_profile_view/<int:id>', views.get_user_profile_view, name='user_profile_view'),
    path('post_published/<int:id>', views.get_post_published, name='post_published'),
    path('profile_update/<int:id>', views.get_profile_update, name='profile_update'),
    path('single_post/<int:id>', views.get_single_post, name='single_post'),
    path('contact', views.get_contact, name='contact'),
    path('comment/<int:id>', views.get_comment, name='comment'),
    path('like/<int:id>/<name>', views.get_like, name='like'),
    path('category/<name>', views.get_category, name='category'),
    path('activate/<uid>/<token>', views.activate, name='activate'),

    path('groups', views.getgroups, name='groups'),
    path('groupsearch', views.getgroups_search, name='groupsearch'),
    path('joingroup/<int:id>', views.getjoingroup, name='joingroup'),
    path('singlegroup/<int:id>', views.getsinglegroup, name='singlegroup'),
    path('creategroup', views.Getcreategroup, name='creategroup'),
    path('groupdelete/<int:id>', views.Getgroupdelete, name='groupdelete'),

    path('memberadd/<int:gid>/<int:mid>', views.Getmemberadd, name='memberadd'),
    path('memberremove/<int:gid>/<int:mid>', views.Getmemberremove, name='memberremove'),

    path('create_grouparticle/<int:id>', views.Getcreategrouparticle, name='create_grouparticle'),
    path('update_grouparticle/<int:gid>/<int:pid>', views.Getupdategrouparticle, name='update_grouparticle'),
    path('delete_grouparticle/<int:gid>/<int:pid>', views.Getdeletegrouparticle, name='delete_grouparticle'),
    path('single_grouparticle/<int:gid>/<int:pid>', views.Getsinglegrouparticle, name='single_grouparticle'),

    path('like_grouparticle/<int:gid>/<int:pid>/<name>', views.Getlikegrouparticle, name='like_grouparticle'),
    path('Comment_grouparticle/<int:gid>/<int:pid>', views.Getcommentgrouparticle, name='Comment_grouparticle'),

    path('remove_groupmeber/<int:gid>/<int:id>', views.Getremovegroupmeber, name='remove_groupmeber'),
    path('show_groupmeber/<int:gid>', views.Getshowgroupmeber, name='show_groupmeber'),
    # blood section
    path('divisions', views.Getdivisions, name='divisions'),
    path('searchblood/<name>', views.Getsearchblood, name='searchblood'),
    path('searchbloodresult/<name>', views.Getsearchbloodresult, name='searchbloodresult'),
    path('becomedoner', views.Getbecomedoner, name='becomedoner'),

]
