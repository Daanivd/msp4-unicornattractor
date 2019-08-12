# UnicornAttractor App  [![Build Status](https://travis-ci.org/Daanivd/msp4-unicornattractor.svg?branch=master)](https://travis-ci.org/Daanivd/msp4-unicornattractor)
The UnicornAttractor app is an app designed by the Unicorn Preservation Society (UPS), to gather more information on sightings and threats facing 
unicorns in the wild. People can download the app and use it to observe the elusive Unicorn (ordinarely not visible to the naked eye, but with this
app you can see them). Sightings are automatically passed on to the UPS, gathered as scientific data. 

Money for UPS is made through contributions. People can either donate, or they can make a contribution to a possible new feature. For new features, a price is set (by the developers) and once this price is met with
the total of contributions to that feature, development of that feature begins. After that the feature is added to the app and can be used freely. 
Users can also suggest new features. If these are approved by the developers they will be added on the website with a set price as a feature people can contribute to

Users are also able to report any bugs with the app on the website in the form of tickets. Users can also upvote specific tickets to indicate they have had this issue as well. This gives developers a good indication on what bugs should be prioritized. 


## UX
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
Register - Allows a person to register as a user, a user is automatically logged in after registering
Login - Allows user to login using username or emailaddress, and password
Reset password - Allows user who have forgotten their password to get an email with a link to reset it
Request feature - Allows user to fill in form to request a new feature
View feature(s) - Allows user to view list of features or one specific feature (only features that funds are being raised for, for development)
Contribute to new feature - Allows user to contribute to a feature by adding it to their cart and pay by credit card using the Stripe Payment platform. 
Add to cart - Allows user to add their contribution to their cart.
Checkout - Allows user to pay for everything in their cart by filling out a form with their address and credit card details. Uses the Stripe Payment platform. 
Report a bug - Allows user to report a bug he/she experiences with the app in the form of a ticket. 
View bug(s) (tickets) - See list of bugs or one specific bug users have reported 
Search bugs (tickets) - The user can type in text in an input field to search bugs
Edit ticket - A user can alter the exisiting information of an existing ticket. 
Upvote ticket - If a user has experienced a bug and someone else has already reported it, he/she can upvote the corresponding ticket to indicate this. 

### Django Apps
Accounts - for users to register and login
Cart - for users to add items (features awaiting development if sufficient funds have been raised) to their cart 
Checkout - for users to pay for their items using the Stripe Payment Platform. This also stores orders in the backend once payment has been done. 
Features - View and suggest (new) features
Home - Functions to view the home page, including statistics on how often new features are developed and time it takes to resolve bugs.
Search - Search tickets (reported bugs) based on a query
Tickets - Create and edit tickets to report on bugs experienced with the apps


### Features Left to Implement
- Strong Customer Authentication (SCA) for Stripe for near future (for payments in Europe)
- Blog with updates on the Unicorn Preservation Society
- More stats on bugs/new features and/or Unicorn sightings.


## Technologies Used
- **HTML**, **CSS** and **Javascript**
    - Base languages used to create website
- [Bootstrap](http://getbootstrap.com)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [JQuery](https://jquery.com)
    - Use **JQuery** for Bootstrap, logic behind the website and in support of EmailJS
- [Python](https://www.python.org)
    - for backend server side processing
    - Please see requirements.txt for dependencies installed
- [Django](https://www.djangoproject.org)
    - Open-source framework for backend web applications based on Python
- [C3.js](https://c3js.org/) 
    -  A D3-based reusable chart library
- [D3.js](https://d3js.org/)
    - JavaScript library for producing dynamic, interactive data visualizations in web browsers.
- [Stripe](https://www.stripe.com)
    - An online payment platform, to enable payments using credit cards on the website. 
- [Travis](https://Travis-ci.org)
    - Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub. 
- [EmailJS](email.js.com)
    - We use EmailJS to link up the modal contact form to an actual e-mail address


## Testing
Testing was done manually, by the developer himself and by a third party, and also for the automatic Django Test Suite.

### Automatic Testing
The plugin **Coverage** was used to 
assess how much of the code was covered. In the end, 98% of the code was covered (964 of 982 statements). Each app folder has its own test files, starting 
with 'test_xxxxx.py' (eg. test_views.py). The continuous integration service provided by Travis also shows all tests were passed:

[![Build Status](https://travis-ci.org/Daanivd/msp4-unicornattractor.svg?branch=master)](https://travis-ci.org/Daanivd/msp4-unicornattractor)

The tests in general go through the steps a user would have to do. A test would have to create instances of users, features and tickets where necessary and then 
subsequently the created user would perform specific actions such as logging in, creating a feature, editing an exisiting ticket or making a payment. Then the test
would see if the correct template, or message was returned. Defensive design was implemented in which a test would purposefully perform an action without logging in,
or filling in a form in a faulty manner, to see if any user-errors would give the correct responses. 

Especially important were the payment tests, using the Stripe-functionality. Using the credit card details and tokens provided by Stripe for testing, as many user scenarios
as possible were tested (as recommended by Stripe). 

Test files can be performed through the CLI, using the following command:
`coverage run --source='app-name' manage.py test`
A report can be found using:
`coverage report`, and more indepth details of the report can be used by viewing the index file created by `coverage html`

### Manual Testing
I tried to test as many functions as possible myself, as well as through non-developer, or your ordinary user, people. Basic functionality such as logging in, resetting the password,
creating a ticket, editing a ticket, upvoting tickets, suggesting a new feature, adding features to the cart and proceeding to checkout. Performing payments through the live site was not
tested as this is not allowed by Stripe. 

### Testing different browsers
Correct display of the website was checked in the following browsers:
  - Google Chrome
  - Safari
  - Firefox
  - Opera

### Testing different devices
Testing of display on various device was done using the model options given by the Chrome Devtools, including iPhone 5,6,7,8,X, iPad, iPad Pro, Google Pixel 2 and Galaxy S5 and desktop experience on computer.



  

  
 




Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.



##Deployment
### Deployment through Cloud9 (AWSeducate)
1. Create a blank workspace in your Cloud9 dashboard.
2. Get all files from github using `git clone https://github.com/Daanivd/msp3` command in the C9 CLI
3. install Python dependies with following command: 'pip3 install -r requirements.txt' (see also step 12)
4. Create 'env.py' for important environmental variables you do not want to make public (eg. push to Github). Environmental variables to put in are 
    SECRET_KEY, EMAIL_ADDRESS and EMAIL_PASSWORD (used for 'reset password' functionality), STRIPE_PUBLISHABLE and STRIPE_SECRET (for Stripe payments),  AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (for using S3 buckets for storing static files and uploaded images), DATABASE_URL (if using a different database from the standard MySQLite, eg. for Heroku)
5. Make migrations using the following command: `python3 manage.py makemigrations` & `python3 manage.py migrate`
6. create super user: `python3 manage.py createsuperuser`
7. Run app with following command: `python3 manage.py runserver $IP:$C9_PORT`.
8. Click on preview >> preview running application and copy link
9. Add link to allowed hosts in settings.py and save
10. Open up Link in browser of choice
11. To access the backend go to your link/admin and login using your superuser credentials
12. *It may be necessary for step 3 to first install the package libpq-dev (`sudo apt-get install libpq-dev`) in order to install psycopg2 

### Deployment through Heroku
1. Copy Github repository
2. Make sure Procfile and requirements.txt for dependencies are correct.
3. Create new heroku app 
4. Add the Heroku Postgres add-on under 'resources'
5. Set additional Config Var's under settings (see point 4 of 'Deployment through Cloud9)
6. Connect Github repository to Heroku App through 'Deployment Method' in Heroku App Dashboard
7. Deploy Branch through Manual Deploy' in Heroku App Dashboard

### Travis Continuous Testing (if needed, after deployment through Heroku or Cloud9)
1. Create/log into account on travis-ci.org
2. Link github repository
3. Set environmental variables, but instead of 'DATABASE_URL' create TRAVIS (empty variable)





## Credits
### Content
Text was all written by the developer, Daniel van Duinkerken. 

### Media
The GIF's used as backgrounds on the home page were made by the developer, Daniel van Duinkerken, using two of the images below. 
[Unicorn Header](http://www.jewishworldreview.com/cols/pruden030119.php3)
[Unicorn Header2](https://www.sealpress.com/titles/mia-michaels/a-unicorn-in-a-world-of-donkeys/9781580057721/)
[unicorn header3](https://medium.com/@UnicornAgency/majestic-mondays-feb-5th-2018-e8553b8aba84)
[forest](https://www.wallpapermaiden.com/wallpaper/25451/forest-trees-mist-sunlight/download/1920x1080)
[clouds](https://www.psephizo.com/revelation/when-is-god-coming-on-the-clouds/)
[ocean](http://www.chefsforoceans.com/)
[unicorn wallpaper](https://www.amazon.co.uk/Rainbow-Unicorn-Wallpaper-Multicoloured-Feature/dp/B076JG8BDL)
[trees](https://ecobnb.com/blog/trees/)
[blue mountains mist](https://wallpaperclicker.com/image/Blue-Mountains-Mist-HD-Wallpaper/15347665/)
[unicornPNG](https://www.pinclipart.com/downpngs/ThJbJ_image-royalty-free-baby-unicorn-clipart-baby-unicorn/)
[Unicorn logo](https://pngtree.com/so/unicorn)

### Acknowledgements
Various code was inspired by the following links:
[IntegerFields with min/max values](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
[Display custom name instead of Object in models](https://stackoverflow.com/questions/33784129/django-display-model-object-in-the-admin-page-instead-of-object-title/33784238)
[Testing for redirects](https://stackoverflow.com/questions/21215035/django-test-always-returning-301)
[Django Test Cases](https://micropyramid.com/blog/django-unit-test-cases-with-forms-and-views/)
[Get verbose version of choice](https://stackoverflow.com/questions/1105638/django-templates-verbose-version-of-a-choice)
[Forloop counter](https://stackoverflow.com/questions/12145434/how-to-output-loop-counter-in-python-jinja-template)
[Django divisibleby](https://stackoverflow.com/questions/36185303/how-to-check-whether-a-number-is-divisible-by-another-in-jinja-template-django?rq=1)
[Django create custom template tag](https://www.codementor.io/hiteshgarg14/creating-custom-template-tags-in-django-application-58wvmqm5f)
[Django use forloop.counter for index](https://stackoverflow.com/questions/4731572/django-counter-in-loop-to-index-list)
[Add text to datapoints d3.js](https://www.oipapio.com/question-1046870)
[Inspiration through similar project](https://rick-will-fix-it.herokuapp.com/features/feature_list/)
[parallax-effect](https://www.haleyschafer.com/)
