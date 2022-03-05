# BookReviews-tietokantasovellus
This is a web based application for book reviews community. Here you can share your thoughts on some book and find new ones to read!

## Välipalautus 1
Right now user can signup, login and logout. User can also create a review for a book which adds the book, categories, rating and review to the database. Missing review field parameters can cause crashing. Only minimal testing has been done.
[Test it in Heroku](https://bookreviews-tietokantasovellus.herokuapp.com/)

## Välipalautus 2
Basic functions are implemented. Styling and UI is not finished. DB queries are quite solid and ready.
[Test it in Heroku](https://bookreviews-tietokantasovellus.herokuapp.com/)

## Loppupalautus
UI and basic functions are ready. Did not have time for testing. 
[Test it in Heroku](https://bookreviews-tietokantasovellus.herokuapp.com/) Create account and write some reviews for your favourite books. Crashing can happen when creating a review without rating *(Broke the JS pop-up at the last meters and did not have time to fix it)*.

## User roles
There are two roles: admin and user

### User can
* Register, loginand logout :heavy_check_mark:
  * Without logging in user can only preview book reviews
* Search for book reviews via book name :heavy_check_mark:
* Search for best reviewed books by category :heavy_check_mark:
* Show top-5 reviewed books on home page :heavy_check_mark:
* Create new a book review for a book :heavy_check_mark:
  * Book review contains: the name of the book, rating (1) - (5), category and optional comment field 
