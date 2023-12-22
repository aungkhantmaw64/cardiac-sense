import os

DATA_PATH = os.path.join(
        os.getcwd(),
        "app/data"
    )

class Explorer:
    
    def __init__(self) -> None:
        self.__available_datasets = os.listdir(DATA_PATH)
    
    def get_available_datasets(self)->list:
        return self.__available_datasets
    
    def get_available_records(self, dataset_name: str)->list:
        all_record_files = os.listdir(
            os.path.join(DATA_PATH,
                         dataset_name))
        available_records = set()
        for file in all_record_files:
             available_records.add(file[:-4:])
        return sorted(list(available_records))
