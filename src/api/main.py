"""Entry point for application"""
from messaging import schedule_texts

if __name__ == "__main__":
    welcome_message = """
    Welcome to daily motivation! Hit ctrl+c to quit!
    """
    print(welcome_message)
    schedule_texts()
