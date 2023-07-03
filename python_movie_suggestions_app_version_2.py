# Code to get all the movie names for one genre
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def scrape_movies_by_genre(genre):
    try:
        service = Service('path/to/chromedriver')  # Replace with the path to your ChromeDriver executable
        driver = webdriver.Chrome(service=service)

        url = f'https://www.imdb.com/search/title/?genres={genre}&sort=user_rating,desc'  # IMDb movies by genre
        driver.get(url)

        movies = []
        while True:
            movie_elements = driver.find_elements(By.CSS_SELECTOR, 'div.lister-item-content')

            for element in movie_elements:
                rank = element.find_element(By.CSS_SELECTOR, 'span.lister-item-index').text.strip('.')
                title = element.find_element(By.CSS_SELECTOR, 'h3 a').text
                genre = element.find_element(By.CSS_SELECTOR, 'p span.genre').text.strip()
                movies.append({'Rank': rank, 'Title': title, 'Genre': genre})

            next_button = driver.find_element(By.CSS_SELECTOR, 'a.lister-page-next.next-page')
            if 'disabled' in next_button.get_attribute('class'):
                break

            next_button.click()

        driver.quit()
        return movies
    except Exception as e:
        print(f"An error occurred while scraping: {str(e)}")
        return None

def save_movie_data(movies):
    try:
        df = pd.DataFrame(movies)
        df.to_csv('movie_data.csv', index=False)
        print("Movie data saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving movie data: {str(e)}")

def read_movie_data():
    try:
        df = pd.read_csv('movie_data.csv')
        return df
    except FileNotFoundError:
        print("Movie data file not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading movie data: {str(e)}")
        return None

def display_movie_suggestions(movies):
    if movies is None:
        print("No movie data available.")
    else:
        print("Movie suggestions:")
        for _, row in movies.iterrows():
            rank = row['Rank']
            title = row['Title']
            genre = row['Genre']
            print(f"{rank}. {title} ({genre})")

def movie_suggestions_app():
    genre = input("Enter a movie genre: ")

    try:
        movies = scrape_movies_by_genre(genre)
        if movies is not None:
            save_movie_data(movies)
            movie_data = read_movie_data()
            display_movie_suggestions(movie_data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the movie suggestions app
movie_suggestions_app()
