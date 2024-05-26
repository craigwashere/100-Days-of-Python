# 100 Days of Python
 Online course of 100 days creating Python apps

> [!Note]
> Missing days are "interactive" through 'Coding Rooms' or 'Auditorium' unless otherwise specified

## Section 1
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

## Section 2
> [!Note]
> This is the data science used on Google colab that I didn't enjoy at all

Day 73:		beginning data science section investigating salaries based on college majors and simple plots with Pandas and MatPlotLib

day 74:		Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask whole bunch of interesting questions about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all.

day 75:		This notebook explores if search popularity relates to other kinds of data. Perhaps there are patterns in Google's search volume and the price of Bitcoin or a hot stock like Tesla.

Day 76:		In this notebook, we will do a comprehensive analysis of the Android app market by comparing thousands of apps in the Google Play store.

Day 77:		In this notebook we'll learn how to use NumPy to work with numerical data.

Day 78:		This notebook investigates if there's a relationship using the movie budgets and financial performance data that scraped from the-numbers.com on May 1st, 2018.

Day 79:		This notebook looks for patterns in past Nobel laureates. We start off making standard bar charts, move on to stacked bar charts. Then we'll make a scatter plot with a rolling average lineplot overlay. Afterwards, we'll make horizontal barcharts, a choropleth showing prize winners by country using a map of the world. Then, we'll create stacked horizontal bar charts, followed by a sunburst chart. Finally, we create a regplot with a regression line and a boxplot.

Day 80:		This notebook examines data related to why so many women in maternity wards were dying from childbed fever (i.e. puerperal fever). We'll make several line plots followed by a boxplot and a histogram. We use Kernel Density Estimate (KDE) to visualise a smoot distribution. Finally, we use a t-test to determine if the differences in the means are statistically significant or purely due to chance. The p-value came out extremely small, therefore we can be certain that handwashing has made a difference to the average monthly death rate. 

Day 81:		Capstone project: building a model that can provide a price estimate based on a home's characteristics. We start off creating several bar charts with a Kernel Density Estimate overlay. We then run Seaborn's pairplot in attempt to visualise all the relationships at the same time. Then, we make several joinplots which is a scatterplot with bar graphs on the top and right side to look for correlations between distance from employment and NOX pollution, INDUS (the proportion of non-retail industry i.e., factories) with NOX (Nitric Oxide Pollution), proportion of lower-income population with RM (number of rooms), and proportion of lower-income population with price. We then get into multivariable regression models and draw some scatter plots. We then look at the residuals to verify they're random by using skew/mean and creating histogram with kernel Density Estimate overlay. finally, we predict a few house prices using the regression models.

## Portfolio Section
>[!Caution]
> These prompts are self-graded

> [!Warning]
> I don't know if any of these are correct, I got answers and drew some plots
>
> day 98:		Use space mission data from 1957 onwards to analyse and visualise trends over time.
>
> Day 99:		Extract insights from combining US census data and the Washington Post's database on deaths by police in the United States.
>
> Day 100:	Using data from the National Longitudinal Survey of Youth 1997-2011, we'll use regression models to try to predict salaries.

Day 83:		Interactive Tic-Tac-Toe (Naughts and crosses). Uses Tkinter for imaging and window events. I found some stock images of 'X' and 'O'. I also found an unwinnable AI to implement, best user can get is a tie. I don't even have a winning .png

Day 84:		image watermarking app using tkinter GUI to handle the file handling and Python Imaging Library (PIL) to handle the image processing.

Day 85:		A Tkinter GUI desktop application that tests your typing speed. I have a master list of words I downloaded from a reading practice website of various lenghts. A couple buttons to start/stop/reset the typing test. I use a separate thread to monitor typing times. When the length of word is matched or greater, the score is adjusted and a new word is retrieved. 

![day 85](https://github.com/craigwashere/100-Days-of-Python/blob/main/day_85/day_85.png)

Day 86:		Using Python Turtle, build a clone of the 80s hit game Breakout. I tried to match the color scheme of the early 1980's Atari game. The game functions almost identically, however, it takes a while to load as there are over 50 turtles to draw including the ball and paddle.

![day 86](https://github.com/craigwashere/100-Days-of-Python/blob/main/day_86/day_86.png)


day 87:     Wifi-cafe app, again. Probably third time revisiting this idea. This time, in addition to Flask, Jinja, and WTForms, we store the cafe information in a SQLite database. 
![Welcome page](https://github.com/craigwashere/100-Days-of-Python/blob/main/day_87/day_87-1.png)
![Cafe List](https://github.com/craigwashere/100-Days-of-Python/blob/main/day_87/day_87-2.png)
![Edit Cafe](https://github.com/craigwashere/100-Days-of-Python/blob/main/day_87/day_87-3.png)


Day 88:		web-based to do list. online to do list, but the list isn't saved anywhere, probably could have implemented that with a file save or something. these webpages make use of bootstrap, flask, and jinja. fairly simple, but functional.

![day 88](https://github.com/craigwashere/100-days-of-python/blob/main/day_88/day-88.png)

Day 89:		App where the text will disappear if user stops typing for 5 seconds. This uses TKinter for the GUI and text space. I found a scroll app implementation off geeksforgeeks.com. The keyDown event deletes the timer keyUp creates. 

![most dangerous text editor](https://github.com/craigwashere/100-Days-of-python/blob/main/day_89/day-89.png)

day 90:		python script to convert a .pdf file to an audio book. I found a webpage describing how to load .pdf files in python and merely needed to send text to Amazon's Polly to convert to speech. It's been a while, but I believe Amazon provided the polly.py code.

for extra credit, Amazon also provided a website to convert text in a textarea to speech in various voices. I used pdf.js to convert the loaded .pdf to text, insert into the text area and send to polly.

None of the voices returned have any inflections, or any variations in speech patterns as they're paid services at the time of the application implementation. 

![image of webpage converting text to speech](https://github.com/craigwashere/100-Days-of-python/blob/main/day_90/day-90.png)

day 91:		Day 91 is a webpage that gets the most common colors from an image and displays the RGBA values and a sample in a table. The image uploading is handled in via Javascript and passed to a Python backend. PIL handles most of the heavy lifting in terms of getting the colors, the values are passed back to the same webpage. (The filename gets erased on upload as default security.)

![image of color pallette generator](https://github.com/craigwashere/100-Days-of-python/blob/main/day_91/day-91.png)

day 92:		 "a custom web scraper to collect data". I was considering moving to another city and wanted information on apartments, specifically, which apartments would accept my 2 dogs. This script uses beautifulSoup for interaction with the webpage and collection of price, rating, weight limit of the dogs, url, and a couple other items. After accumulating all this, writes to a .csv file locally.

day 93:     Write Python code to play the Google Dinosaur Game. When google.com detects a device not connected to the internet, it displays a dinosaur game whose object is to vault cacti and rocks. This python script loads a faux page and automates playing the game. The main function forks two processes, one to get the pixels of a certain area of the screen, the other to check the pixels for a certain color. Most of the interface is handled through pyautogui. I had a little trouble getting the timing correct, apparently, it differs by system. This works for a few minutes at least.

day 94:		Space Invaders. A remake of the 1978 video game. I borrowed a lot from the breakout game several weeks back, but implemented skins ("shapes") for the turtles to mimic the orginal game. also, game pieces explode in very rudimentary animation. Again, it takes a little while to render 50 turtles.

![game play](https://github.com/craigwashere/100-Days-of-python/blob/main/day_94/day-94-1.png)
![end game explosion](https://github.com/craigwashere/100-Days-of-python/blob/main/day_94/day-94-2.png)

day 95:		a custom website using an interesting API. xkcd.com provides an API for their comics which includes the comic, comic titles,
URLs, post dates, transcripts (when available), and other metadata. The Python script checks for valid response and passes the json data to the flask webpage. If the response was 404, set the id back to '1' and get the first comic. The webpage is fairly trivial, display the image, title, date, and a couple chevrons to navigate to the next/previous comic.
![day 95](https://github.com/craigwashere/100-Days-of-python/blob/main/day_95/day-95.png)
