from operator import index
import os
import pandas as pd
import numpy as np

from datetime import datetime
from glob import glob


class MissingValueCorrection:
    @staticmethod
    def data_processing(input_csv_path: str, output_csv_path: str):
        df = pd.read_csv(input_csv_path)
        df.columns = ['poi_id', 'poi_name', 'country_name',
                      'lat', 'long', 'mean', 'max', 'min', 'precipitation']

        # Add date column
        df['date'] = datetime.strptime(input_csv_path[-14:-4], '%Y-%m-%d')

        df = MissingValueCorrection.inplace_nulls(df)
        df.dropna(inplace=True)
        df.to_csv(output_csv_path, index=False)
        print(f'output the file: {output_csv_path}')
        return

    @staticmethod
    def inplace_nulls(df: pd.DataFrame) -> pd.DataFrame:
        df.replace('', np.nan, inplace=True)
        df.replace(' ', np.nan, inplace=True)
        return df


class SeparateByCity:
    @staticmethod
    def data_processing(df: pd.DataFrame, poi_id: int, output_csv_path: str):
        df_tmp = df[df['poi_id'] == poi_id]
        df_tmp.to_csv(output_csv_path, index=False)
        print(f'output the file: {output_csv_path}')
        return


input_foler = 'data/raw'
missing_value_output_folder = 'data/processed'
by_city_output_folder = 'data/bycity'

if __name__ == '__main__':
    for p in glob(os.path.join(input_foler, '*csv')):
        output_path = os.path.join(
            missing_value_output_folder, p.split('/')[-1])
        MissingValueCorrection.data_processing(p, output_path)

    df_all_period = pd.concat([pd.read_csv(p) for p in glob(os.path.join(missing_value_output_folder, '*csv'))],
                              axis=0).reset_index(drop=True)

    for poi_id in df_all_period['poi_id'].drop_duplicates():
        output_path = os.path.join(by_city_output_folder, f'{poi_id}.csv')
        SeparateByCity.data_processing(df_all_period, poi_id, output_path)
