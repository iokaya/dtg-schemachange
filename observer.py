import time
import configparser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define a custom event handler by subclassing FileSystemEventHandler
class NewFileHandler(FileSystemEventHandler):
    # Define the behavior when a file is created
    def on_created(self, event):
        # Check that the event is not a directory
        if not event.is_directory:
            # Print the path of the new file that was added
            print(f"New file added to {event.src_path}")

# Read the configuration file to get the folders to monitor
config = configparser.ConfigParser()
config.read('folders')
folders_to_watch = []
for section in config.sections():
    path = config.get(section, 'path')
    folders_to_watch.append(path)

if __name__ == "__main__":
    # Create an instance of the custom event handler
    event_handler = NewFileHandler()
    # Create an instance of the observer
    observer = Observer()
    # Schedule the observer to monitor each folder in the list
    for folder_path in folders_to_watch:
        observer.schedule(event_handler, folder_path, recursive=True)
        # The `recursive` parameter tells the observer to monitor subdirectories as well

    # Start the observer
    observer.start()
    try:
        # Keep the observer running until the user interrupts the program with a keyboard interrupt
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if a keyboard interrupt is detected
        observer.stop()
    # Wait for the observer's thread to join the main thread before exiting
    observer.join()
