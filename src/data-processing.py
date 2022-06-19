import os
import pandas as pd
import numpy as np

from glob import glob


class MissingValueCorrection:
    @staticmethod
    def data_processing(input_csv_path: str, output_csv_path: str):
        df = pd.read_csv(input_csv_path)
        df.columns = ['poi_id', 'poi_name', 'country_name',
                      'lat', 'long', 'mean', 'max', 'min', 'precipitation']

        df = MissingValueCorrection.inplace_nulls(df)
        df.dropna(inplace=True)
        df.to_csv(output_csv_path)

    @staticmethod
    def inplace_nulls(cls, df: pd.DataFrame) -> pd.DataFrame:
        df.replace('', np.nan, inplace=True)
        df.replace(' ', np.nan, inplace=True)
        return df


input_foler = 'data/raw'
output_folder = 'data/processed'

if __name__ == '__main__':
    for p in glob(os.path.join(input_foler, '*csv')):
        output_path = os.path.join(output_folder, p.split('/')[-1])
        MissingValueCorrection.data_processing(p, output_path)
