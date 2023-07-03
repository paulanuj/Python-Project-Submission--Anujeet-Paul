# Python-Project-Submission--Anujeet-Paul

# Movie Suggestions App
The Movie Suggestions App is a Python application that scrapes movie data from IMDb based on user input for the genre and provides movie suggestions. The app uses web scraping techniques with Selenium and saves the scraped data to a CSV file. It also integrates pandas for reading and displaying the movie suggestions.

# Software and Libraries Used
1. Python 3: The programming language used to develop the application.
2. Selenium: A Python library used for web scraping. It allows the app to automate interactions with IMDb's website and retrieve movie data.
3. ChromeDriver: A separate executable that acts as a bridge between the app and the Chrome browser. It is required by Selenium to control the browser and perform web scraping.
4. Pandas: A powerful library for data manipulation and analysis. It is used to save the scraped movie data to a CSV file and facilitate reading and displaying the movie suggestions.
5. Chrome Browser: The web browser used to access IMDb's website and retrieve movie data.

# Project Details
The Movie Suggestions App is designed to assist users in finding movie recommendations based on their preferred genre. Here are some key features of the project:

1. Web Scraping: The app utilizes Selenium to scrape movie data from IMDb. It interacts with IMDb's website, retrieves information such as movie titles, ranks, and genres, and compiles them into a structured format.
2. CSV Data Storage: The scraped movie data is saved to a CSV file named movie_data.csv. This allows for easy storage and retrieval of movie information for future use.
3. Error Handling: The app includes robust error handling mechanisms to ensure smooth execution. It utilizes try-except blocks to catch and handle exceptions that may occur during web scraping, data processing, and file operations. Appropriate error messages are displayed to provide information about any encountered errors.
4. User Interaction: The app prompts the user to enter a movie genre of their choice. It then scrapes IMDb for movies belonging to that genre, saves the data, and displays Top 50 movie suggestions along with their ranks and genres. Please note, version 2 code can be used in order to get the names of all the movies in the genre.

# Prerequisites
Before running the app, make sure you have the following installed:
1. Python 3
2. Selenium
3. ChromeDriver (compatible with your Chrome browser version)
4. Pandas

# Installation
1. Clone this repository to your local machine or download the source code.
2. Install the required Python packages using the following command:
"pip install selenium pandas"
3. Download the appropriate ChromeDriver executable for your Chrome browser version and update the path/to/chromedriver placeholder in the code with the path to the ChromeDriver executable.

# Usage
1.Run the movie_suggestions_app.py script:
"python movie_suggestions_app.py"
2. Enter a movie genre when prompted by the app.
3. The app will scrape movie data from IMDb based on the given genre, save it to a CSV file named movie_data.csv, and display movie suggestions on the console.

# Error Handling
The app includes error handling mechanisms to ensure a smooth execution. Here's how error handling is implemented in different parts of the code:

1. Web Scraping Error Handling:
The scrape_movies_by_genre() function includes a try-except block to catch any exceptions that may occur during web scraping. If an error occurs, an appropriate error message is displayed, and the function returns None.
2. Data Saving Error Handling:
The save_movie_data() function includes a try-except block to catch any exceptions that may occur while saving the scraped movie data to a CSV file. If an error occurs, an error message is displayed.
3. Data Reading Error Handling:
The read_movie_data() function includes a try-except block to catch potential exceptions that may occur while reading the movie data from the CSV file. If an error occurs, an error message is displayed, and an empty list is returned.
4. General Error Handling:
The main part of the code includes a try-except block that wraps the entire execution. This block catches any unexpected exceptions that may occur during the execution of the app. If an error occurs, an error message is displayed.

## Please note that IMDb's website structure may change over time, which may require adjustments to the code to ensure it continues to function correctly.

