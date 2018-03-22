# artistiCal

## How to collaborate
1. ALWAYS DO THIS FIRST `git pull origin master`

2. then you can start doing some changes to the project

3. After you finished, do the following to upload your version

```
git add .
git commit -am "(whatever message you want)"
git push origin master
```

## Update
1. Before starting, do the following step to update your project repo folder

   `git remote -v`
   
   The output may be like this:
   ```
   origin	https://github.berkeley.edu/kyra-chang/artistiCal.git (fetch)
   origin	https://github.berkeley.edu/kyra-chang/artistiCal.git (push)
   ```
   but this is the old address, we need a new one
2. so do the following:
   ```
   git remote set-url --delete origin https://github.berkeley.edu/kyra-chang/artistiCal.git
   git remote set-url --add origin https://github.berkeley.edu/artistiCal/artistiCal.git
   ```
   Check again for your remote address:
   
   `git remote -v`
   
   The output may include this:
   ```
   origin	https://github.berkeley.edu/artistiCal/artistiCal.git (fetch)
   origin	https://github.berkeley.edu/artistiCal/artistiCal.git (push)
   ```
3. Last step, upload your local repo:
   ```
   git pull https://github.berkeley.edu/artistiCal/artistiCal
   git push origin master
   ```
   So that your git repo is in this new address instead of the old one! Hurray!


## Introduction

```
artistiCal
├── aC_bookfest
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── templates
│   │   ├── alpha
│   │   │   ├── ...
│   │   │   └───index.html
│   │   └───form
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static
│   ├── css
│   ├── fonts
│   ├── images
│   ├── js
│   └───sass
├── db.sqlite3
├───manage.py
└───artistiCal
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
All these files, made by `django-admin startproject`, is the whole block of our web app.

The thing we're going to do is mainly in the **aC_bookfest** folder, made by `django-admin startapp`.

* We define all objects called `Models` – this is a place in which we will define our components that will appear in our website.

* A view is a place where we put the "logic" of our application. It will request information from the `model` you created before and pass it to a `template`. `Views` are just Python functions.

* Django `template` tags allow us to transfer Python-like things into HTML, so you can build dynamic websites faster.
   Currently we haven't built any html file in aC_bookfest yet, that'll be discussed how we build the platform later.

The folder **artistiCal** you see on this page is more like the backstage page, which we may not need now.

* `manage.py` is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

* The `settings.py` file contains the configuration of your website.

* `urls.py` file contains a list of patterns used by urlresolver.


The folder **static** stores all the static files like css, js, fonts, images, sass.

The folder **.ebextensions** is for using **EB CLI** to communicate local file with the AWS system.



## EB CLI
It is a command line tool that use your terminal to communicate with the AWS system. You can use the AWS website instead to do the same thing, e.g. upload the project and deploy, init a new project...

## How to collaborate
### Terminal way
1. Add a new folder in whatever you want in your computer, or just skip this step

2. `git clone https://github.berkeley.edu/artistiCal/artistiCal.git` 

   This step will pull all the files into the folder you're in

3. For the first time you have to do this step:
   ```
   git config --global user.name "(type your calnet username)"
   git config --global user.email "(type your calnet email)"
   ```
   then you can start doing some changes to the project

4. After you finished, do the following to upload your version

```
git add .
git commit -am "(whatever message you want)"
git push origin master
```

### Github way
1. Download the file you want to do some changes
2. Do some changes
3. Go to the place where you download the file and click on **upload files**
   ![alt text][rubbish]
4. This page will come up, be sure to write down the commit message as clear as possible to let others know what changes you've made (but don't have to be like 'change on line 14' that kind of detail)
   ![alt text][rubbishs]



[rubbish]: https://github.berkeley.edu/kyra-chang/artistiCal/blob/master/rubbish.png
[rubbishs]: https://github.berkeley.edu/kyra-chang/artistiCal/blob/master/rubbishs.png






(Just to take notes here that I need this to write the markdown file)
<https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>
