import schedule
import time
import random


class Topic():
    def __init__(self, content=[], images=[]):
        self.content = content
        self.images = images


def decide_research_type():
    return random.choice(["News", "LLM"])


def news_research() -> Topic:
    pass


def llm_research() -> Topic:
    pass


def main_task():
    research_type = decide_research_type()

    topic = (
        news_research()
        if research_type == "News"
        else llm_research()
    )
    


# Schedule the task
schedule.every().day.at("16:58").do(main_task)
schedule.every().day.at("16:59").do(main_task)
schedule.every().day.at("17:00").do(main_task)
schedule.every().day.at("17:01").do(main_task)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
