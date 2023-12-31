from abc import ABC, abstractmethod
import numpy
import os
import wfdb

DATA_PATH = os.path.join(
    os.getcwd(),
    "app/data"
)


class Explorer:

    def __init__(self) -> None:
        self.__available_datasets = os.listdir(DATA_PATH)

    def get_available_datasets(self) -> list:
        return self.__available_datasets

    def get_available_records(self, dataset_name: str) -> list:
        all_record_files = os.listdir(
            os.path.join(DATA_PATH,
                         dataset_name))
        available_records = set()
        for file in all_record_files:
            available_records.add(file[:-4:])
        return sorted(list(available_records))

    def get_record_path(self, dataset_name: str, record_name: str) -> str:
        return os.path.join(DATA_PATH, dataset_name + "/" + record_name)


class Record(ABC):

    @abstractmethod
    def to_dict(self) -> dict:
        pass


class PhysionetRecord(Record):

    CHANNEL = 0
    def __init__(self, record: wfdb.Record) -> None:
        super().__init__()
        self.wfdb_record = record

    def to_dict(self) -> dict:
        signal_y = self.wfdb_record.p_signal[:, self.CHANNEL]
        time_x = numpy.arange(0, len(signal_y)) / self.wfdb_record.fs
        return {"time_s": time_x,
                "voltage_mV": signal_y
                }

    @staticmethod
    def from_path(path: str):
        record = wfdb.rdrecord(path)
        return PhysionetRecord(record)
