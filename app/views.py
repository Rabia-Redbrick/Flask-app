from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from app import db
from app import models
from app.models import User
from app.models import employee
from flask import request, redirect
"""from django import template
from django.conf import settings

register = template.Library()

# index view function suppressed for brevity

@register.filter 
def getattribute(obj, val):
    return getattr(obj, val) 

register.filter('getattr', getattribute)
"""

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')    
def ind():
    return 'Index page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
    return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,providers=app.config['OPENID_PROVIDERS'])


@app.route('/signup')
def hello():
    email = request.form['openid']
    print("The email address is '" + email + "'")
    return redirect('/')




@app.route('/myname')
def func2():
    return 'Doneeee-----!!!!!!'

@app.route('/user/<username>')
def func3(username):
    return 'User %s' % username

@app.route('/page1')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' ,
            'date':'22sep2014'
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!', 
            'date': '5nov2014'
        }
            ]

    datadic=[
            {'user':'rabia',
            'password':'1234'
            },
            {
            'user':'mehreen',
            'password':'4321'

            }            
            ]



    return render_template('temp1.html',user=user,posts=posts,data=datadic)


@app.route('/userinfo')

def func1():

    users=User.query.all()
    """arr=[];
    for u in users:        
        arr.append(u.id)
        arr.append(u.nickname)
        #return "%r" %(u.id,u.nickname)
        
    return '%s' % arr"""    
    return render_template('mytemp.html',tabname='User',data=users)

@app.route('/emp')

def func4():

    ee=employee.query.all()
    """for uu in ee:
       # print(u.id,u.nickname)
        return "%s %d" %(uu.name,uu.contactno)
        
    return 'done'   """

    return render_template('mytemp.html',tabname='employee',data=ee)
"""
@app.route('/pg')
def pgdata():
    a=customers.query.all()
    for u in a:
        return "%d %s" %(u.id,u.name,u.phone)

    return 'hellooo'  """  

