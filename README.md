# artistiCal

## Introduction
All these files, made by `django-admin startproject`, is the whole block of our web app.

The thing we're going to do is mainly in the **aC_bookfest** folder, made by `django-admin startapp`.

The folder **artistiCal** you see on this page is more like the backstage page, which we may not need now.

The folder **.ebextensions** is for using **EB CLI** to communicate local file with the AWS system.

`manage.py` is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

## EB CLI
It is a command line tool that use your terminal to communicate with the AWS system. You can use the AWS website instead to do the same thing, e.g. upload the project and deploy, init a new project...

## How to collaborate
### Terminal way
1. Add a new folder in whatever you want in your computer, or just skip this step

2. `git clone https://github.berkeley.edu/kyra-chang/artistiCal.git` 

   This step will pull all the files into the folder you're in

3. Do some changes

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
