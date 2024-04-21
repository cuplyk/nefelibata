# blog/utils.py

def calculate_reading_time(content):
    # Your implementation to calculate reading time
    # This is just a placeholder example
    words_per_minute = 200
    word_count = len(content.split())
    reading_time_minutes = word_count / words_per_minute
    return int(reading_time_minutes)  # Convert to integer
