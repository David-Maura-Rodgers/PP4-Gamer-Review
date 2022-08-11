# GAMER REVIEWS - README
 
## PURPOSE OF THIS SITE:
Gamer Reviews is a site dedicated to gamers who would like to post their own reviews of games they have been playing. The user or gamer in this case, can post their own reviews, which are subject to authorisation by the Site Admin. Once approved, the user can then view the reviews they have posted to the site and edit or delete them as they wish - provided that they are logged in with their user credentials.
 
<br>
 
## SUPERUSER SITE ADMIN FUNCTION:
This site uses Django's Admin functionality for content moderation control. The site has a Superuser with their own login credentials.
 
This enables the Site Admin to be able to go to the server side of the application to authorise user reviews and comments.
 
The Admin panel can be accessed simply from the home page. You can navigate to it by clicking in the URL bar, hit / (forward slash) on keyboard and type admin. Like so: **/admin** and hit **enter**
 
**NOTE:**
- During the development of this project, I posted several test review posts. This was done to test the functionality of the **Create Review**, **Edit Review** and **Delete Review** functions.
- You will also find some comments visible in the review detail, this was also done to test comment functionality.
- **(All of the review content is simply just placeholder text used to test the functionality of content display for site)**
- Site user can use all the functions on the front end providing they are the author of the review post.
- Site Admin can do all of the above from the admin panel.
 
<br>
 
# FEATURES:
 
## Home Page
The user will be met with the Home Page as shown below. They have either the choice of registering to use the site or to login if they are already a registered user of the site. Conversely, the user can go to the Register page if they are on the Login page.
 
The user is able to view any review they like by clicking the Game Title Text with the gold coloured background.
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184168917-c3118b43-f99f-433e-b3dc-84611833e738.png)
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184169802-9964464f-629e-4e56-b05a-de9e65a0bcff.png)
 
<br>
 
## Register and Login
If the user would like to register, they can click the link to do so and then they are taken to the page below. There is also a link on this page to go straight to the Login page.  
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184170135-64e83c21-c1ab-480a-974e-f3c8cb482242.png)  
 
 
## Create a Review:
Once the user is logged in, they can post a review to be authorised for publishing by the site Admin.
 
They have four fields to complete, 3 of which are mandatory. If these 3 fields - Title, Game, Content are not filled in, an on screen prompt will appear informing the site user.
 
![image](https://user-images.githubusercontent.com/91907661/184175307-18f31d5a-eef9-4582-8de8-945b9ad22208.png)
 
<br>
 
## Your Reviews:
Once the user is logged in, they can view the list of reviews they posted, but only those that have been authorised by the site Admin.
 
Importantly, this list only contains the reviews the user themselves have posted. The relevance of this will be explained further on.
 
![image](https://user-images.githubusercontent.com/91907661/184170861-82080a21-ed20-45bc-b076-7b22a3b656d7.png)
 
<br>
 
## Review Detail:
Below is what the user will see when they click on review to see the content.
 
The review title, game and subtitle are displayed along with the date the review was created on.
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184171453-321885d0-e89d-44e1-a5d8-70892dc9bb5f.png)
 
<br>
 
When the user scrolls down they can see more of the review content itself. They vote to like a review, or click the smiley face if they think it is amusing, or the lightbulb if they think it is interesting or insightful.
 
They can also view any comments made by other users or they can post a comment of their - pending Admin approval.
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184171732-50beaa13-91b4-442f-9817-df8e4df7d13d.png)
 
<br>
 
## Edit and Delete Reviews:
From the Your Reviews page - The user can also choose to edit or delete their own reviews. As shown below:
 
![image](https://user-images.githubusercontent.com/91907661/184172205-01aa3b3d-6cb2-437f-af73-31fc9ebd3e75.png)
 
If they select edit or delete, they will be taken to the appropriate pages as shown below:
 
![image](https://user-images.githubusercontent.com/91907661/184172672-04e7bdd7-9a72-45fd-a80b-d8bb3cab85bd.png)
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184173104-b59f5b2a-248f-4556-b8bd-547fc92e5d2f.png)
 
<br>
 
## Edit and Delete Reviews (SAFETY FEATURE):
As mentioned above, it is important that the user who is logged in can only see their own reviews from the Your Reviews, as this gives access to the edit and delete options.
 
<br>
 
![image](https://user-images.githubusercontent.com/91907661/184173537-366e0dba-f8b7-405f-b85e-f8d521958275.png)
 
<br>
 
# AGILE PLANNING:
I approached the development of this project using agile planning. I broke the development up into 6 Epics and 3 sprints. The plan was to complete the task and user stories within each Epic and about 3 to 4 weeks.
 
The Kanban board was created using github projects and can be viewed [here](https://github.com/David-Maura-Rodgers/PP4-Gamer-Review/projects/1).
 
<br>
 
# Epics
 
The following sections will explain the focus of each epic and the order in which they were planned:
 
<br>
 
**EPIC 1 - Basic Setup**
 
Install all libraries and dependencies need for the project - gunicorn, dj_database_url, psycopg2, django-summernote, django-allauth, django-crispy-forms
 
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
 
- User can click on icons in review detail page: like, funny, insightful
- icons are only active for authenticated users
- User can leave comments on posts which are sent to site Admin for approval
- Toasts appear after review post, comment post, and all login activity: this is shown to user upon successful execution of all these function and then fades away after a 2.5 seconds
 
<br>
 
**EPIC 6 - Submit, Edit and Delete Reviews**
 
This part of the project was the most time consuming but essential componentS of the site. 3 key features are as follows:
 
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
 
<br>
 
# WIREFRAMES:
Below I will provide wireframes to illustrate how I thought each page would appear. These wireframes were created using [Figma](https://www.figma.com/)
 
All pages will be fully responsive to all pixel sizes and the nav menu will become a burger icon for smaller resolutions
 
<br>
 
### Home Page:
 
![image](https://user-images.githubusercontent.com/91907661/183301047-b3610743-15a7-420b-9589-844978434ccd.png)
 
<br>
 
### Sign Up:
 
![image](https://user-images.githubusercontent.com/91907661/183301174-616b0d28-12de-44e3-9727-15f44cbe5279.png)
 
<br>
 
### Sign In:
 
![image](https://user-images.githubusercontent.com/91907661/183301094-2339cb7c-2844-474b-a9cd-fe39a55d668b.png)
 
<br>
 
### Review Detail:
 
![image](https://user-images.githubusercontent.com/91907661/183302034-efbdb447-112d-4c3d-ba3b-98007f293856.png)
 
<br>
 
### Create A Review:
 
![image](https://user-images.githubusercontent.com/91907661/183301376-c0cef37d-e0c9-4ce6-83bb-07d4cc67a445.png)
 
<br>
 
## Edit and Delete Review:
 
The Edit page will very much resemble the Create A Review page, but the functionality here will be to edit what has been posted by the user previously.
 
The Delete page functions as you would expect, and will just ask the user to delete the selected review or cancel and go back to the previous page.
 
<br>
 
# Database Design and ERD
The purpose of the database is to make CRUD functionality available to the user. The Review model is at the heart of this - it provides the framework from which the user interacts with the site, with all the most relevant aspects related to creating a game review.
 
The next model is the Comments model, which allows community engagement among registered users to leave comments for one another's review posts.
 
Users are also able to to leave likes, funny and insightful votes using the icons mentioned previously. These are handled as many to many relationships as many users can leave many votes for many reviews.
 
Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.
 
![image](https://user-images.githubusercontent.com/91907661/183520884-739a977f-ce2c-4d47-a687-ca820bb9aa5e.png)
 
<br>
 
## Security
I have used using the UserPassesTextMixin and LoginRequiredMixin within the Django class based views.
Restricted functionality such as edit and delete functionality listed in the features was secured using this method.
 
Environment variables are stored in env.py and included in gitignore and these variables and their values are also stored within the Heroku config vars.
 
<br>
 
# APPLICATION TESTING, VALIDATION & SEO
I have provided a seperate file for all my Test cases and outcomes. This can be found in the [TESTING.md](TESTING.md) file.
 
<br>
 
## Lighthouse Results:
Please see screenshot below for Lighthouse results:
 
![image](https://user-images.githubusercontent.com/91907661/184167971-f94ed22d-b74a-44ec-8fe5-4ade2d1869d1.png)
 
<br>
 
## HTML
 
All pages were run through the [w3 HTML Validator](https://validator.w3.org/)
 
**NOTE:**
- Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI.
 
- To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.
 
<br>
 
## CSS
All pages were run through the [w3 CSS Validator](https://jigsaw.w3.org/css-validator/)
 
<br>
 
## PYTHON
 
All pages were run through the official [Pep8](http://pep8online.com/) validator to ensure all code was pep8 compliant.
 
**NOTE:**
- The AUTH_PASSWORD_VALIDATORS dictionary in settings.py has lines too long errors. I am afraid though that I have no way of correcting this.
 
<br>
 
## JAVASCRIPT
JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.
 
**NOTE:**
- There is only a very small piece of JavaScript in this project which is found in base.html. The function captures any toasts/messages generated by the app and closes them after 2.5 seconds.
 
- **Altough this script works perfectly fine, I get the warnings as shown below:**
    - Expected an identifier and instead saw '<'.
    - Expected an assignment or function call and instead saw an expression.
    - Missing semicolon.
  - Expected an assignment or function call and instead saw an expression.
  - Unclosed regular expression.
  - Unrecoverable syntax error. (100% scanned).
 
<br>
 
## Responsiveness
The html elements of this page have largely been constructed using Bootstrap.
- I have used Inspect option to go through responsiveness of all pages:
 
![image](https://user-images.githubusercontent.com/91907661/184174549-f19ac205-ec31-4b2f-95b9-9972a047b061.png)
 
- Site should be responsive and functional on all devices from 320px up
- Hamburger menu appears for mobile devices
 
<br>
 
# BUGS & FUTURE ENHANCEMENTS/FEATURES
 
### **Bugs & Known Issues**
- In the commit history there may appear to be some issues with my env.py file. I may have committed too early without having done this properly.
- Again, with the env.py file, my database on Heroku became corrupted so I had to generate new a new Postgres database key variable
- I was trying to implement the Edit and Delete Review function to be accessible from the nav bar, but could not get it to work as hoped. Instead, these feature are accessible from review_detail.html which is accessed via clicking on the the Review Title on view list on the Home page or Your Reviews page
- No lang attribute for html class. This has now been added with "en" value
- Some of the hr lines appear slightly thicker than other in places
- Button inside anchor tags that needed to be changed to forms to be compliant
- Submit Changes button won't go back to Your Reviews page, instead goes back to Home page
- User has to be told to use br html tags to create paragraphs in create a review and edit review forms
 
<br>
 
### **Future features and enhancements**
- Users can see a preview of their post before hitting the Submit button
- User will be able to submit their own photos instead of the one which appears as default
- User can use a search function which searches for strings (for game names, as example)
- User can search for all reviews that are reviewed on a particular console (controlled by the drop down menu choices)
- I wanted to implement the summernote panel on the front end, however, I tried several times to make the note panel responsive to screen width changes. Unfortunately, I had no more time to get this fixed and had to abandon the idea.
- Contact Us page could be added for site user to contact the Site Admin
 
<br>
 
# Deployment
 
## Heroku Deployment
 
I have deployed this site to [Heroku](https://id.heroku.com/login). Steps for deployments are outlined as below:
 
- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres and click to connect
- Go to the settings tab and click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This is provided with Postgres)
  - PORT: 8000
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorise when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy
 
## **Live site link:**
Please follow this link provided to access the site - [Gamer Review - Live Site](https://gamer-review-2022.herokuapp.com/)
 
<br>
 
# Credits
I would like to thank [Gareth McGirr](https://github.com/Gareth-McGirr) for going through a coding session with me in order to help with some of the structure and planning for the Edit and Delete functions of my site. His experience and insight was very helpful and very much appreciated.
 
## Images
PP4-Gamer.jpg was taken from [Pixabay](https://pixabay.com/photos/games-gaming-consoles-ps4-gamepad-2453777/)
 
 
Masthead image taken from [Unsplash](https://unsplash.com/photos/npxXWgQ33ZQ)
 
## Code
CSS code for Masthead taken from [Start Bootstrap](https://startbootstrap.com/snippets/full-image-header)
 
CCS code for static Masthead image rendering taken from [Stack Overflow](https://stackoverflow.com/questions/57625331/changing-social-media-icon-color)
 
CSS Code for social media icon colours: [Stack Overflow](https://stackoverflow.com/questions/57625331/changing-social-media-icon-color)
 
 





# Functional Testing
 
**Authentication tests**
 
**Description:**
 
Ensure that site user can register as a user on the site with required credentials
 
Steps:
 
1. Navigate to [Gamer Reviews](https://gamer-review-2022.herokuapp.com/) and click Register link on Nav Bar
2. Enter username, email and password
3. Click Sign up
 
Expected:
 
If all required details are entered successfully, the user can then access the site for it's intended use.
 
Actual:
 
User is informed that they have signed up successfully and they have access to site functionality
 
<hr>
<br>
 
**Description:**
 
**User is able to log in to the site**
 
Steps:
1. Navigate to [Gamer Reviews](https://gamer-review-2022.herokuapp.com/) and click Log In on the Nav Bar
2. Enter login details
3. Click login
 
Expected:
 
User is successfully logged in and redirected to the home page
 
Actual:
 
User is successfully logged in and redirected to the home page
 
<hr>
<br>
 
**Description:**
 
**User is able to log out of the site**
 
Steps:
1. Login to the website
2. Click the on Log Out on the Nav Bar
3. Click confirm on the confirm logout page
 
Expected:
 
User is logged out
 
Actual:
 
User is logged out
 
 
**Description:**
 
**User is able to log out of the site**
 
Steps:
1. Login to the website
2. Click on Log Out on the Nav Bar
3. Click confirm on the confirm logout page
 
Expected:
 
User is logged out
 
Actual:
 
User is logged out
 
<hr>
<br>
 
**Description:**
 
**User can create a Review**
 
Steps:
1. Ensure site user is logged in
2. Click on Create A Review on the Nav Bar
3. Fill in all required fields: Title, Game, and Content. Subtitle is an optional field.
4. Click on Submit Review to be submitted to Site Admin for approval
 
Expected:
 
Authenticated user can navigate to Create A Review Page and use the form to create their own Review. Once this is done they will receive a toast message telling them their submission has been successful
 
Actual:
 
User creates a Review post using the form provided and they are redirected to home page, informing them they have been successful with their review submission
 
<hr>
<br>
 
**Description:**
 
**Form validation works on Create a Review form**
 
Steps:
1. Ensure site user is logged in
2. Click on Create A Review on the Nav Bar
3. Try to submit form while leaving one of the required fields empty (Title, Game, Content)
4. Click on Submit Review button
 
Expected:
 
User will see a warning message pop up in the empty field informing them that this field must not be empty.
 
Actual:
 
User can see a warning message pop up in the empty field informing them that this field must not be empty if they click on the Submit Review button.
 
<hr>
<br>
 
**Description:**
 
**User can navigate to Your Reviews page and view their posts**
 
Steps:
1. Ensure site user is logged in
2. Click on Your Reviews on the Nav Bar
3. Click on the review Title to access the the review in full
 
Expected:
 
User can successfully see a list view of all the posts they have made. They can then click on any of the Review Titles to access the full detail of the post.
 
Actual:
 
User is successfully taken to Your Reviews page and can see a list view of all the posts they have made. They can then click on any of the Review Titles to access the full detail of the post.
 
<hr>
<br>
 
**Description:**
 
**User can only view their own posts on Your Reviews and not the reviews of other users**
 
Steps:
1. Ensure site user is logged in
2. Click on Your Reviews on the Nav Bar
3. Scroll through all reviews to check that all Gamer: tags are that of the logged in user
 
Expected:
 
User can only see the reviews they created and not those of other users
 
Actual:
 
User can scroll through the list view on the Your Reviews Page and only sees the reviews they have posted
 
<hr>
<br>
 
**Description:**
 
**User can see content of a review and make a comment using the form provided**
 
Steps:
1. Ensure site user is logged in
2. Click on any Review Title on the home page
3. User can scroll through the page to see review text, icons and comment form.
4. User enters a comment to be submitted to Site Admin for approval
 
Expected:
 
User can click on any Review Title and see full content of review plus icons and comment form. They can leave a comment successfully.
 
Actual:
 
User can see all the content as mentioned above. When they click on the Submit Comment button they are kept on same page and told their comment has been submitted for approval
 
<hr>
<br>
 
**Description:**
 
**User can upvote and undo upvote on the like, funny and insightful icons**
 
Steps:
1. Ensure site user is logged in
2. Click on any of the like, funny and insightful icons
3. Check that the icons counter has increased by 1
4. Click on the same icon to see if icon counter is reduced by 1
 
Expected:
 
User can click on any of the like, funny and insightful icons. The counter is increased by 1, and decreased by 1 if you click on the same icon to undo.
 
Actual:
 
User can click on any of the like, funny and insightful icons. The counter is increased by 1, and decreased by 1 if you click on the same icon to undo.
 
<hr>
<br>
 
**Description:**
 
**User can edit their reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
3. Click on the Edit Review button
4. Change text in fields
5. Click on Submit Changes button
 
Expected:
 
User can click the Edit Review button from their reviews once they are on the review detail page. They are then taken to a form which allows user to edit previously entered content.
 
Actual:
 
User can click the Edit Review button from their reviews once they are on the review detail page. They are then taken to a form which allows user to edit previously entered content. They are then redirected to the Your Reviews page and receive a toast message confirming that they have successfully updated their review.
 
<hr>
<br>
 
**Description:**
 
**User can delete their reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
3. Click on the Delete Review button
4. Click on Confirm Delete button
 
Expected:
 
User can click the Delete Review button from their reviews once they are on the review detail page. They are then taken to a page which asks them to either Confirm Delete or Cancel Delete via buttons.
 
Actual:
 
User can click the Delete Review button from their reviews once they are on the review detail page. They are then taken to a page which asks them to either Confirm Delete or Cancel Delete via buttons.
 
<hr>
<br>
 
**Description:**
 
**User can Edit and Delete *ONLY* their own reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
 
Expected:
 
If the user is not the gamer/owner of their post, they should not be able to see any option to Edit or Delete a review.
 
Actual:
 
User can only see an option to go back to the Home page, and no buttons appear for Edit or Delete review.
 
<hr>
<br>
 
**Description:**
 
**All nav links and buttons work as intended**
 
Steps:
1. Ensure site user is logged in
2. Click all navbar links to ensure they direct user as intended
3. Click all Review Title links (with dynamic colour background) to make sure they go to the corresponding review detail page
4. Click all Cancel, Submit and Back to home buttons
 
Expected:
 
User should be able to click on all links and buttons as described in the steps above and works as intended
 
Actual:
 
User can click on all links and buttons as described in the steps above and they work as intended
 
<hr>
<br>
 
**Description:**
 
**All social media footer icon links work as intended**
 
Steps:
1. Ensure site user is logged in
2. Click all icon links in footer to ensure they direct user as intended
 
Expected:
 
User should be able to click on all icon links in the footer as described in the steps above and work as intended
 
Actual:
 
User can click on icon links in the footer as described in the steps above and they work as intended
 
<hr>
<br>
 
**Description:**
 
**Site Pagination works as intended**
 
Steps:
1. Ensure site user is logged in
2. Ensure there is more than 6 review posts on the home page and/or Your Reviews page
3. Click on previous and next buttons that appear once the above condition is met
 
Expected:
 
User should be able to click on the next button which appears if there are more than 6 review posts on a page. Similarly, user should be able to go back from that page to previous page with the back button
 
Actual:
 
User can click on both the next and previous buttons if there are more that 6 review posts on Home page or Your Reviews page
