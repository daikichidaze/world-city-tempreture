import csv
from tracemalloc import start
import requests
import time
from datetime import datetime, timedelta


class DataCollecter:
    def __init__(self, base_url: str, output_folder: str, target_date: datetime):
        self.base_url = base_url
        self.output_folder_path = output_folder
        self.target_date = target_date

    def Data_collect(self):
        uri = self.base_url + self.__generate_parameter(self.target_date)
        x = requests.get(uri)
        col, val = self.__format_response(x)
        output_file_path = f'{self.output_folder_path}/{self.target_date.strftime("%Y-%m-%d")}.csv'
        self.__generate_file(output_file_path, col, val)
        return

    def __generate_parameter(self, target_date: datetime) -> str:
        y = target_date.year
        m = target_date.month
        d = target_date.day
        return f'?&y={y}&m={m}&d={d}'

    def __format_response(self, raw: requests.Response):
        csv_raw = csv.reader(raw.text.splitlines())
        csv_list = list(csv_raw)
        columns = [r0 + r1 for r0, r1 in zip(csv_list[0], csv_list[1])]
        return (columns, csv_list[2:])

    def __generate_file(self, path, col, val):
        with open(path, 'w') as f:
            writer = csv.writer(f, quotechar='"')
            writer.writerow(col)
            writer.writerows(val)
        return


base_url = r'https://www.data.jma.go.jp/cpd/monitor/dailyview/all_download_d.php'
output_folder = '../data'

start_date = datetime(2021, 1, 1)
duration_days = 365
end_date = start_date + timedelta(days=duration_days)


if __name__ == "__main__":
    target_date = start_date

    for _ in range(duration_days):
        dc = DataCollecter(base_url, output_folder, target_date)
        dc.Data_collect()
        target_date = target_date + timedelta(days=1)
        time.sleep(0.5)
