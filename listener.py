import time
from watchdog.observers import Observer
from utils import OnChange


def file_listener():
    COVER_LETTER_PATH = "C:/Users/russ1/Documents/Important Documents/Resume/Software Engineer/Cover Letters"

    print(f"Starting to listen at {COVER_LETTER_PATH}")

    callback = OnChange()
    observer = Observer()
    observer.schedule(callback, COVER_LETTER_PATH, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


file_listener()
