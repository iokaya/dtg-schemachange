from observer import monitor_folders
from config import get_folders_to_monitor

if __name__ == "__main__":
    # Get the list of folders to monitor from the configuration file
    folders_to_monitor = get_folders_to_monitor()
    # Call the monitor_folders function with the folders_to_monitor list as an argument
    monitor_folders(folders_to_monitor)
