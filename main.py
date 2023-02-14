import pandas as pd
from metasingleton import MetaSingleton


class Reader(metaclass=MetaSingleton):
    def __init__(self):
        self.__path = None

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, new_path):
        if new_path.endswith('.xlsx'):
            self.__path = new_path
        else:
            print('Unsupported file format. File must be .xlsx')

    def read_file(self) -> pd.DataFrame:
        data = pd.read_excel(self.__path)
        return data

    @staticmethod
    def filter_data(data: pd.DataFrame) -> pd.DataFrame:
        data = data[data['number'] > 50]
        return data

    def write_data(self, data: pd.DataFrame) -> None:
        if self.__path is not None:
            data['number'].to_excel(self.__path, columns=['number'], index=False)
        else:
            print('Please specify file path')


if __name__ == '__main__':
    reader = Reader()
    reader1 = Reader()
    # to check if the singleton
    print(reader)
    print(reader1)
    reader.path = r'files/average_excel_enjoyer.xlsx'
    file_data = reader.read_file()
    print(file_data)
    filtered_data = reader.filter_data(file_data)
    reader.path = r'files/output.xlsx'
    reader.write_data(filtered_data)
    file_data = reader.read_file()
    print(file_data)
