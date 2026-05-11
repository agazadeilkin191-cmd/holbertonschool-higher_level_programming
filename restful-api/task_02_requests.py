import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints the status code 
    along with all post titles to the console.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful (200 OK)
    if response.status_code == 200:
        posts = response.json() # Parse the data into a JSON object
        
        # Iterate through the parsed data and print the titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts from the API and saves id, title, and body 
    into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Prepare a list of dictionaries with required fields
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        # Define the file name
        filename = 'posts.csv'
        
        # Write the data to a CSV file
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader() # Write column headers
            writer.writerows(structured_data) # Write post data
        
        print(f"Successfully saved data to {filename}")
