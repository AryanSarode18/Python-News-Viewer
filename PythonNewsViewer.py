# Import the 'requests' library for making HTTP requests
import requests

# Set your NewsAPI key
API_KEY = 'Your NewsAPI Key Here'

# NewsAPI endpoint for fetching top headlines
URL = 'https://newsapi.org/v2/top-headlines'

# Function to fetch and display news based on country and category
def fetch_and_display_news(country, category):
    # Set parameters for the API request
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
    }

    try:
        # Send a GET request to the NewsAPI
        response = requests.get(URL, params=params)
        data = response.json()

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            articles = data['articles']

            # Display information for each article
            for idx, article in enumerate(articles, start=1):
                print(f"Article {idx}:")
                print("Title:", article['title'])
                print("Source:", article['source']['name'])
                print("Description:", article['description'])
                print("URL:", article['url'])
                print("=" * 50)

        else:
            # Print an error message if fetching news fails
            print("Failed to fetch news:", data.get('message', 'Unknown error'))

    except requests.RequestException as e:
        # Print an error message if a request exception occurs
        print("An error occurred:", e)

# Main function to interact with the user
def main():
    print("Welcome to Python News Viewer!")
    print("Available news categories: business, entertainment, general, health, science, sports, technology")

    # Set the default country to 'in' (India)
    country = 'in'

    while True:
        category = input("Enter a news category (or 'exit' to quit): ").lower()

        if category == 'exit':
            print("\nThanks for Using This Program!\nBye!\nExiting!")
            break

        # Check if the entered category is valid
        if category not in ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']:
            print("Invalid category. Please choose from the available categories.")
            continue

        # Fetch and display news for the chosen category
        fetch_and_display_news(country, category)

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
