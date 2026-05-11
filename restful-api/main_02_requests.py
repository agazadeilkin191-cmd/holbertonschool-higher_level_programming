from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

if __name__ == "__main__":
    # Execute function to print post titles
    print("--- Fetching and Printing Titles ---")
    fetch_and_print_posts()
    
    # Execute function to save posts to CSV
    print("\n--- Fetching and Saving Posts to CSV ---")
    fetch_and_save_posts()
