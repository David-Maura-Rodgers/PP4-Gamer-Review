# GAMER REVIEWS - README
 
## Purpose of this site/application:
Gamer Reviews is a site dedicated to gamers who would like to post their own reviews of games they have been playing. The user or gamer in this case, can post their own reviews, which are subject to authorisation by the site Admin. Once approved, the user can then view the reviews they have posted to the site and edit or delete them as they wish - provided that they are logged in with their user credentials.
 
<br>

# FEATURES:
 
## Home Page
The user will be met with the Home Page as shown below. They have either the choice of registering to use the site or to login if they are already a registered user of the site. Conversely, the user can go to the Register page if they are on the Login page.
 
The user is able to view any review they like by clicking the Game Title Text with the gold coloured background. 

<br>

![image](https://user-images.githubusercontent.com/91907661/182706010-6c982ecc-de34-4ba5-82ca-4e5c878bcc2a.png)

<br>

![image](https://user-images.githubusercontent.com/91907661/182707384-2797637d-d948-46be-ad47-174270d09394.png)
 
<br>

## Register and Login
If the user would like to register, they can click the link to do so and then they are taken to the page below. There is also a link on this page to go straight to the Login page.  

<br>

![image](https://user-images.githubusercontent.com/91907661/182706542-bd14bbe3-90aa-408f-b792-44abed28a999.png)  
 
 
## Create a Review:
Once the user is logged in, they can post a review to be authorised for publishing by the site Admin.
 
They have four fields to complete, 3 of which are mandatory. If these 3 fields - Title, Game, Content are not filled in, an on screen prompt will appear informing the site user.
 
![image](https://user-images.githubusercontent.com/91907661/182711196-7b14e81e-71c3-4c6e-840d-516296e2d734.png)
 
<br>

## Your Reviews:
Once the user is logged in, they can view the list of reviews they posted, but only those that have been authorised by the site Admin.
 
Importantly, this list only contains the reviews the user themselves have posted. The relevance of this will be explained further on.
 
![image](https://user-images.githubusercontent.com/91907661/182710143-425b5f85-1d85-4e8a-ace4-0c588c3fb7c6.png)
 
<br>

## Review Detail:
Below is what the user will see when they click on review to see the content.
 
The review title, game and subtitle are displayed along with the date the review was created on.
 
<br>

![image](https://user-images.githubusercontent.com/91907661/183266457-3ba44111-d95d-4c95-8ec0-05365355ff9b.png)

<br>
 
When the user scrolls down they can see more of the review content itself. They vote to like a review, or click the smiley face if they think its is amusing, or the lightbulb if they think it is interesting or insightful.
 
They can also view any comments made by other users or they can post a comment of their - pending Admin approval.
 
<br>

![image](https://user-images.githubusercontent.com/91907661/182712764-214a9217-b6af-443d-be3a-ae6eda126a59.png)

<br>
 
## Edit and Delete Reviews:
From the Your Reviews page - The user can also choose to edit or delete their own reviews. As shown below:
 
![image](https://user-images.githubusercontent.com/91907661/182714588-c94bce8d-75b5-4fcc-b4c2-0459fdcef515.png)
 
If they select edit or delete, they will be taken to the appropriate pages as hown below:
 
![image](https://user-images.githubusercontent.com/91907661/183263526-7a365c86-67ea-4868-8efb-0081ba6313ab.png)

<br>

![image](https://user-images.githubusercontent.com/91907661/182715380-98a0b481-3920-4082-a745-401108d62b43.png)

<br>
 
## Edit and Delete Reviews (SAFETY FEATURE):
As mentioned above, it is important that the user who is logged in can only see their own reviews from the Your Reviews, as this gives access to the edit and delete options.

<br>

![image](https://user-images.githubusercontent.com/91907661/183266381-2b432e01-a024-4ac9-b60e-fadd4a39fd87.png)

<br>

# AGILE PLANNING:
I approached the development of this project using agile planning. I broke the development up into 6 Epics and 3 sprints. The plan was to complete the task and user stories within each Epic and about 3 to 4 weeks.

The Kanban board was created using github projects and can be viewed [here](https://github.com/David-Maura-Rodgers/PP4-Gamer-Review/projects/1).

<br>

# Epics

The following sections will explain the focus of each epic and the order in which they were planned:

<br>

**EPIC 1 - Basic Setup**

Install all libraries and dependencies need for the project - gunicorn, dj_database_url, psycopg2, dj3-cloudinary-storage, django-summernote, django-allauth, django-crispy-forms

<br>

**EPIC 2 - Database Models and Admin function**

This entailed creating the Review and Comment models. These are the two most important themes of the site and their functionality is key to the purpose of the application.

Using the data models and libraries that Django provides, the functionalities covered in this epic are:
- Creating review posts
- Ability to comment on posts
- Link these models to the backend admin function for post and comment approval

<br>

**EPIC 3 - HTML Templates and creation of Views**

This part of the project was dedicated to the creation of the base.html and from there, the index(home) page and review detail page. This also included css styling and site pagination.

Views created:
- Review List (home page)
- Posted Review
- Likes, funny, insightful (voting icons for each post)

<br>

**EPIC 4 - Authorisation Sign Up, Login and Logout**

This Epic required the installation of allauth from the Django framework. This came with Sign Up, Login and Logout - these were customised to suit the style on the app/site. This was sufficient to ensure authorisation criteria for the project.

<br>

**EPIC 5 - User interaction: comments, likes and toasts**

This Epic focused on interactivity and more dynamic parts of the app.

- User can click on icons in review detail page: like, funny, insighful
- icons are only active for authenticated users
- User can leave comments on posts which are sent to site Admin for approval
- Toasts appear after review post, comment post, and all login activity: this is shown to user upon succesful exection of all these function and then fades away after a 2.5 seconds

<br>

**EPIC 6 - Submit, edit and delete Reviews**

This part of the project was the most time consuming but essential components of the site. 3 key features are as follows:

- Once user is logged in and authenticated, they can access the Create a Review page
- User can then use the crispy form to enter the content the wish to appear on their review: this is the sent for approval to site admin
- User can click on Your Reviews link and view only the reviews they have posted: they can then select which they want to Edit and those they want to delete
- Code within the review detail page will only allow logged in user to manipulate their own posts and not those of other users

<br>

**EPIC 7 - Documentation and Deployment**

I have set up whitenoise so that my static files are served in deployment. I have also deployed the project to Heroku so that it is live for users.

### Tasks:
- Complete readme documentation
- Complete testing documentation write up


# WIREFRAMES:
Below I will provide wireframes to illustrate how I thought each page would appear.

All pages will be fully responsive to all pixel sizes and the nav menu will become a burger icon for smaller resolutions

### Home Page:

![image](https://user-images.githubusercontent.com/91907661/183301047-b3610743-15a7-420b-9589-844978434ccd.png)

### Sign Up:

![image](https://user-images.githubusercontent.com/91907661/183301174-616b0d28-12de-44e3-9727-15f44cbe5279.png)

### Sign In:

![image](https://user-images.githubusercontent.com/91907661/183301094-2339cb7c-2844-474b-a9cd-fe39a55d668b.png)

### Review Detail:

![image](https://user-images.githubusercontent.com/91907661/183302034-efbdb447-112d-4c3d-ba3b-98007f293856.png)

### Create A Review:

![image](https://user-images.githubusercontent.com/91907661/183301376-c0cef37d-e0c9-4ce6-83bb-07d4cc67a445.png)

### Edit and Delete Review:

The Edit page will very much resemble the Create A Review page, but the functionality here will be to edit what has been posted by the user previously.

The Delete page functions as you would expect, and will just ask the user to delete the selected review or cancel and go back to previous page.

### Database-Design

The purpose of the database is to make CRUD functionlaity available to the user. The Review model is at the heart of this - it provides the framework from which the user interacts with the site, with all the most relevant aspects related to creating a game review.

The next model is the Comments model, which allows community engagement among registered users to leave comments for one another's review posts.

Users are also able to to leave likes, funny and insightful votes using the icons mentioned previously. These are handled as many to many relationships as many users can leave many votes for many reviews.

Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

![image](https://user-images.githubusercontent.com/91907661/183520884-739a977f-ce2c-4d47-a687-ca820bb9aa5e.png)

<br>

### Security
I have used using the UserPassesTextMixin and LoginRequiredMixin within the Django class based views.
Restricted functionality such as edit and delete functionality listed in the features was secured using this method.

Environment variables are stored in env.py and included in gitignore and these variables and their values are also stored with Heroku Config vars.