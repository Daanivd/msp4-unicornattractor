# UnicornAttractor App  [![Build Status](https://travis-ci.org/Daanivd/msp4-unicornattractor.svg?branch=master)](https://travis-ci.org/Daanivd/msp4-unicornattractor)
The UnicornAttractor app is an app designed by the Unicorn Preservation Society (UPS), to gather more information on sightings and threats facing 
unicorns in the wild. People can download the app and use it to observe the elusive Unicorn (ordinarely not visible to the naked eye, but with this
app you can see them). Sightings are automatically passed on to the UPS, gathered as scientific data. 

Money for UPS is made through contributions. People can either donate, or they can make a contribution to a possible new feature. For new features, a price is set (by the developers) and once this price is met with
the total of contributions to that feature, development of that feature begins. After that the feature is added to the app and can be used freely. 
Users can also suggest new features. If these are approved by the developers they will be added on the website with a set price as a feature people can contribute to

Users are also able to report any bugs with the app on the website in the form of tickets. Users can also upvote specific tickets to indicate they have had this issue as well. This gives developers a good indication on what bugs should be prioritized. 


## UX
- Features: Users can suggest new features. After submitting a feature suggestion, developers will look if it the feature is feasible and how much it would cost to develop (status=awaiting pricing). If the feature is feasible, it will be posted
            on the website as a feature users can contribute to (status=price set). Once the goal price has been obtained through the developers they will start developing it (status=in development), and once it is developed, the feature is added to the app (status=feature added)
            For only front-end users, the features in status 'price is set' are visible as these are the only ones they can contribute to.
- Ticket/Bugs: If a user has found a bug with the app, they can report it on the website. User can submit a form to report the bug, edit it later or others can add to it. they can also check up the particular ticket for updates from the developers.          
- New User: Interested in Unicorns and their plight has found the UPS and their app. That person goes onto the website to see what they can do to help. Here they see they can create
            create a user account. From here they can make contributions in the form of a donation or supporting potential new features. They can also report bugs they have had with the app
            through submitting a ticket.
- User with account: Here the user can be an active member, participating in improving the app by reporting known bugs or suggesting new features. 


# Wireframes
Please see [here](https://github.com/Daanivd/msp4-unicornattractor/blob/master/Wireframes.pdf) to view the wireframes.


## Features

### Existing Features
- Register - Allows a person to register as a user, a user is automatically logged in after registering
- Login - Allows user to login using username or emailaddress, and password
- Reset password - Allows user who have forgotten their password to get an email with a link to reset it and use that link to reset their password.
- Request feature - Allows user to fill in form to request a new feature
- View feature(s) - Allows user to view list of features or one specific feature (only features that funds are being raised for, for development)
- Contribute to new feature - Allows user to contribute to a feature by adding it to their cart and pay by credit card using the Stripe Payment platform. 
- Add to cart - Allows user to add their contribution to their cart.
- Checkout - Allows user to pay for everything in their cart by filling out a form with their address and credit card details. Uses the Stripe Payment platform. 
- Report a bug - Allows user to report a bug he/she experiences with the app in the form of a ticket. 
- View bug(s) (tickets) - See list of bugs or one specific bug users have reported 
- Search bugs (tickets) - The user can type in text in an input field to search bugs
- Edit ticket - A user can alter the exisiting information of an existing ticket. 
- Upvote ticket - If a user has experienced a bug and someone else has already reported it, he/she can upvote the corresponding ticket to indicate this. A user can only do this once per ticket. 

### Django Apps
- Accounts - for users to register and login
- Cart - for users to add items (features awaiting development if sufficient funds have been raised) to their cart 
- Checkout - for users to pay for their items using the Stripe Payment Platform. This also stores orders in the backend once payment has been done. 
- Features - View and suggest (new) features
- Home - Functions to view the home page, including statistics on how often new features are developed and time it takes to resolve bugs.
- Search - Search tickets (reported bugs) based on a query
- Tickets - Create and edit tickets to report on bugs experienced with the apps


### Features Left to Implement
- Strong Customer Authentication (SCA) for Stripe for near future (for payments in Europe)
- Blog with updates on the Unicorn Preservation Society
- More stats on bugs/new features and/or Unicorn sightings
- More options on viewing different kind of features (not just with status=price set)


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


## Testing [![Build Status](https://travis-ci.org/Daanivd/msp4-unicornattractor.svg?branch=master)](https://travis-ci.org/Daanivd/msp4-unicornattractor)
Testing was done manually, by the developer himself and through use of the web app by a third party (person with no developer background), and also using the automatic Django Test Suite.


### Automatic Testing
The plugin **Coverage** was used to 
assess how much of the code was covered. In the end, 98% of the code was covered (964 of 982 statements). Each app folder has its own test files, starting 
with 'test_xxxxx.py' (eg. test_views.py). The continuous integration service provided by Travis also shows all tests were passed.

**Location of test files**
- Accounts App: test_apps.py, test_backends.py, test_forms.py, test_views.py
- Cart App: test_apps.py, test_views.py
- Checkout App: test_apps.py, test_models.py, test_views.py
- Features App: test_apps.py, test_models.py, test_views.py
- Home App: test_apps.py, test_views.py
- Tickets App: test_apps.py, test_models.py, test_views.py

The tests in general go through the steps a user would have to do. A test would have to create instances of users, features and tickets where necessary and then 
subsequently the created user would perform specific actions such as logging in, creating a feature, editing an exisiting ticket or making a payment. Then the test
would see if the correct template, or message was returned. Defensive design was implemented in which a test would purposefully perform an action without logging in,
or filling in a form in a faulty manner, to see if any user-errors would give the correct responses. 

Especially important were the payment tests, using the Stripe-functionality. Using the credit card details and tokens provided by Stripe for testing, as many user scenarios
as possible were tested (as recommended by Stripe). Here is are the steps regarding testing payments as an example:
    1. Create user, log user in and create and save new feature
    2. Add new feature to cart with contribution of eg. 10 euro.
    3. Test the checkout page is loaded properly
    4. Post, to the checkout page, all details necessary (address/payment details, using the Stripe credit card details and Stripe_id according to their documentation on testing,
        and verify payment went through, correct message is shown and the correct page is rendered. 
    5. Post, to the checkout page, all details necessary (address/payment details, using the Stripe credit card detail for a incorrect card, and verify the payment did not go through,
       correct message is shown and the correct page is rendered. 
    6. Post, to the checkout page, with incomplete form (part of address details missing), and check that the page did not go through, correct message is shown and the correct page is rendered. 
        

There were some difficulties with automatic testing, which I think is due to the use of modals for some forms in the web app. A possible solution to this would be to use the plugin 'django-bootstrap-modal-forms',
which I only found out about later. Considering the modal forms in this web app seem to work correctly (also tested through manual testing), this was not implemented in this web app. 
Two other issues I found were with testing the upvoting functionality, and checking if a contribution a feature is added to that features 'totalContributions' field after payment. Upvoting was eventually tested manually,
and the second issue was checked through adding print statements (for 'totalContributions) to the 'for' statement to add to the 'totalContributions field (line 51 in checkout.views). This way I could check if the correct amounts
were added when running the automatic testing, which they were. 


Test files can be performed through the CLI, using the following command:
`coverage run --source='app-name' manage.py test`
A report can be found using:
`coverage report`, and more indepth details of the report can be seen by viewing the index file created by `coverage html`


### Manual Testing
I tried to test as many functions as possible myself, as well as through non-developer, or your ordinary user, people. While browsing the website, functions such as filling out all forms (registration, login, password reset, submit ticket, edit ticket, submit feature, contact-form) correctly and incorrectly 
(to check for proper handling of errors). All other functions such as upvoting a ticket, modal pop-ups and message alerts were tested to ensure proper functioning. Additionally, to test the
login_required decorator,the web app was browed as a logged in user, and a user that hasn't been logged in, to ensure certain functions are not accesible without logging in. 


### Testing different browsers
Correct display of the website was checked in the following browsers:
  - Google Chrome
  - Safari
  - Firefox
  - Opera

### Testing different devices
Testing of display on various device was done using the model options given by the Chrome Devtools, including:
- Desktop experience (desktop computer or laptop)
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- Iphone 5/SE
- Iphone 6/7/8
- Iphone 6/7/8 plus
- Iphone XL
- Ipad
- Ipad Pro


## Deployment
**Deployment through Cloud9 (AWSeducate)**
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

**Deployment through Heroku**
1. Copy Github repository
2. Make sure Procfile and requirements.txt for dependencies are correct.
3. Create new heroku app 
4. Add the Heroku Postgres add-on under 'resources'
5. Set additional Config Var's under settings (see point 4 of 'Deployment through Cloud9)
6. Connect Github repository to Heroku App through 'Deployment Method' in Heroku App Dashboard
7. Deploy Branch through Manual Deploy' in Heroku App Dashboard

**Travis Continuous Testing (if needed, after deployment through Heroku or Cloud9)**
1. Create/log into account on travis-ci.org
2. Link github repository
3. Set environmental variables, but instead of 'DATABASE_URL' variable create TRAVIS variable (empty variable).

##DEVELOPER INSTRUCTIONS 
Unicorn Preservation Society developers working with this system need to regularly check for new features by logging in as an admin. If new features have been suggested, 
developers need to decide on a price. During each status change the 


## Credits
### Content
Text was all written by the developer, Daniel van Duinkerken. 

### Media
The GIF's used as backgrounds on the home page were made by the developer, Daniel van Duinkerken, using two of the images below. 
- [Unicorn Header](http://www.jewishworldreview.com/cols/pruden030119.php3)
- [Unicorn Header2](https://www.sealpress.com/titles/mia-michaels/a-unicorn-in-a-world-of-donkeys/9781580057721/)
- [unicorn header3](https://medium.com/@UnicornAgency/majestic-mondays-feb-5th-2018-e8553b8aba84)
- [forest](https://www.wallpapermaiden.com/wallpaper/25451/forest-trees-mist-sunlight/download/1920x1080)
- [clouds](https://www.psephizo.com/revelation/when-is-god-coming-on-the-clouds/)
- [ocean](http://www.chefsforoceans.com/)
- [unicorn wallpaper](https://www.amazon.co.uk/Rainbow-Unicorn-Wallpaper-Multicoloured-Feature/dp/B076JG8BDL)
- [trees](https://ecobnb.com/blog/trees/)
- [blue mountains mist](https://wallpaperclicker.com/image/Blue-Mountains-Mist-HD-Wallpaper/15347665/)
- [unicornPNG](https://www.pinclipart.com/downpngs/ThJbJ_image-royalty-free-baby-unicorn-clipart-baby-unicorn/)
- [Unicorn logo](https://pngtree.com/so/unicorn)

### Acknowledgements
Various code was inspired by the following links:
- [Change form field name on form](https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name)
- [Django messages Alert box](https://pythonprogramming.net/messages-django-tutorial/)
- [Extending user model with profile](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)
- [Edit two models in one form](https://stackoverflow.com/questions/26184277/edit-two-models-in-one-form)
- [Create profile on registration](https://stackoverflow.com/questions/1909617/django-registration-and-user-profile-creation)
- [IntegerFields with min/max values](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- [Display custom name instead of Object in models](https://stackoverflow.com/questions/33784129/django-display-model-object-in-the-admin-page-instead-of-object-title/33784238)
- [Testing for redirects](https://stackoverflow.com/questions/21215035/django-test-always-returning-301)
- [Django Test Cases](https://micropyramid.com/blog/django-unit-test-cases-with-forms-and-views/)
- [Get verbose version of choice](https://stackoverflow.com/questions/1105638/django-templates-verbose-version-of-a-choice)
- [Forloop counter](https://stackoverflow.com/questions/12145434/how-to-output-loop-counter-in-python-jinja-template)
- [Django divisibleby](https://stackoverflow.com/questions/36185303/how-to-check-whether-a-number-is-divisible-by-another-in-jinja-template-django?rq=1)
- [Django create custom template tag](https://www.codementor.io/hiteshgarg14/creating-custom-template-tags-in-django-application-58wvmqm5f)
- [Django use forloop.counter for index](https://stackoverflow.com/questions/4731572/django-counter-in-loop-to-index-list)
- [Add text to datapoints d3.js](https://www.oipapio.com/question-1046870)
- [Inspiration through similar project (and its github)](https://rick-will-fix-it.herokuapp.com/)
- [parallax-effect](https://www.haleyschafer.com/)
- Many thanks to my mentor Dick v. Vlaanderen for mentor sessions.

