# Django Social Media -  Dwitter 🐦💩
[Based on real python tutorial](https://realpython.com/django-social-forms-4/)

**Functionalities**

**Custom User**
* AbstractUser
* email as username
* One To One model (Profile)
* profile image

**Followers functionalities**
* Follow and Unfollow users: Many To Many model
* Create users

**CRUD Content**
* CRUD posts (dwetts)

**FrontEnd**
* Bulma
---
**Views**

1. dashboard_view: 
  * Show list of dweets of users that logged user is following -> only by the templates logic
  * form to create dweets based on logged user
  
2. profile_list_view:
  * List of created users
  * List of following and followed by

3. profile_view: 
  * list of dweets by user
  * form to follow/unfollow that user
---

**Next**
1. User management
2. Images and static files
3. Make notes on models and forms