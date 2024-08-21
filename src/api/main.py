"""Entry point for application"""
from messaging import schedule_texts

if __name__ == "__main__":
    print("""
    Welcome to daily motivation! Hit ctrl+c to quit!
    """)
    schedule_texts()
