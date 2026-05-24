from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class CSVHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("responses.csv"):
            print("responses.csv updated! Re‑running scripts...")
            subprocess.run(["python", "run_all.py"])

if __name__ == "__main__":
    path = os.getcwd()   # current folder monitor করবে
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("Watching responses.csv for changes... Press CTRL+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
