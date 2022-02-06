# BookReviews-tietokantasovellus
This is a web based application for book reviews community. Here you can share your thoughts on some book and find new ones to read!

## Välipalautus 1
Right now user can signup, login and logout. User can also create a review for a book which adds the book, categories, rating and review to the database. Missing review field parameters can cause crashing. Only minimal testing has been done.
[Test it in Heroku](https://bookreviews-tietokantasovellus.herokuapp.com/)

## User roles
There are two roles: admin and user

### User can
* Register, loginand logout :heavy_check_mark:
  * Without logging in user can only preview book reviews
* Search for book reviews via book name or category :white_large_square:
* Search for best reviewed books by category or year :white_large_square:
* Create new a book review for a book :heavy_check_mark:
  * Book review contains: the name of the book, rating (1) - (5), category and optional comment field 
* Like the reviews of some book :white_large_square:


### Admin can
* Delete unappropriate reviews :white_large_square:
* Suspend a user from reviewing :white_large_square:
