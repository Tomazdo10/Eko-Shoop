#                                                   EKO SHOOP

![Screenshot (458)](https://user-images.githubusercontent.com/66019489/120065959-efac1d00-c06b-11eb-97ed-1dbce24b50dd.png)


## LINKS :
-------------------------------------------------------------------------------------------------------

### Introduction

### User Stories

### Feauters/Wireframes

### Theme & Topography

### Database & Design

### Feauters Left to Implement

### Technologies Used

### Testing:
* Code Testing
* User Story Testing
* Screen Size Testing
* Further Testing
* Manual Testing

### Deployment

### Issues & Bugs

### Credits & Aknowledgements

---------------------------------------------

## Introduction

Hi my name is Tomaz Dobnik and this is my last project to build for the software developer diploma
at [Code Institute](https://codeinstitute.net).The idea for the project came from passion for the nature
surounded by us and how badly we impact on the inviroment arround us, with pollution and so much litter and plastic everywhere.
So I've decided to do something simple like an Eko-Shoop store where you can buy or find some idea or advice
how to reduce the use of plastic arround you and make our Planet greener.

(Link to live open site : Click Here)[https://8000-aquamarine-elk-fqic5cog.ws-eu08.gitpod.io/]

-----------------------------------------------------
### User Story

* As a Shopper i want to be able to view all the products and 
  chose one's i like the most and need the most.

* As a Shopper i want to see what i have in my shopping bag and 
  how much I'am speending.

* As a Shopperi would like to see specifications of product and 
  and view details of the individual product.

* As a Shopper i would like see new products on the market and 
  have access to new trends.

* As a user i will want to see if the site is easy accessible for me 
  and check immediately if the site is build for me.
  
* As a site user i will want to easily to login or logout in to the account
  and to access and use personal information.

* As a site user I would like to have my own profile and see the history
  of payments and orders I've done.

* As a shopper I would like to search for a name or a particular product
  I'am interested in or find a specific product.

* As a shopper I want to see what I have searched for and make a decision
  if that's the product i want.

* As a shopper I want to see the items in my bag and adjust the quantity if i want to.
  Remove the item from the shopping bag or swap it for another one.

* As a shopper I want t want to have the ability to order or buy as a guest if if i'm 
  not registered. 
-----------------------------------------------------------------------------------

## Features & Wireframes

### Landing Page

The website is design to be simple as it possible, to give a clear image and links to 
possibility to be able to shop and explore for new items and stuff you want to purchase.
The page and rest of the paiges will have a logo and a main search window in the middle,
as well navbar links to the shopping area, shopping bag and login user account.
On the smaller screens this search funcionality will be achivable thrue the dropdown
search box.

The main task of the search bar is to navigate users true the website to find the 
products they are looking for or mainly to explore.

### Products

 * Every page will show the products with (title,price,image), and back to top icon.

### One Product

 * An individual product, chosed from the all products view with the description of all 
   fields, the ability to plus and minus the quantity of order and buttons for user, to
   continue shopping or add the relevant number of items to basket.

### Sign Up 

* Page It's giving the user ability to create the account, using their personal details
  with button submit and sign-in or navigate to login page if they see that they actually
  have the account open.

### Sign In 

* Page is giving the user ability to enter their username or email address and password so
  they can login to their account.

### Profile 

* A simple page giving user the ability to review  their profile details and update if 
  required so.

### Bag/Basket 

* It's a page showing with the items that user has put it in to buy or see what are the 
  items he's interested in, givin him the total price he spend or attend to spend it.
  Buttons giving the ability to continue shopping or to go to checkout app if the user
  has finished shopping.

### Checkout 

* A page that gives a user the ability to reviw and purchase all the items he put in the bag.
-------------------------------------------------------------------------------------

## Theme & Colors
----------------------------------------------------------------------------------------
* Colors are design to be soft and light grey, white and green image for background
  give the website emphasis, the below colour palette was generated using [coolors](https://coolors.co/555555-ffffff-000000-222222-627262).

![project 4](https://user-images.githubusercontent.com/66019489/116603139-7f9f5f80-a924-11eb-8725-e8c010d4529f.png)

## Database and Feauture Design

 ### Products: 
-------------------------------------------------------------------------------------------------
 * The user data information is stored in models:

   * consisting of 6 subsets

     * SKU-Numerical identifier
     * Name of the product
     * Description of the product
     * Price of the product 
     * Rating 
     * Image of the product

## Features left to implement

 * In the future if this would rael bussines i would add more products to website more
   options to chose from, i would also add the email option to login and login true 
   social media account.
---------------------------------------------------------------------------------------
## Technologies Used:

* HTML, CSS, Javascript & Python languages
* [Google Fonts](https://fonts.google.com/)-Family=Lato font used through all pages.
* [EcoShoop](https://theecoshopuk.com/),[andKeep](https://andkeep.com),[Google](https://www.google.com/)-I found images and products on
  different pages as presented to get some more specific idea for the products and my Eko Shoop project.
* [Gitpod](https://www.gitpod.io/) IDE used to code.
* [Github](https://github.com/)-to host the repositories for this project.
* [Git](https://git-scm.com/)-for version control.
* [Wirefames](https://balsamiq.com)-used to design wireframes.
* [Django](https://www.djangoproject.com/)-used as the framework to create the app and the template language.
* [Coloors](https://coolors.co/)-used for colour palette.
<<<<<<< HEAD
* [Bootstrap](https://getbootstrap.com/)-front-end framework used.
* [Stripe](https://stripe.com)-used to process credit card transactions.
* [AWS](https://aws.amazon.com/)-used to store static and media files.
* [Fontawesome](https://fontawesome.com/)-used for various icons across the site.

#### Languages Used 

[Image](Screenshot(376).png)

----------------------------------------------------------------------------------------------
## Testing

  * Code Testing
  * Manual Testing
  * User Story Testing
  * Screen size Testing

### Code Testing 

[W3C HTML Validator](https://validator.w3.org/nu/#textarea) HTML: tested by right clicking and then using View page source to see rendered page code.
 I am aware that there are outstanding issues with the HTML code validation but sue to time constraints I was unable to resolve all issues.

[The W3C CSS Validation](https://jigsaw.w3.org/css-validator/) CSS: style.css tested with  W3C CSS Validation no errors remain.

[JSHint](https://jshint.com) Javascript: was tested with no errors remain.

Python Code tested by typing python3 -m flake8 to test all .py files.


  * Errors that were automatically generated (the init files, migration files, Django setup files etc). This constitutes the majority of issues
    Some E501 errors remain as the lines cannot be shortened
    Some E128 errors remain as the flake8 check would need them for be indented far too much in to pass and would not be user friendly
    Some DJ01 errors remain as this setting should be present
---------------------------------------------------------------------------------------------------------------
## Manual Testing 

### Home Page 
  * Tested the Home link on the navbar to check that the home page is rendered.
  * Tested the Shop link on the navbar to check that the /products page is rendered?
  * Tested the search box from all views to check that the relevant products are displayed
    when the word searched is in the product title or product description
  * Tested the My Account link on the navbar to check that the correct dropdowns display 
    dependent on whether the user is logged in or not
  * Tested the shopping basket icon to check that the /bag page is rendered
----------------------------------------------------------------------------------------------------------
 I could not finish with the proper testing
 Due too run out of time i couldn not test the shopping bag properly or the products itself because i ran into 
 an issue which didn't load me the products to my website, and because i run out of time to finish the project
 properly i had to levae it as it is. Hopefully i will be able to fixed it and deploy it again with all the sites.
 Properly functional.

 --------------------------------------------------------------------------------------------------
 ## Deployment

 ### Deploy to Heroku

  * Sign in to [Heroku](https://signup.heroku.com)
  * Create a new app by clicking Create new app in the New dropdown box
  * Choose a relevant and unique app name
  * Add Heroku Postgres as an add-on
  * In the Config Vars add the relevant variables for: 
    SECRET_KEY
    STRIPE_PUBLIC_KEY
    STRIPE_WH_KEY
    DATABASE_URL
    USE_AWS (set to True)
    DISABLE_COLLECT_STATIC
  * Freeze the requirements in the terminal by typing 'pip3 freeze > requirements.txt'
  * Create a Procfile and save the below code into item
    web: gunicorn eko_shoop_home.wsgi:application
  * To set the database so it works with Postgres comment out the current database settings 
    and add the below code to settings.py

    DATABASES = {
    'default': dj_database_url.parse(database_url_from_heroku_config_vars)
    } 

  * Run migrations
  * Create a superuser by typing python3 manage.py createsuperuser
  * Revert back to the original setup in settings.py
  * Add the below code in an if statement

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


   * Add the app name to ALLOWED_HOSTS in settings.py
   * To make it easier, set Heroku to deploy automatically when code is pushed to GitHub


 ## Amazon web Services

 Go to [AWS](https://aws.amazon.com/)
* Search for S3 and create a new bucket, give this bucket the same name as the Heroku app
* Unblock public access and finish creating the bucket
* In the permissions tab, edit cross origin resource sharing (CORS) and paste the below in

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]

  * Select Policy Generator to create a new security Policy
  * Select S3 Bucket Policy as the type of policy and add a * to principle
  * Set the Action to Get Object and paste in the ARN (Amazon Resource Name)
  * Click Add Statement, then Generate Policy
  * Copy the policy and paste it into the bucket policy editor
  * Make sure a * is added to the end of the Resource value to allow access to all resources in the bucket
  * In the ACL (Access Control List), set list object permissions for everyone
  * Open IAM (Identity and Access Management) and create a group giving it a name
  * Go the the Policies tab and choose Create Policy
  * Select Import Managed Policy from the JSON tab, search for S3 and import S3 Full Access Policy
  * Back on S3, copy the ARN and paste this twice in to the Resource item. The second arn line should have a /* on the end like the below "arn:aws:s3:::bucket/*"
  * Click Review Policy, name it and give it a decription before clicking Create Policy
  * Search for the policy created and click Attach Policy
  * Then create a user from the User tab by clicking Add User
  * Give the user a name and allow the user programmatic access
  * Add the user to the group, click end until done
  * Download the CSV file which will contain the access keys, be sure to save the file as it can only be downloaded once
  * For Django to connect to S3, install boto3 and django-storages
  * Also add 'storages' to the installed apps in settings.py
  * Add the 2 AWS keys to the config vars in the Heroku config vars
  * Add the below if statement to settings.py to check that USE_AWS is set to true

if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'eko-shoop'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

## Isues and Bugs
-----------------------------------------------------------------------------------
### Open Issues

I had an issue uploding the categories and database to my website, I was guided by tutor
but we couldn't successfuly manage to do it, so ran out of time and i couldn't finish my 
last project successfuly. I will continue after the recived results to make it 
work properly, and deploy it again.

## Credits & acknowledgements

As always, the advice and support from tutors and slack comunity.

The Code Institute Boutique Ado project walk-through was vital in assisting me in this process.

As always, so much research and troubleshooting was gained by extensive use of [StackOverflow](https://stackoverflow.com/).
=======

## Languages Used 
![Screenshot (376)](https://user-images.githubusercontent.com/66019489/116663782-7ac3c580-a98f-11eb-8118-6687673b2c81.png)
>>>>>>> ad3e28bd4377f962160239c1e2e2884ad2050d27

