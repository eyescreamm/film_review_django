## film review app

#### General Description
The proposed web application allows the user to post and read film reviews. The user can: 

- Display the list of all movies poster registered in the DB. 
- Click on any movie in the list to read the description of movie's info such as title, rating, plot, reviews wrote by users and so on.
- User can register or login to write the reviews.
- Writing the rating and comment about each movie

The curren or furture being work:

- Implement function of sorting and filtering movie list by rating.
- Create mypage to see the list of review written by each user.
- Design the rich UI.

Notes: 

- user only can write the review with login status.
- Users can only write one review for one movie.
- When registering a user, a unique username and email address must be provided.
- Each review is associated with its author.  

Tables:

Film

|Column|Type|Comment|　
| --- | --- | --- |
| id | int | unique film ID |
| title | char(100)  | film title |
| count_reviews | int | total number of reviews |

User
| Column | Type | Comment　|　
| ---- | ---- | ---- |
| id | int | unique user ID |
| name | char(20)  | user name |
| email | email field | user's email address |
| password | char(100) | user's login password |

Review
| Column | Type | Comment　|　
| ---- | ---- | ---- |
| id | int | unique review ID |
| user | user object  | user |
| film | film object | film |
| rating | int | rating of film (1~5) |
| comment | char | comment of film |
| created_at | date  | creating date |
| updated_at | date | updating date |
