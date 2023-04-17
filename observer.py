import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import get_snowflake_env_vars
from logger import logger

# Define a function to monitor a list of folders
def monitor_folders(folders_to_watch):
    # Define a custom event handler by subclassing FileSystemEventHandler
    class FileHandler(FileSystemEventHandler):
        ## Initialize FileHandler
        def __init__(self, path, connection) -> None:
            super().__init__()
            self.path = path
            self.connection = connection
        # Define the behavior when a file is created
        def on_created(self, event):
            # Check that the event is not a directory
            if not event.is_directory:
                # Log the path of the new file that was added
                logger.info(f"Monitor: {self.path} - Connection: {self.connection} - New file added to {event.src_path} - Running schemachange....")
                # Create a new environment
                env = os.environ.copy()
                # Get snowflake env variables
                vars = get_snowflake_env_vars(self.connection)
                # Set env variables
                env["ROOT_FOLDER"] = self.path
                for key, value in vars.items():
                    env[key] = value
                # Set the schemachange command
                command = "schemachange -f $ROOT_FOLDER -a $SNOWFLAKE_ACCOUNT -u $SNOWFLAKE_USER -r $SNOWFLAKE_ROLE -w $SNOWFLAKE_WAREHOUSE -c DEMO_DB.SCHEMACHANGE.CHANGE_HISTORY"
                # Call subprocess.run() with the command and copied environment
                result = subprocess.run(command, shell=True, env=env, capture_output=True)
                # Print the command output
                print(result.stdout.decode())


    # Create an instance of the observer
    observer = Observer()
    # Schedule the observer to monitor each folder in the list
    for folder in folders_to_watch:
        # Extract path & connection variables
        path = folder['path']
        connection = folder['connection']
        # Create an instance of the custom event handler
        event_handler = FileHandler(path, connection)
        # Log the directory being monitored
        logger.info(f"Monitoring directory: {path} - Connection: {connection}")
        # Schedule the monitoring
        # The `recursive` parameter tells the observer to monitor subdirectories as well
        observer.schedule(event_handler, folder['path'], recursive=True, )

    # Start the observer
    observer.start()
    try:
        # Keep the observer running until the user interrupts the program with a keyboard interrupt
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Log the keyboard interrupt
        logger.info("Keyboard interrupt detected. Stopping monitoring.")
        # Stop the observer if a keyboard interrupt is detected
        observer.stop()
    # Wait for the observer's thread to join the main thread before exiting
    observer.join()
    # Log the end of the monitoring process
    logger.info("Monitoring stopped.")
