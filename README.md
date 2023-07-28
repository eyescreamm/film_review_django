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

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Type</th>
      <th>Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>int</td>
      <td>unique film ID</td>
    </tr>
    <tr>
      <td>title</td>
      <td>char(100)</td>
      <td>film title</td>
    </tr>
    <tr>
      <td>count_reviews</td>
      <td>int</td>
      <td>total number of reviews</td>
    </tr>
  </tbody>
</table>

User

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Type</th>
      <th>Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>int</td>
      <td>unique user ID</td>
    </tr>
    <tr>
      <td>name</td>
      <td>char(20)</td>
      <td>user name</td>
    </tr>
    <tr>
      <td>email</td>
      <td>email field</td>
      <td>user's email address</td>
    </tr>
    <tr>
      <td>password</td>
      <td>char(100)</td>
      <td>user' login password</td>
    </tr>
  </tbody>
</table>

Review

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Type</th>
      <th>Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>int</td>
      <td>unique review ID</td>
    </tr>
    <tr>
      <td>user</td>
      <td>user object</td>
      <td>user</td>
    </tr>
    <tr>
      <td>film</td>
      <td>film object</td>
      <td>film</td>
    </tr>
    <tr>
      <td>rating</td>
      <td>int</td>
      <td>rating of film (1~5)</td>
    </tr>
    <tr>
      <td>comment</td>
      <td>char</td>
      <td>comment of film</td>
    </tr>
    <tr>
      <td>created_at</td>
      <td>date</td>
      <td>creating date</td>
    </tr>
    <tr>
      <td>updated_at</td>
      <td>date</td>
      <td>updating date</td>
    </tr>
  </tbody>
</table>
