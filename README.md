# dtg-schemachange

## Requirements

> :snake: `Conda` or `Miniconda` must be installed

> :cyclone: `SnowSQL` named connections must be ready with given pattern
```bash
# For MacOS and Linux users
# ~/.snowsql/config
# For Windows users
# %USERPROFILE%\.snowsql\config
[connections.<CONNECTION_NAME>]
accountname = <ACCOUNT_NAME>
username = <USERNAME>
password = <PASSWORD>
rolename = <ROLE_NAME>
warehousename = <WAREHOUSE_NAME>
dbname = <DB_NAME>
```

## Usage

> :cd: `cd` into the project directory
```bash
cd ~/projects/dtg/dtg-schemachange
```

> :outbox_tray: Create new `conda` environment if not exists
```bash
conda env create -f environment.yaml
```

> :seedling: Activate `conda` environment
```bash
conda activate dtg-schemachange
```

> :star2: Install required packages
```bash
pip install -r requirements.txt
```

> :open_file_folder: Alter `folders.ini` for monitoring specified folders in format below
```bash
[<ANY_NAME>]
connection = <CONNECTION_NAME>
path = <ROOT_FOLDER>
```

> :runner: Run the main python script
```bash
python app.py
```