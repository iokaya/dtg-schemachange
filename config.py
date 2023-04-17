import os
import configparser
from logger import logger

def get_snowflake_env_vars(connection_type):
    # Get the home directory of the current user
    home_dir = os.path.expanduser("~")

    # Define the path to the SnowSQL configuration file
    config_file = os.path.join(home_dir, ".snowsql", "config")

    # Create an instance of the ConfigParser class
    config = configparser.ConfigParser()

    # Read the contents of the SnowSQL configuration file
    config.read(config_file)

    # Construct the section name based on the connection type
    section_name = f"connections.{connection_type}"

    # Get the values for the specified connection from the configuration file
    account_name = config.get(section_name, "accountname")
    user_name = config.get(section_name, "username")
    password = config.get(section_name, "password")
    role_name = config.get(section_name, "rolename")
    warehouse_name = config.get(section_name, "warehousename")

    # Log the retrieved values
    logger.info(f"Retrieved Snowflake connection configuration for {connection_type} connection. Account Name: {account_name}, User Name: {user_name}, Role Name: {role_name}, Warehouse Name: {warehouse_name}")

    # Return the specified values
    return {
        "SNOWFLAKE_ACCOUNT": account_name,
        "SNOWFLAKE_USER": user_name,
        "SNOWFLAKE_PASSWORD": password,
        "SNOWFLAKE_ROLE": role_name,
        "SNOWFLAKE_WAREHOUSE": warehouse_name
    }



def get_folders_to_monitor():
    # Specify the name of the configuration file
    config_file = "folders.ini"
    # Create an instance of the ConfigParser class
    config = configparser.ConfigParser()
    # Read the contents of the config file
    if config.read(config_file):
        # Create an empty list to hold the folders to monitor
        folders_to_monitor = []
        # Iterate over each section in the file
        for section in config.sections():
            # Get the path and connection options for each section
            path = config.get(section, "path")
            connection = config.get(section, "connection")
            # Append the folder path and connection type in the format of 'folder_path:connection_name' to the list of folders to monitor
            folders_to_monitor.append({"path": path, "connection": connection})
            # Log the folder that was added to the list
            logger.info(f"Added {section} - {path} to list of folders to monitor.")
        return folders_to_monitor
    else:
        # If the file cannot be read, log an error and return an empty list
        logger.error("Could not read configuration file.")
        return []
