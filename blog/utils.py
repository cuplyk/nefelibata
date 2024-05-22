def calculate_reading_time(content):
    words_per_minute = 200  # Average reading speed
    word_count = len(content.split())
    reading_time_minutes = word_count / words_per_minute
    return max(1, int(reading_time_minutes))  # Ensure at least 1 minute
