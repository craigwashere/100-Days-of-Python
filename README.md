# 100 Days of Python
 Online course of 100 days creating Python apps

Missing days are "interactive" through 'Coding Rooms' or 'Auditorium' unless otherwise specified
Day 18:		day_18.py has to functions: create a random path and create a spirograph of random colors
		hirst.py recreates Hirst dot painting with Turtle

Day 19:		turtle race

Day 20:		'snake' game with Python turtles

Day 22:		Pong with Python turtles

Day 23:		Frogger type game with Python turtles

Day 24:		This is a template letter generator using one file for the names and another for the letter template. output files are stored in separate files according to names.

Day 28:		This is a windowed application for work/break scheduling. It uses tkinter for the window API and displays a tomato for some reason.

Day 29:		password generator with a tkinter GUI and saves with corresponding website and email address in a text file. Probably not the best way to store passwords, but for learning a Python GUI, fairly functional.

Day 31:		language learning app to learn vocabulary in a foreign language, French in this case. The words to learn are read from a .csv file using Pandas and displayed with tkinter GUI. The basic idea is to provide feedback as to which words were remembered correctly, the ones remembered correctly are removed from the master list and stored in a separate file when the app closes. When the app reopens, it looks for the words to learn file, if not found, loads the default list. Got some neat images for correct/incorrect.

day 34:		concludes the quiz program, but marks the first time using Python requests to retrieve data from a URL. While the application is a trivia game, it does demonstrate higher level software ideas including classes. Again, UI is handled through tkinter and mostly contained in the UI class.

day 35:		This app requests weather information from an online source and uses an email API to send and email to me regarding the weather. I hadn't setup an email client at the time of completing this.

day 38:		exercise tracker that uses nutritionix and sheety APIs. The Nutritionix API gets calorie count. Sheety API updates Google Sheets.

Day 44:		introduction to web page development, building a static web page in HTML and CSS.

Day 45:		uses beautifulSoup to scrape data from a webpage and write the results in a file. This script gets the 'top 100 must watch movies' from an archived version of empireonline.com

Day 46:		script that prompts for a year then uses BeautifulSoup to query to get the top songs from billboard.com. Once the top songs are obtained, we use spotipy to connect to spotify to load a playlist.

Day 47:		simple script to check a price on InstantPot and send an email when the price drops below a certain value. It uses beautifulSoup to scrape the price and python's builtin smtplib library to send the email. I believe the idea was to have this run remotely and periodically until an email is received.

Day 48:		this marks the beginning of web-based automation. Using selenium main.py gets upcoming events from python.org, interaction.py enters dummy values in a mock website created by the instructor. Selenium2.py is an inherited version of Selenium I used for the cookie automation that plays the cookie game on a website.

Day 49:		script to automatically apply for a job through linkedIn.com using selenium (in this case the inherited Selenium2 I created to handle some of the leg work).  Inside the Selenium2, as before, we make use of the geckodriver to run the we browser of choice (firefox).

Day 50:		requires tinder and facebook, I subscribed to neither and don't want to bother.

Day 51:		automates a internet speed test through speedtest.net and posts the results on twitter. I don't have twitter and won't bother. Makes use of Selenium2.

Day 52:		required instagram, again, not going to bother.

Day 53:		scrapes data from zillow.com and puts it into a premade Google form. (form has since been deleted). We scrape adress, price, and URL from zillow. Again, most projects using the inherited Selenium2

Day 54:		intro to web development with Flask. 

Day 55:		continutation of web development with backend development with a number guessing game.

Day 56:		starts with template web development in Flask, this is a resume web page.

Day 57:		further expands on template development using Jinja by building a blog page.

Day 58:		crash course in HTML and css writing a fictional "tindog" web page. 

Day 59:		blog webpage with templates with Flask/Jinja. 

Day 60:		login for the blog page using forms. 

Day 61:		login form example with validation, displays separate pages for successful vs. unsuccessful login.

Day 62:		a cafe blog type web  application that lists cafes and their rating with respect to power connections. it uses Flask, WTForms, and Jinja. It also writes the cafes to a .csv file for retrieval on next opening.

Day 63:		book cataloging web page to add books with rating. User can edit rating, but not the book entries. User can add/delete books. No .css styling. Book entries are added to a SQLite database. Again uses jinja forms for page population.

Day 64:		blog for Top 10 Movies. Backend uses SQLAlchemy to communicate to a SQLite database to store the movies and ratings. The front end uses WTForms, Flask, Jinja templates, and bootstrap. One of the bootstrap components is the carousel to display movie poster of selected movies and ratings. Also uses the tmdb API to get the  URL for the movie poster and other data.

Day 65:		cafe blog, but in API form. The only html template simply shows a welcome page, however, we have end points for updating coffee prices, deleting a cafe, adding a cafe, searching for a cafe, fetching all the cafes, and fetching a random cafe. Data returned is .json and includes several fields.

Day 66:     	blog server to display, add, edit, delete blogs. A lot of the front end was already created in terms of .css and javascript. Nevertheless, this project uses flask, wtforms, sqlalchemy, and ckeditor. We CRUD the sqlite database through sqlalchemy. The front end has a text editor field through CKEditor. Routes through the Python main file render templates with WTForms.

Day 68      simple application to utilize Flask authorization. Registered users are kept in a sqlite database, templates are rendered with default .css and wtforms.


Day 69:		culmination of 4 'days' of learning. The final website has several routes, user login validation and adminstration mode. Users can add posts and comment on other blogs. Again, utilizing WTForms, jinja, bootstrap, SQLAlchemy, and SQLite.
