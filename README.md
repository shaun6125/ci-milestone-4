# Milestone Project 4

Better U
***

## Table of Contents:
* [What does it do and what does it need to fulfil?](#what-does-it-do-and-what-does-it-need-to-fulfil)
* [Functionality of Project](#functionality-of-project)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Wireframing & Proposed/Implemented Functionality per Page](#5-wireframing--proposedimplemented-functionality-per-page)
* [Technology Used](#technology-used)
* [Database](#database)
* [Features](#features)
    * [Future Features](#future-features)
    * [Defensive Design](#defensive-design)
* [Testing](#testing)
    * [Found Bugs & Fixes](#found-bugs--fixes)    
* [Deployment](#deployment)
* [Credits](#credits)

***

## Welcome to Better U!


***

## What does it do and what does it need to fulfil?
This Milestone project creation is the culmination of learning and study from all modules of the Full Stack Developer Course, culminating in the creation of this Full Stack Framework Django project. This Application will allow an admin to store and manipulate data records and also allow users to create, read, update, delete & purchase memberships and products for this newly created site called, <a href="(https://betteru-7cee832264c3.herokuapp.com/)">Better U</a>.

### Functionality of Project
The application uses Django 3 to encourage rapid development, by following a model-template-view architecture pattern. The project uses Separation of Concern amongst the applications to utilise the Django Framework effectively.

Alongside using Django, sqlite was used in the Project's inception phase as a test database for local testing. Sqlite is self-contained highly reliable, SQL database engine that features all the normal relational database management. Once I was ready I switched to using PostGreSQL (aka Postgres), for my Development Database to ensure that any data entered was visible in my deployed application. Postgres is open source and boosts a fully technical and easy to use Object relational database management system.

Using Django and the above Database methods an administrator for the application (in this case the owner of Better U), has complete access to a completely custom styled Admin dashboard where they can Create, Read, Update and Delete records in the each proposing application model if appropriate. For example: The owner accesses the admin dashboard to update product records, which is a totally separate and completely custom Django application made specifically for this purpose.

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables & secret variables are stored in an env.py file which is then held in a git ignored file to ensure project integrity is held to a high secure present day and project requirements standard.

Please ensure when testing payments in this application to use the Stripe test card numbers available <a href="https://stripe.com/docs/testing#cards">here</a>. Throughout development of the application the card number used by myself and my Peers was:
* Card number: 4242424242424242 (16-digit Card number)
* CVV: Any 3 digit combination.
* Dates: Any future date.

[Back to top](#table-of-contents)

## User Experience:

#### User Stories:
_Generic (Guest/Public) User:_
* As a Generic User, I want to be able to view the site on any device I may have, (mobile/tablet/desktop).
* As a Generic User, I want to have the ability to register to the site.
* As a Generic User, I want to have the ability to research the business and anything associated with same through the application.
* As a Generic User, I want to have the ability to view the established Accessibility Statement & Privacy Policy if any.
* As a Generic User, I want to be able to view available Membership prices.
* As a Generic User, I want to be able to view available Products and prices.
* As a Generic User, I want to be able to get in contact with the business owner through the website.
* As a Generic User, I want to have the ability to see the established social accounts coupled with the business, eg: Facebook, Instagram etc.
* As a Generic User, I want to have information available as to the directions of the business site.

_Registers (Logged in) User:_
* As a Registered User, I want to have the ability to Login to the site via my registered details.
* As a Registered User, I want to have the ability to review membership options and but one.
* As a Registered User, I want to be able to view my Cart and any items I currently have awaiting payment in my Cart.
* As a Registered User, I want to be able to view items currently added to my Cart.
* As a Registered User, I want to have the ability to Logout of the application.

_Application Owner/Administrator User:_
* As a Site Administrator, I want to be able to login to an administration panel.
* As a Site Administrator, I want to have the ability to update site content, such as Product lists, User details, Membership packages etc.
* As the Owner, I want to ensure any user navigating to my site has a positive User experience between content and responsive design to theming.
* As the Owner, I want to show any user navigating to my site the products, services & pricing available.
* As the Owner, I to showcase the new premises location on a map embedded into one of the public pages.

_Developer:_
* As a Developer, I want to demonstrate my growing abilities as a budding Full Stack Software developer during my time on the CI course.
* As a Developer, I want a project that I can proudly showcase to potential employers via my Github Repository.
* As a Developer, I want to create a project that is fully scalable and can be expanded upon as I continue to grow as a developer.

#### Design
I rather enjoy learning new ways to style my projects and I feel more and more that Front End Development and Design is my calling in this profession. 

Keeping to a clean and simple design approach I feel it brings an element of professionalism and doesn't distract the user from the purpose of the site.

##### 1. Font
This project uses the font: (INSERT HERE), this was chosen to reflect the clean and simple approach that the site uses.
  
“Sans-Serif” is used as the default backup font in cases where these fonts have difficulty loading. 

##### 2. Color Scheme

This project as outlined previously uses a minimalistic approach and so utilises a clean simple, black and white scheme, using bootstraps colors "dark, warning, success etc" to highlight certain aspects - such as top of pop ups, incorrect info entered etc. This use of colour in these areas are more to do with the user experience than the site functionality, but help to showcase the thought process that has gone into the small details.


##### 3. Wireframing & Proposed/Implemented Functionality per Page

Wireframing for this project began with Pen and paper as all my projects tend to start, but ultimately Wireframes were created using Balsamiq. Each page or view of the application was rendered as a wireframe in both Small and Medium-Large viewports to show the difference between the aesthetics and showing how the elements per page would react to differing viewport sizes. Each element planned out in this stage has made it into the physical build of the application with not much deviation occurring from the original wireframe plans. these can be seen here: 

<details>
   <summary>Base Template Wireframes</summary>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/home_page.png" alt="home page wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/checkout_page.png" alt="checkout wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/log_in_page.png" alt="log in wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/products_page.png" alt="products wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/profile_page.png" alt="profile wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/register_page.png" alt="register wireframe">
   </p>

   <p align="center">
      <img height="350" src="https://github.com/shaun6125/ci-milestone-4/blob/main/media/subscribe_page.png" alt="subscribe wireframe">
   </p>
   </details>

* Base Template:

   The base.html parent template contained all the default components for each child template to inherit from. All links were provided to third party icon providers, frameworks, stylesheets and script links. The navbar & footer partial components were created in their own html files and inserted into the base.html via the Jinja `include` statement to ensure separation of concern could occur for ease of scalability of the application elements. 
   
   The navbar partial template component contains all primary relevant navigation throughout the site. The navbar uses Bootstrap and the jQuery & Popper.js library to ensure it stays responsive and collapses into a toggler on medium screen sizes or less thus ensuring Mobile first design. The navigational items change depending on whether a user is logged in or not to ensure that the flow of the application is upheld. 
  
  The footer partial template component contains supplementary information pertaining to the website such as  Socials, and some information about myself as the Developer and it's intended use and purpose for `educational purposes`.

  Where appropriate, `block` statements were used for the Page titles, the main inheritance portion in the body and finally for any bespoke scripts that needed to be loaded on specific pages.
  ```html
  {% block content %}
  {& endblock %}
  ```

***

* Home (Index) Page:

   The home (Index) page is the primary landing page and has two call to actions based on whether a User is logged in or not. If they are not logged in the two call to actions are to Register/Login. This is essential to our users as we want to ensure high numbers of first time visitors register for the site and that all recurring registered users have multiple places to login from.
   
   If the user is already logged in the content of the call to action cards change to reflect the logged in status. This time around notifying the user of the Membership page. 
   
   The home page also contains the `_alerts.html` partial to deliver success messaging to the User on Registration, Login & Logout as well as any error messages to be displayed to the user when attempting to access restricted content as an example.
   
***

* Membership Template:

   This template is comprised of some context pertaining to the services offered with membership options, an image to break up the flow of the page a bit. The payment plan detailed on this template can be controlled by the Admin in the Admin panel of the site, and future versions of the site will have multiple price points for subscription, allowing further expansion such as - tailored workout/meal plans based on results from a questionnaire the user takes. Another future option would be for online workout coaching, and based on these various services the subscription rates can be increased, giving the user choice and greater option.
   
   These plans are returned to the template by querying the database table "Membership" and grabbing all the available objects within. 
  
  The wireframe initially had a button to add a plan to the Cart but during application development I utilised the anchor element & empty span method combo as detailed previously to add a cart to the user. Users can only add a plan to a cart if they are logged in, or if they are logged & their cart is empty. This idea behind this is that as these plans are monthly subscription based it was to ensure a user would never buy multiple plans for the forthcoming 30-day period. A user can re-buy a Plan at their leisure right now in separate transactions, with a future implementation being they can only buy one plan in any 30-day period.

***

* Login Template:

   The Login Template is simple, some text, the brand image to break up the page a bit and the login form. The login form itself is generated via a Django Form class. It takes two fields, Username & Password. It checks the username submitted versus the list of Registered users to the site which is held via the PostGres Database, and the password for that user. If both are met entry to the application is permitted. If not, an error alert is displayed detailing that login details were submitted incorrect, and that is produced by passing a message to be stored in the Django Messages Framework and outputting same to the included partial `_alerts.html` on the `login.html` template.
   
   As with the registration page, defensive design elements are achieved in the login template itself using Jinja expression syntax to produce the `_error.html` partial template instead of the default `login.html` template if the expression returns `True` meaning the User is already logged into the application. This step is crucial in maintaining that a user cannot attempt to login multiple times resulting in poor User Experience of the site.

   Lastly, in an attempt to direct users to the appropriate section of the application, included under the form "Submit" button is a link to the Registration page allowing users who have yet to register for the application navigate to same and register.
   
***

* Cart Template:

   The cart template is only accessible to those who have logged in, and shows a user if the cart has something to checkout or not. If it is empty and the user navigates to this template, some helpful short text is displayed to the user detailing same. If the cart has had a plan added to it, then the Cart will display that plan and also a small asterisk symbol will appear in the Navbar alongside the `Cart` Nav-item. For as long as the user is currently logged in, without checking out or clearing the basket, this asterisk symbol will persist, highlighted in yellow across all pages.
   
    If the user wants to checkout, then clicking on the checkout button displayed in the cart card will navigate the user onto same, however, as with the edit-post.html template, a two factor visual cue delete is in play. When a user clicks on `Click here to Clear Cart`, a dialog box slides open with some warning text as to the permanency of this action. If the user wants to continue, a final click on the `Clear` button will clear the cart and navigate the user back to the membership template. As the cart is now clear, the asterisk also disappears from view denoting to the user that their cart is empty.

***

* Checkout Template:

   The checkout template is only accessible to a logged in user, and if a Cart has had an item added to it and then if the user has selected to Checkout that Cart. It will detail the currently selected plan for checkout as a secondary visual inspection for the user to ensure they are getting exactly what they want. And it will also have the Payment form. The Payment details form rendered on the checkout.html template is comprised of two seperate Django forms. One for capturing the Payment details pertaining to the card being used and the other to capture the necessary information for the Order.
   
   There are multiple defensive elements at play for this particular form, from ensuring that the user cannot leave any fields blank to ensuring the correct length of digits is entered for the Credit Card No. & CVV number.
   
   Once a user clicks to buy, and if successful payment is made, the user is redirected back to the Memberships page displaying a success message, and the cart is cleared. If there are any errors detected on submission, the Stripe Error messages will appear detailing the found error, or the normal HTML field warnings will show per field if a field is left blank etc.   

***

Products Template

   The products template is available to all users and displays a set of products that can be broken down into category, sorted and added to the basket. the features on this page for the super user is that they are able to edit and delete directly on the page without having to go to the admin screen.The products are listed in a responsive manner catering to multiple devices and are easily accessed into the product view page for an expansion of detail and the link to add to the bag.

***

Profile Template

   The profile template shows the user a list of what they have previously bought and keeps a record should they need it. here they can change their personal details and their shipping details.

***

* 404 Page Template:

   A simple template that exists in the root `templates` folder and is the automatic return to a User when they attempt to navigate to a Page that does not exist. Contains some context information as to why this page is returning for the User and some directional prompts on how to navigate the site from their. 

***

* 500 Page Template:

   A simple template that exists in the root `templates` folder and is the automatic return to a User when the Server for the application goes down. Contains some context information as to why this page is returning for the User and some directional prompts on how to navigate the site from their. 

***

## Technology Used

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS, JS & Python ~ core languages used to create this multi-page CRUD application.
* <a href="https://www.djangoproject.com/">Django</a> ~ Used as the architectural engine following the model-template-view approach.
* <a href="https://getbootstrap.com/"> Bootstrap Framework</a> ~ Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* Bootstrap's <a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/#js">Imported Javascript & JQuery</a> ~ For the Modal and Responsive Navbar expand & collapse functionality.
* <a href="https://www.heroku.com/">Heroku</a> ~ A cloud platform as a service enabling deployment for this CRUD application.

#### Tools Used:

* <a href="">PostgreSQL</a> ~ A free and open-source relational database management system emphasizing extensibility and technical standards compliance. Designed to handle high range of workloads including Web services with many concurrent users.
* Google Chrome DevTools ~ Used to test the application's functionality, the responsiveness of same, and the CSS visualisation, as well as assisting in such tasks as figuring out the correct style properties to override Bootstraps user agent styling.
* <a href="https://balsamiq.com/">Balsamiq</a> ~ Used for the creation of my pre-build wireframes showing the main elements and differences in size of same through small to large screen sizes.
* <a href="https://validator.w3.org/">W3C HTML Validator</a> & <a href="https://validator.w3.org/">W3C CSS Validator</a> & <a href="https://jshint.com/">JSHint</a> ~ Used to check the validity and efficiency of my code.
* <a href="https://github.com/django-extensions/django-extensions">Django Extensions Plugin</a> ~ For validating my templates for any jinja rendering errors.
* <a href="https://fontawesome.com/icons?d=gallery">Font Awesome Icons</a> ~ For social icons used in Footer and Iconography present throughout site.

## Database

The database used for this Project was Postgres, as an Installed add-on to the deployed Heroku Application. Sqlite3 was used for a little while in the beginning to test the User Authentication, Registration & Login, and for testing the creation of Posts for the Forum. Mid-development I moved to local & deployed testing so Postgres was used from that point on.

When each app and its models were created and implemented, `python manage.py makemigrations` was run in the terminal to create the initial model package and `python manage.py migrate` was then used to apply the model to the database and create the table.

Where possible, first-time-right methodology was approached when creating the models to avoid to many alterations to the models and the database table through multiple `makemigrations` and `migrate` commands.

## Features

This project uses Django 3 in conjunction with Bootstrap 4 to structure and display elements on templates/views to the user. As Django 3 was the most up to date version of the templating framework, it allowed me to broaden my horizons and expand on the learning material of the course. Streamlining such processes as setting up `urlpatterns`. Python 3.8 was also used as the base Python language and as the Project's interpreter in my IDE.

The project is fully responsive and renders as expected on all modern and up to date browser as you will see in the Testing section below.

HTML, CSS and JS were used to implement the Frontend of the project and Django and Postgres was used to create and control the Backend. Stripe and Stripe JS V2 was used to control the credit card payments and Stripe library errors.

The project boasts several key features:
* User Authorisation, Authentication and Logout Features
* CRUD Functionality for Authenticated Users in the Forum and for the Admin of the Site itself with all available tables.
* Aws s3 is used to host static files and media to the deployed site.
* Stripe Integration to allow for e-commerce functionality.
* Fully integrated Navigation dynamically mapped per User type, Public/Authenticated.
* An evolve over time, ever growing functional User Profile to make it easy for Users to see previous orders they've created and access the subscription services.
* A contact form that can be utilised by Public/Authenticated users, which sends an email to the Administrator of the application, notifying them of a new Contact form submission. This is currently wired to come to myself as the developer during Assessment but a copy of a previously submitted contact notification email:

#### Future Features:

Future Features as of right now are:
* Password Reset for Users.
* Show current Membership Plan bought in User Dashboard and display countdown of when renewal of same is needed.
* User Account Update/Delete functionality.
* More subscription services, including the ones intended for this project, but due to time contraints i was unable to build another data base of meal plans and workout plans.
* Questionnaire to encourage sign up rate of subscriptions due to personalisation of the user.
* Video tutorials/ online coaching
* Forum for users to share their experiences and progress
* Map with pin drops to highlight the user's closest gyms.

#### Defensive Design

Defensive design for this application was implemented where possible via function views, form field types, model fields and even in the templates themselves. Throughout the development of the project, all aspects of developed and present Defensive Design elements were tested thoroughly both through local preview and deployed Live Application.

* On registration & login functions, several defensive elements are at play. Between checking the unique fields are in fact unique, to testing if the user is logged in already when attempting to get to both of these views via a browser url injection. Error messaging and the use of the `_alerts.html` partials component work in conjunction with each other to detail to the user the type of error they have.
        
* A Public user can only access the Index, Membership, Login, Registration, Bag, and product pages such. On top of that, the Membership page contains plans that can be added to a cart by a User. In the interest of keeping purchases to only those user who are Authenticated, when a Public user click to add a Plan to a cart they are met with an error detailing they must register & login to perform that action.

   If any user attempts to reach a page that doesn't exist via a browser url or any other means they may have, the application will throw a custom `404.html` template detailing same and how to navigate back to the normal flow of the application.
   
* All form fields existing throughout the site are built with specific field types befitting the data warranted for collection, and even simple validation like min/max lengths or even if the field should be required to be filled or not. And any forms where necessary include Cross-site forgery tokens to safeguard against Cross site forgery attacks. 

## Testing

Testing was done manually as was the case with all my projects throughout my time on the course. Testing was a constant affair during development and was tested on multiple devices at a time from a Samsung ultra s24 Smartphone to my PC as well as a Fire tab 10 Tablet. This ensured that any prevalent bugs at time of development were dealt with in a swift and timely manner and not on an ad-hoc basis at the end of the Development of the Application.

The actual file code validation was done via automatic Validators where possible for example, W3C CSS Validation Service & JSHint etc. Using the HTML Validator allowed me to fully check my templates for any errors, if any existed at time of inspection. Luckily, PyCharm's interpreter will throw an error for most HTML errors too. 

All modern browsers were used to test the responsivity and frontend functionality of the site, as well as the CSS for the application across same. These browsers included Google Chrome, Opera, Microsoft Edge and on Safari via iPad Tablet.

#### Found Bugs & Fixes:

During development and ongoing testing of the Application both via local and deployed links several bugs were found that proved to be a little more than a quick fix. I commited when i ran into a bug and gave a breakdown in the description each time. There are still a few bugs on this project, such as the use of stripe api for subscription payments, as i chose to go about this in a different method than the one used for the main checkout, the webhooks get confused and it can cause issues passing back to the correct page on completion of the subscription payment. 

i had a massive problem when deploying the project and so had to remove alot of the local hosting capability from the pages in order to get it to work on heroku and utalise aws. by rolling back in the branch you will be able to find a working local host version of the site before i began moving over to postgre server. 

aws was another big headache as all instructions failed trying to push static files into the bucket, this caused major issues and lots of code modification to get this working. the fix for this was to push it to staticfiles/static and to push it directly from the shell using the aws cli, this took several attempts to work the code right to achieve. there is still soome bugs here, such as some images dont display in the deployed project.

another bug that i havent had time to fix was the image size, due to the large amount of images used for the products database, i should have been more selective to ensure all images are of the same pixal sizes to ensure a smooth seating on the site, as some of the ones i took from amazon are longer than others it ruins the overall asthetics of the site.

************ ADD BUGS HERE *************************

## Deployment

This full stack application was developed using PyCharm IDE and version controlled via local (git) and online (github) repository technologies. Any secret environment variables were stored in an `env.py` file which was added to a `.gitignore` file keeping those files out of play from the public repo. Those variables detailed in the env.py file were re-enacted over in the Heroku Settings tab for this application under the `Config Vars` section allowing the deployed site to utilise these secret variables.

Branches were used throughout the development of the applications per large feature. These branches were used to develop each feature and then when tested and working, were merged back into the Master branch of the github repo. The branches are visible in the `branches` tab of the public repo dashboard. This ensured that the deployed build of the site was functioning and building and passing in travis from the Master branch while simultaneously allowing me the freedom to implement and test any functionality locally without worrying about a push being made that add an imposing or looming bug to the deployed site.

Deploying this application was achieved by:
* Pushing the code from my IDE to Github via Git.
* Creating an app on Heroku & deploying it from same.
* Adding any secret environment variables to the Config Vars of Heroku App Settings tab and assigning those the requisite secret values held in the env.py for Live Deployment.
* In Heroku 'Deploy tab', deployment method was set to Github with automatic deploys set from the master branch.
* Once the above was done, the app was deployed via this (ADD HEROKU ADDRESS HERE)

To clone the repository:
* Select the Repository from the Github Dashboard.
* Click on the "Clone or download" green button located above and to the right of the File Structure table.
* Click on the "clipboard icon" to the right of the Git URL to copy the web URL of the Clone.
* Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.
* Change the directory to where you want to clone the repository too. 
* Paste the Git URL copied from above and click "Ok". 
* Once open create an env.py file and assign the Database URL, Secret Key, Stripe Publishable & Stripe Secret, and finally Emailing variables. Ensure the `env.py` is living in the root of your project directory and then add it to `.gitignore` to ensure your Secret details aren't exposed.

###### <i>Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 4 Grading!</i>

