import wfdb
import os

data_path = os.path.join(
    os.getcwd(),
    "src/data"
)

if not os.path.exists(data_path):
    os.mkdir(data_path)

databases = ["mitdb", "ltafdb", "cpsc2021"]

for database in databases:
    wfdb.io.dl_database(db_dir=database, 
                        dl_dir=os.path.join(
                            data_path,
                            database 
                        ))