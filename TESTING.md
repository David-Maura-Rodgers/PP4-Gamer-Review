# Functional Testing

**Authentication tests**

**Description:**

Ensure that site user can register as a user on the site with required credentials

Steps:

1. Navigate to [Gamer Reviews](https://gamer-review-2022.herokuapp.com/) and click Register link on Nav Bar
2. Enter username, email and password 
3. Click Sign up

Expected:

If all required details are entered succesfully, the user can then access the site for it's intended use.

Actual: 

User is informed that they have signed up succesfully and they have access to site functionality

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

Authenticated user can navigate to Create A Review Page and use the form to create their own Review. Once this is done they will receive a toast message telling them their submission has been succesful

Actual:

User creates a Review post using the form provided and they are redirected to home page, informing them they have been succesful with their review submission

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

User sees a warning message pop up in the empty field informing them that this field must not be empty if they click on the Submit Review button.

<hr>
<br>

**Description:**

**User can navigate to Your Reviews page and view their posts**

Steps:
1. Ensure site user is logged in
2. Click on Your Reviews on the Nav Bar
3. Click on the review Title to access the the review in full

Expected:

User can succesfully see a list view of all the posts they have made. They can then click on any of the Review Titles to access the full detail of the post.

Actual:

User is succesfully taken to Your Reviews page and can see a list view of all the posts they have made. They can then click on any of the Review Titles to access the full detail of the post.

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
4. User can enter a comment to be submitted to Site Admin for approval

Expected:

User can click on any Review Title and see full content of review plus icons and comment form. They can leave a comment successfully.

Actual:

User can see all the content as mentioned above. When they click on the Submit Comment button they are kept on same page and told their comment has 