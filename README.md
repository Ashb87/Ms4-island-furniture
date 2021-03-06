# Milestone Project Four | Island Furniture

<img src="assets/screenshots/am-i-responsive.png"> 

[View the live project here](https://ms4-island-furniture.herokuapp.com/) <br>

## Overview

<hr>

This website has been created for my Fullstack Framework Milestone 4 project. 
For this project I have decided to build an e-commerce site based around my dads furniture business. With the hope that in the future it can be used as his own website to advertise and sell his products.

## Contents

  * [User Experience](#user-experience-ux)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Wireframes](#wireframes)
      - [Imagery](#imagery)
      - [Color Scheme](#color-scheme)
      - [Typography](#typography)

  * [Structure](#structure)
    - [Data Schema](#data-schema)
    - [Apps and Models](#apps-and-models)
  
  * [Features](#features)
  * [Future Features](#future-features-i-would-like-to-implement)
  
  * [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs-used)
  
  * [Testing](#testing)
  
  * [Deployment](#deployment)

  * [Notes](#notes)
  
  * [Credits](#credits)

## User Experience-(UX)

<hr>

### Target Audience

  The target audience for my site is for anyone that wants to add their own unique bit of furniture to their home. 
  As advertised on the site most of the products can be made to measure and availible in many different colours. 
  Although the furniture wont belong in every home, there is no specific audience as it is mainly down to each individuals personal taste. 

### Business Goals

  1. To have a fully functioning e-commerce site where customers can purchase products direct from the site.
  2. Make profit from their products through the site.
  3. Give a platform to advertise their business and showcase what they do.
  4. Build a larger customer base.
  
### User Stories

   * #### As the site owner or Admin I would like:
     1. the site to be attractive, responsive and easy to navigate for the user.
     2. the purpose of the site to be clear to the user.
     3. to add a product easily on the site.
     4. to edit or delete any of the existing products on the site.
     5. Securely store user information and previous orders.
     6. Keep the site secure by only allowing authorised users to access certain areas of the site.
     7. Allow customers to contact the business through the website.

   * #### As a general visitor I would like:
     1. the site to be clear as to what it is selling/providing.
     2. the site to be attractive and easy to navigate between different pages.
     3. the site to be responsive to whichever device I am using.
     4. to easily search for, view and see information on all of the products for sale.
     5. to be able to make a purchase as a guest.
     6. to view and ammend my bag at any time.
     7. to easily and securely enter my payment details.
     8. email confirmation of my order after completion.
     9. to read any reviews left by other customers.
     10. to be able to contact the company directly through the site.


   * #### As a returning user I would like:
     1. to easily register to the site to have my own profile where my details can be stored.
     2. to easily login and out of my account.
     3. to see details of my previous orders.
     4. email confirmation upon registering an account and placing any orders.
     5. to be able to edit my account details and change my password if I forget it.
     6. to leave reviews on any products I have purchased. 


### Design

<hr>

  When thinking about the design of the site I knew I wanted something fairly neutral and simple in design to help appeal
  to a wider audience, as the site is not targeted towards any specific demographic. With this in mind I chose a colour scheme that I believe contrasts well whilst looking attractive. On some of the pages the layout is broken into different sections with coloured backgrounds to help distinguish between them. For example on the home page the about section is set on a dark green background, with the section directly below placed on a grey background to give a clear separation. As well as on the products detail page there is review section towards the bottom set on a grey background again to help separate the sections and give a bit of conttast to the site. 

  All text on the site is set to a colour that is easily readable against whichever background it sits on, with the hover effect on the links also still readable while giving a clear sign of it being clickable.

* ### Wireframes

  To create my wireframes I used balsamiq. I have done a design for both large and smaller screens to show how the layout of the site will change accordingly with different screen sizes. The links to the wireframes are below. <br>
  * [Large screens](https://github.com/Ashb87/Ms4-island-furniture/blob/main/assets/wireframes/island-furniture-lg-wireframe.png)
  * [Smaller screens](https://github.com/Ashb87/Ms4-island-furniture/blob/main/assets/wireframes/island-furniture-small-wireframe.png) 

  Most of the design of my site has been kept similar to those in the wireframes. As the design went on and with speaking to my mentor, together we made a few adjustments. Mainly this was positioning of buttons and links. For example on my basket/bag page on the wireframe I have the remove item button below the product image. My mentor advised that this should be a smaller link and off to the side so that the customer isn't drawn to the idea of removing their products.
  I also removed the total cost for each item and decided that just having the total at the bottom of the page was enough.
  For the navbar, in my wireframes I had kept all the product options in one click down button, however when playing with the design I much preferred the look of having the options displayed on the main navbar.
  I also decided to add more information to my footer, after browsing other sites offering similar products I found that most have links to their contact and/or faq pages. So I added these and a business address just to balance the footer out and make it look more professional. 

* ### Imagery

  For the imagery of this site I have used a lot of my dads own stock photos as I wanted to make the site as genuine to his business as I could. However as he is not much of a photographer and clearly doesn't have the best camera, some of the photos aren't as good quality as I would like them to be. Because of this I also wanted to add a few products with better images I got online. I also found that due to the way some of the photos are taken and different styles of furniture, a lot of the photos were different sizes and some were portrait while others were landscape. To get around the issue I decided to set a height for the images on the products page so that when browsing the products, all the images look uniform and helps keep the page looking smarter. Although this does mean thaty for some products part of the image is cut off. Then when a product is clicked and you are taken to the product details page the photo is then shown as intended. <br>
  If a product is added with no image then a default image will be placed there instead.<br>
  For the hero image on the home page I have used a photo I took myself from where Island Furniture sells some of their products, using a fade in effect when the page is refreshed. I have also used an image on the about section of a picture taken in West Mersea where the business is based. This is to add to the design of the home page and promote where they are from. 

* ### Colour Scheme

  For the colours on this project I knew I didn't want anything to bold or colourful but also wanted it to be attractive and not boring. While at the same time making sure they contrast together nicely. After playing about with a few colours on my navbar I decided to look at [coolors.co](https://coolors.co/) to get some more ideas. When using the generator I had an idea of a dark green so when one came up that I liked I applied it to my navbar. I then added a gold colour to it for the links. I again changed my mind and decied I wanted the navbar and footer to be a dark grey, but still really liked the green. So I have used it throughout the site on different elements. It can be found as a background colour on my home page. It is the cololur to all my buttons and also used on the faq section. I then changed the bottom links of my navbar to white to contrast nicely with the dark grey and also not have to much of the gold. <br>
  Throughout the site each page has it's own heading and for this I have used the same gold colour as well as for all my hr rules. The majority of the site is set on a white background as I think it gives a clean look with all the elements contrasting nicely against it.<br>
  For two other sections, (review section and colours used section) I have used a much lighter grey. I did this to break the site up a little bit and a bit of contrast. <br>
  Overall I think the colours work well together and give an attractive finish that should appeal to most users.<br>
  The colours used can be viewed below.

  <img src="assets/screenshots/colours-used.png" width="450" height="150"> 
  <br>

* ### Typography

  I have used two fonts across the site, both imported from google fonts. <br>
  They are **Handlee** and **Montserrat Alternates** <br>
  The Handlee font has been used for my headings and home link text in the navbar. I chose this because I think it's an attractive font with a bit of character to it and so stands out well. The Montserrat Alterantes font has been used for all other text on the site. I chose this because it's a bit different to standard fonts but is still esily readable and works well with the look of the site and both fonts compliment each other well.

## Structure

### Data schema

I have created a database schema for the project using [dbdiagram](https://dbdiagram.io/home). See the image below

<img src="assets/screenshots/db-diagram.png" width="500" height="250">
<br>

For the data schema I have made tables consisting of the different models I have across the project apps. I have then linked the models together where they relate to each other. For example the user profile is linked to the reviews, contact and checkout models. Linked together by the users name. The order model and order_line_item model are linked by total cost of the product  which in turn results in a grand total for the checkout process. Products and categories are linked together by the product name which in turn are linked again to the reviews model, checkout and order_line_item.

### Apps and Models

#### Checkout App
  
- Order Model
  - Holds information for each order which is created when a user completes the checkout process.

-  OrderLineItem Model
  - Contains information for each product added to the bag.

#### Contact App

- Contact Model
  - Holds information for each contact message sent to admin

#### Products App

- Category Model 
  - Stores the product categories

- Products Model
  - Stores information for individual products

- ProductReview Model
  - Stores the reviews added by users to products

#### Profiles App

- UserProfile Model
  - This model securely stores information on each registered user. Information is pulled from this Model to pre-fill the personal information form on the checkout page if the user is logged in, and has information saved.

Models I have added myself for the project can be found in the products app (ProductReview) and the contact app (Contact).

### Adding Categories and Products

- When I first started building my project I knew that I wanted to use a lot of images of my dads own furniture to make the site. Doing this I knew I would need to manually add in all the categories and products myself as I wasn't going to be using any pre existing databases. With the advice from Code Institute I added only a few items to the categories and products files within my fixtures folder. This was enough to work with and help design the layout of the site to see how the products pages would display. 
- Once I had deployed the site and installed the postgres database I was then able to add a lot more products and images by using the product management form. This was a great way for me to test all the functionality of adding, editing and deleting products to and from the database. 

## Features

<hr>

  * ### Across all pages

    * Responsiveness. The site is responsive to all screen sizes for every page no matter what device it is being viewd on.
    * Navbar. The navbar is consistent througout the site and changes depending on the scren size. The home link and bag link remain in the header no matter what size screen. Wheres all the other links are hidden on smaller screens and accessible through the burger icon with a dropdown menu.
    * Footer. The content of the footer remains the same for all screen sizes with links to the contact page, faqs and social media sites. For smaller screens the elements stack on top of each other rather than being side by side with padding and margin added where needed to adapt to the different layout.
    * Messages/Toasts. Messages and Toasts are used when executing certain actions on the site, such as logging in and out, adding and removing products from the shopping bag, completing a transaction, and for admin actions too like adding and editing products.
    * Buttons. The buttons used on the site remain the same througout. I decided to keep all my buttons the same to give a consistent look. All the buttons are clear in their intentions so wont add any confusion to thet user by looking the same. 

  * ### Home Page

    * A hero image with a fade in effect to showcase some of the items for sale.
    * A carousel that showcases some of the furniture that is availble to buy in the products section. 
    * An about us section to give a brief history of the company as well as what they offer today.
    * A section to promote the colours and paints used on the products that the customers can chose when purchasing an item.

  * ### Products Page

    * A drop down bar allowing the user to chose in what order the products are displayed. For example by price or category.
    * An image for each product to show what is on offer which links to the products detail page.
    * A small bit of information for each product showing its name, price and which category it belongs to.
    * A back to top button to take the user to the top of the page.
    * For admin users there is the added option to edit and delete a product.

  * ### Product details Page 
    
    * A larger image of the product selected.
    * A description of the product including the products dimensions.
    * A drop down box allowing the customer to chose a colour for their product.
    * A quantity selector box to add one or more of the item to their bag.
    * A button to add their selections to their bag.
    * A button to take them back to the products page.
    * Breadcrumb links below the header to navigate back to all products or the current category they are viewing.
    * Reviews for the product if any have been added.
    * The option to add a review if the user is logged in.
    * Add and edit product links for admin user only.

  * ### Shopping bag page

    * A summary of each item added to the bag with a picture, item name and colour chosen. Price of that item and a selector box giving the user the option to add another of the same product and then update the total.
    * A summary giving the total bag cost, delivery cost and then the total cost of the two combined.
    * A button to take the user back to the products to carry on shopping.
    * A button to take the user to the checkout page.

  * ### Checkout page

    * An order summary showing the user everything they have in their bag and the total cost of their purchase.
    * Delivery form that allows the user to input their delivery information
    * An option for users with a profile to save their information to their profile.
    * Stripe input element where users can input their card details to pay for the products.
    * A button link to take them back to the bag page incase they want to adjust anything.
    * A *complete order* button that allows the user to process their order and complete their purchase.
    * Text warning alerting the user that payment WILL be taken upon completing their order
    * A confirmation email will be sent to the user with information about their recent purchase.

  * ### Checkout success / Order history page

    * A total summary of the users order including price, order number, order date and delivery information.
    * Button at the bottom of the screen showing an option to either navigate back to products page or back to the users profile depending on whether the user completed a new order, or viewed a previous order from the profile screen.

  * ### Sign in / Sign up page

    * On the sign up page the user can register an account by providing an email address, username and password. All of these fields are required so will show an error if the information is eneterd incorrectly.
    * On the login page the user can login to their account by entering their username or email address as well as their password.
    * on the login page the user has link to click if they have forgotten their password where they are then directed to a different page and asked to enter their email address. They will then recieve an email giving them steps to reset their password.
    * On the login page they also have the option to click the remember me button so they wont have to enter their details everytime.

  * ### Profile page

    * Shows the user all their default delivery details and allows them to update it.
    * Shows all previous orders from their account with a link to click on previous order numbers which takes them to the history page for that specific order.
    * A button link allowing the user to change their password.

  * ### Add / Edit products page - Admin only -

    * Add product allows the admin to add a new product to the site. They can enter the category, name, description, price, whehter it can be painted and the otion to add an image.
    * Buttons to either cancel or complete the action.
    * On the edit page the item they are editing is autofilled with all its existing information. The admin then has the option to edit any of the fields they require.
    * Buttons to either cancel or confirm updating the product.

  * ### Contact & FAQ page

    * The page is split down the middle for larger screes with a contact form on the left and the FAQs down the right.
    * The contact form allows a user to add their name, email address and a message to send to the email address linked to the site. When a message is sent they will recieve a confirmation email to say there message has been recieved.
    * FAQs displayed in an accordion, so a user can click on any question and the information relating to that question will dropdown below it. 

## Future Features I would like to implement

<hr>

  * ### Adding reviews
  
    * Although the site already has a reviews section that is only availible to users with a profile, I would like to take this further and add a function that only allows a user to leave a review for an item they have already purchased.
  
  * ### Size options

    * I would like each product to have different sizes availible and for the price to change accordingly.

  * ### Average rating

    * I would like for the rating left by the users to review to return an average rating for that specific item.

  * ### Pagination

    * Pagination on products would allow for only a set number of products to show per page. Although my site doesn't have a large number of products, for e-commerce sites with lots of products, it would not be viable to a user to have to take the time to continuously scroll down without knowing when the product list will end.

  * ### Social media logins

    * Logging in through social media sites is an increasingly popular feature on many sites, implementing this would be good for users to make the logging in process quicker and smoother.

## Technologies Used

<hr>

### Languages

  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) <br>
  * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) <br>
  * [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) <br>
  * [Python](https://www.python.org/)

### Frameworks, Libraries and Programs Used

  * [Django](https://www.djangoproject.com/) <br>
     Django was used as the main framework to build the site
  * [Bootstrap](https://getbootstrap.com/)<br>
     Bootstrap was used to help build the structure of the website and add responsiveness across different screen sizes.
     It also supplied a lot of the styling like paddings and margin as well as built in components such as the modal.
  * [Balsamiq](https://balsamiq.com/) <br>
     I used balsamiq to design and draw up my wireframes before starting the project.
  * [Google Fonts](https://fonts.google.com/) <br>
     Google fonts was used throughout the project to import my selected fonts.
  * [Font Awesome](https://fontawesome.com/) <br>
     Font awesome was used to add all icons used on the site.
  * [Gitpod](https://www.gitpod.io/) <br>
     Gitpod was the text editor I used for this project.
  * [Git](https://git-scm.com/) <br>
     Git is used as version control software to add, commit and push code to my GitHub repository where the code is then stored.
  * [GitHub](https://github.com/) <br>
     I have used GitHub as a remote repository to push and store the committed changes to my project from Git.
  * [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) <br>
     I have used Google chromes built in developer tools to help with the styling of the site, selecting colors and to help fix any bugs I found.
  * [Heroku](https://id.heroku.com) <br>
     Heroku has been used to deploy my live site.
  * [SQlite3](https://www.sqlite.org/index.html) <br>
     Used as the development database
  * [PostgreSQ](https://www.postgresql.org/) <br>
     Used as the database for the deployed site.
  * [Stripe](https://stripe.com/gb) <br>
     Used to handle card payments through the site.
  * [AWS S3](https://aws.amazon.com/) <br>
     Amazon Web Services, used for hosting images and static files

## Testing 

Find the full Testing Document [here!](TESTING.md)

## Deployment

### Github

### Initial creation
I created the repository using the following steps:
 1. Logging into my [GitHub](https://github.com/Ashb87) account and clickng the green button near the top left of the page displaying the text **NEW.**
 2. This took me to a page with the option to create a new repository. Under *repository template* I clicked on the *code institute* template.
 I chose a name for the repository suitable for the project and then clicked the *create repository* button.
 3. I opened the new repository and clicked the green *gitpod* button to create a new workplace in Gitpod for writing and editing my code to develop the site.

 ### Forking the GitHub Repository
Forking a repository enables us to make a copy of the original repository on our GitHub account so we can view it and make changes with out affecting the original work.
This is done using the following steps:
 1. Log in to [GitHub](https://github.com/Ashb87/Ms3-Movie-Review) account and select the relevant repository.
 2. To the top right of the page there are three the buttons, the furthest right says **Fork.** Click on this button.
 3. A copy of the original repository will now be in your account.

 ### Making a Clone
To make a clone of my project use the following steps:
 1. Go to my [account](https://github.com/Ashb87/Ms4-island-furniture) and locate relevant repository.
 2. Next to the green **Gitpod** button, click on **CODE.**
 3. Click on **Download Zip.**
 4. Once dowloaded, you can extract the zip file's contents and save to a desktop and run the website locally.

 ### Running the server locally
To run and view the project for development purposes, DEBUG needs to be set to true in `seetings.py`. This will help determine any bugs or errors found by django in the code. Then when wanting to view the site you will need to type `python3 manage.py runserver` in the terminal. This will allow you open the port 8000 and view the site. When the server is stopped the site will no longer be running. 

## Heroku

1.	Go to [Heroku](https://www.heroku.com) and create an account if you don't already have one. 
2.	Once logged in create a new app, making sure to use only lower case letters and no spaces for the name, choose the region closest to you and select ???Create App???
3.	When the app has been created, click on the ???Resources??? tab to add the Postgres database
4. Type in ???Heroku Postgres??? and select it from the dropdown list. This will automatically create a DATABASE_URL variable in Heroku Config Vars which can be found by clicking on the ???Settings??? tab, and clicking the ???Reveal Config Vars??? button
5. Now head over to the ???Deployment??? tab to set automatic deployments when pushing to GitHub. Set the deployment method to ???GitHub??? and search for your repository, then Click ???Connect???, and then ???Enable automatic deployments???
6. Back in your IDE, install both `dj_database_url` and `psycopg2-binary` using `pip 3 install 'app name'` in order to use Heroku Postgres. Then freeze the requiremtns with the command `pip3 freeze > requirements.txt`.
7. In your `settings.py` file, comment out the existing sqlite DATABASES and add the following code;

```
DATABASES = {
	???default??? = dj_database_url.parse(???database_url')
}
```

8. In the terminal login to your heroku account by typing `heroku login ???i`
9. Once logged in, you will need to run migrations to migrate your models to Postgres;
  - In the terminal, enter `heroku run python3 manage.py migrate --plan` to show what will be migrated
  - If you are happy with the migrations, enter `heroku run python3 manage.py migrate`
10.	If you are using a JSON file with product information stored, you will need to load these to Heroku also by entering the following into your terminal;

`heroku run python3 manage.py loaddata categories`

`heroku run python3 manage.py loaddata products`

11. You will then need to create a super user so you can access the admin page by entering `python3 manage.py createsuperuser` and folllowing the commands in the terminal. 
12. Next install `gunicorn` in the terminal and freeze the requirements by entering `pip3 freeze > requirements.txt` in your terminal. 
13. Create a `procfile` by entering the following into your terminal;

`web: gunicorn name_of_your_app.wsgi:application`

14. Before committing and pushing these changes to GitHub, make sure you uncomment your `DATABASES` code in `settings.py` and amend your code to ensure your database url doesn???t get accidentally committed to GitHub!
???	Once this is done, `add`, `commit` and `push` your changes to GitHub


Make sure that all of your configuration variables are up to date on Heroku. You can do this by going in to the settings tab and clicking on Reveal Config Vars. This is the list of variables you will need, these variables also include ones for AWS which the following section will go over.

| Key                   | Value                    |
| --------------------- |--------------------------|
| AWS_ACCESS_KEY_ID     | `aws_access_key`         |
| AWS_SECRET_ACCESS_KEY | `aws_secret_access_key`  |
| DATABASE_URL          | `auto-generated`         |
| EMAIL_HOST_PASS       | `email_key`              |
| EMAIL_HOST_USER       | `your_email`             |
| SECRET_KEY            | `secret_key`             |
| STRIPE_PUBLIC_KEY     | `your_stripe_public_key` |
| STRIPE_SECRET_KEY     | `your_stripe_secret_key` |
| STRIPE_WH_SECRET      | `stripe_webhook_key`     |
| USE_AWS               | `True`                   |


## AWS

### Setting up

1. Go to AWS and set up an account if you don???t already have one. You will be asked to enter credit/debit card details, but if using the free tier you should not be charged.  
2. Log in to AWS, and navigate to S3. You can search for ???S3??? in the search bar at the top of the screen. 
3. Create a new bucket by clicking on the orange ???Create Bucket??? button. 
4. Make sure that your bucket name matches the name of your app on Heroku, and that you select the region closest to you. 
5. Scroll down to ???Block Public Access settings for this bucket??? and uncheck the checked box. Confirm that you are happy to do this, then scroll to the bottom of the page and click the orange ???Create Bucket??? button. You will be taken to your bucket dashboard, and from here, you will need to make some amendments to your bucket. 

### Bucket Properties
1. Click on the ???Properties??? tab and scroll down to the bottom of the page, where you will find a ???Static website hosting??? section. Click on the edit button.
2. In the top section select ???Enable??? to enable static website hosting. 
3. The next section is ???Hosting Type???. Select ???Host a static website??? and scroll down to the ???Index Document??? inputs. 
4. It will first ask you to specify the home or default page, which is `index.html`
5. It will then give you the option of entering an error link for if an error occurs. In the input, type `error.html`
6. Leave the Redirection rules blank, and click the orange ???Save Changes???. 

### Setting Permissions
1. Next, click on the ???Permissions??? tab, scroll to the bottom of the page and click edit in the ???Cross-origin resource sharing (CORS)??? section. 
2. Add in the following code, 
```
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
```
3. Click on the orange ???Save Changes??? button and navigate to the ???Bucket Policy??? section.

### Generating A Bucket Policy

1. Click on the ???Policy Generator??? button. This will open a new window. 
2. Next you will need to select ???S3 Bucket Policy from the dropdown list.
3. Then, you will need the following options set;
    - Effect ??? Allow
    - Principle - *
    - Actions ??? GetObject, GetObjectAcl, PutObject, PutObjectAcl and DeleteObject
    - Amazon Resource Name (ARN) ??? This will be found on the previous page, under ???Bucket ARN???. Copy this and paste it into this box
4. After these have been entered, click ???Add Statement??? then ???Generate Policy???.
5. Copy the policy into the bucket policy editor, adding `/*` onto the end, the click ???Save Changes???.

### IAM - Creating A Group and Policy

1. Next, search for IAM in the search bar at the top, and click on it to set up a group policy.
2. Under ???Access Management??? on the left hand side, click on ???User Groups??? and create a new group.
3. Give the group a name and click ???Create Group???. 
4. This will take you back to the IAM dashboard. Go back to the ???Access Management??? section on the left hand side, and click on ???Policies???. 
5. Click ???Create Policy??? and head over to the JSON tab, and select ???Import Managed Policy???. 
6. Search for and click on ???AmazonS3FullAccess??? then ???Import???.
7. Copy your ARN and place it in the code so that it looks like the below;
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR-ARN",
                "arn:aws:s3:::YOUR-ARN/*"
            ]
        }
    ]
}
```
8. Click on ???Next: Tags???, ???Next: Review???, put in a name and click on ???Create Policy???. 

### Group Policy

1. You will then need to attatch a policy to the Group created.
2. Go to ???User Groups??? under ???Access Management??? click on your newly created group and go over to the ???Permissions??? tab.
3. Click on the ???Add Permissions??? button, and then select ???Attach Policy???.
4. Click on the checkbox next to the policy you have just created, then click ???Add Permissions???.

### IAM - Create User

1. Back at the IAM dashboard, click on ???Users???, then ???Add User???.
2. Choose a name and tick the checkbox to give the user access, then click ???Next: Permissions???.
3. Select the group to put the user in and keep clicking the next buttons until the very end and click ???Create user???.
4. Click on ???Download .csv??? file and save this somewhere you remember, as you will not have access to this page again! This file will contain information such as your access codes.

### Saving Images To S3 Bucket
If you want to save images to your S3 bucket, you will need to do the following;
1. Go back to the S3 dashboard, and click on your bucket. 
2. Click ???Create Folder???, call it ???media??? and confirm with the second ???Create Folder??? button.
3. When you are in this folder, click ???Upload???, then ???Add Files??? or ???Add Folder???, then ???Upload???.

## Notes

When I first deployed to Heroku and set the secret key to `SECRET_KEY = os.environ.get('SECRET_KEY', '')` when trying to run the server locally to view the site I would get a message in the terminal telling me I needed to have the secret key in my settings for it to run. After speaking with a tutor she noticed that I had my secret key in my settings and advised that I set it as a variable in my gitpod settings instead so I wouldnt need it displayed in my settings. So I used the django secret key generator to get a new one, added that to the variables in my gitpod settings and deleted the one out of my `seetings.py` to make sure it wasn't being deployed to my github repository. 


## Credits

### Code and Content
- [Bootstrap](https://getbootstrap.com/) was used for the structure and layout of the site.
- [Stackoverflow](https://stackoverflow.com/) was used to help find solutions to the issues I had whilst building my project.
- [Code Institute](https://codeinstitute.net/) boutique ado project was used a lot throughout the project to help with functionality across the site.
- [Youtube](https://www.youtube.com/) was used to help put together my contact model and views.
These were:
  - [B learning club](https://www.youtube.com/watch?v=lSgRWA4PMt4&t=477s)
  - [Hacker shack](https://www.youtube.com/watch?v=94ylwr2r3Hs&t=831s)
  - [Dennis Ivy](https://www.youtube.com/watch?v=gpTrmDpadZY)


### Acknowledgements
- The **Mini Feb 2021** team on slack for all the feedback and support given to each other.
- Sunny Hebbar for all his useful feedback and support he has offered me thoughout the whole course.
- The Code Institute slack community for all the helpful hints and tips.
- All the tutors at Code Institute who helped me fix issues along the way. You saved me from a few breakdowns!!
- Friends and Family who have taken their time to offer advice and feedback duirng the devolopment of my project.
- [w3schools](https://www.w3schools.com/) for all its useful information in helping to build my project.

[Back to top](#overview)