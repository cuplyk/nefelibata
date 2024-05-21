import math
from bs4 import BeautifulSoup

def calculate_reading_time(content):
    """
    Calculate the estimated reading time for a piece of content.
    
    Parameters:
    content (str): The content to calculate reading time for.

    Returns:
    int: Estimated reading time in minutes.
    """
    # Define words per minute reading speed
    words_per_minute = 200
    
    # Use BeautifulSoup to strip HTML tags if content includes HTML
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    
    # Calculate word count
    word_count = len(text.split())
    
    # Calculate reading time in minutes and round up
    reading_time_minutes = math.ceil(word_count / words_per_minute)
    
    return reading_time_minutes
