# GAMER REVIEWS - README
 
## Purpose of this site/application:
Gamer Reviews is a site dedicated to gamers who would like to post their own reviews of games they have been playing. The user or gamer in this case, can post their own reviews, which are subject to authorisation by the site Admin. Once approved, the user can then view the reviews they have posted to the site and edit or delete them as they wish - provided that they are logged in with their user credentials.
 
<BR>

# FEATURES:
 
## Home Page
The user will be met with the Home Page as shown below. They have either the choice of registering to use the site or to login if they are already a registered user of the site. Conversely, the user can go to the Register page if they are on the Login page.
 
The user is able to view any review they like by clicking the Game Title Text with the gold coloured background.  
<BR>

![image](https://user-images.githubusercontent.com/91907661/182706010-6c982ecc-de34-4ba5-82ca-4e5c878bcc2a.png)
<BR>

![image](https://user-images.githubusercontent.com/91907661/182707384-2797637d-d948-46be-ad47-174270d09394.png)
 
<BR>

## Register and Login
If the user would like to register, they can click the link to do so and then they are taken to the page below. There is also a link on this page to go straight to the Login page.  

<BR>

![image](https://user-images.githubusercontent.com/91907661/182706542-bd14bbe3-90aa-408f-b792-44abed28a999.png)  
 
 
## Create a Review:
Once the user is logged in, they can post a review to be authorised for publishing by the site Admin.
 
They have four fields to complete, 3 of which are mandatory. If these 3 fields - Title, Game, Content are not filled in, an on screen prompt will appear informing the site user.
 
![image](https://user-images.githubusercontent.com/91907661/182711196-7b14e81e-71c3-4c6e-840d-516296e2d734.png)
 
<BR>

## Your Reviews:
Once the user is logged in, they can view the list of reviews they posted, but only those that have been authorised by the site Admin.
 
Importantly, this list only contains the reviews the user themselves have posted. The relevance of this will be explained further on.
 
![image](https://user-images.githubusercontent.com/91907661/182710143-425b5f85-1d85-4e8a-ace4-0c588c3fb7c6.png)
 
<BR>

## Review Detail:
Below is what the user will see when they click on review to see the content.
 
The review title, game and subtitle are displayed along with the date the review was created on.
 
![image](https://user-images.githubusercontent.com/91907661/182712169-71790644-3744-4f08-a56f-ea39dbdb421c.png)
 
 
When the user scrolls down they can see more of the review content itself. They vote to like a review, or click the smiley face if they think its is amusing, or the lightbulb if they think it is interesting or insightful.
 
They can also view any comments made by other users or they can post a comment of their - pending Admin approval.
 
<BR>

![image](https://user-images.githubusercontent.com/91907661/182712764-214a9217-b6af-443d-be3a-ae6eda126a59.png)

<BR>
 
## Edit and Delete Reviews:
From the Your Reviews page - The user can also choose to edit or delete their own reviews. As shown below:
 
![image](https://user-images.githubusercontent.com/91907661/182714588-c94bce8d-75b5-4fcc-b4c2-0459fdcef515.png)
 
If they select edit or delete, they will be taken to the appropriate pages as hown below:
 
![image](https://user-images.githubusercontent.com/91907661/183263526-7a365c86-67ea-4868-8efb-0081ba6313ab.png)

<BR>

![image](https://user-images.githubusercontent.com/91907661/182715380-98a0b481-3920-4082-a745-401108d62b43.png)

<BR>
 
## Edit and Delete Reviews (SAFETY FEATURE):
As mentioned above, it is important that the user who is logged in can only see their own reviews from the Your Reviews, as this gives access to the edit and delete options.

<BR>

# AGILE PLANNING:
I approached the development of this project using agile planning. I broke the development up into 6 Epics and 3 sprints. The plan was to complete the task and user stories within each Epic and about 3 to 4 weeks.

The Kanban board was created using github projects and can be viewed [here](https://github.com/David-Maura-Rodgers/PP4-Gamer-Review/projects/1).

<BR>

# Epics

The following sections will explain the focus of each epic and the order in which they were planned:

**EPIC 1 - Basic Setup**

Install all libraries and dependencies need for the project - gunicorn, dj_database_url, psycopg2, dj3-cloudinary-storage, django-summernote, django-allauth, django-crispy-forms

**EPIC 2 - Database Models and Admin function**

This entailed creating the Review and Comment models. These are the two most important themes of the site and their functionality is key to the purpose of the application.

