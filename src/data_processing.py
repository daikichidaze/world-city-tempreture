from operator import index
import os
import pandas as pd
import numpy as np

from datetime import datetime, timedelta
from glob import glob

from data_collection import start_date, end_date, duration_days


class MissingValueCorrection:
    @staticmethod
    def data_processing(input_csv_path: str, output_csv_path: str):
        df = pd.read_csv(input_csv_path)
        df.columns = ['poi_id', 'poi_name', 'country_name',
                      'lat', 'long', 'mean', 'max', 'min', 'precipitation']

        # Add date column
        df['date'] = datetime.strptime(input_csv_path[-14:-4], '%Y-%m-%d')

        df = MissingValueCorrection.inplace_nulls(df)
        df = MissingValueCorrection.convert_column(
            df, ['lat', 'long', 'mean', 'max', 'min', 'precipitation'], float)
        df.dropna(inplace=True)
        df.to_csv(output_csv_path, index=False)
        print(f'output the file: {output_csv_path}')
        return

    def inplace_nulls(df: pd.DataFrame) -> pd.DataFrame:
        for c, v in df.iteritems():
            if v.dtypes == object:
                df[c] = v.str.strip()

        for s in ['', ' ', '--']:
            df.replace(s, np.nan, inplace=True)

        return df

    def convert_column(df: pd.DataFrame, column_list: list, target_type: type) -> pd.DataFrame:
        for c in column_list:
            df[c] = df[c].astype(target_type)
        return df


class SeparateByCity:
    year_set = set(start_date + timedelta(days=i)
                   for i in range(duration_days))
    min_days = duration_days - 5
    target_days = duration_days

    @staticmethod
    def data_processing(df: pd.DataFrame, poi_id: int, output_csv_path: str):
        df_tmp = df[df['poi_id'] == poi_id]
        df_tmp = SeparateByCity.linier_space(df_tmp)

        df_tmp.to_csv(output_csv_path, index=False)
        print(f'output the file: {output_csv_path}')
        return

    def linier_space(df_poi: pd.DataFrame) -> pd.DataFrame:
        number_of_days = len(df_poi['date'].unique())

        if number_of_days > SeparateByCity.target_days:
            raise(ValueError('raws of dataframe is not correct'))

        if number_of_days < SeparateByCity.min_days:
            return df_poi

        miss_dates = SeparateByCity.year_set - set(df_poi['date'])

        for d in sorted(miss_dates):
            if d in set(df_poi['date']):
                continue

            if d >= df_poi['date'].min():
                front_last = df_poi[df_poi['date'] < d].iloc[-1]
            else:
                front_last = df_poi.iloc[0]

            if d <= df_poi['date'].max():
                back_first = df_poi[d < df_poi['date']].iloc[0]
            else:
                back_first = df_poi.iloc[-1]

            missing_days = max(
                (back_first['date'] - front_last['date']).days - 1, 1)

            df_add = pd.DataFrame()
            df_add[['poi_id', 'poi_name', 'country_name', 'lat', 'long']] = \
                [front_last[['poi_id', 'poi_name', 'country_name', 'lat', 'long']].tolist()] \
                * missing_days

            for c in ['mean', 'max', 'min', 'precipitation']:
                df_add[c] = np.linspace(
                    front_last[c], back_first[c], missing_days+2)[1:-1]

            df_add['date'] = [front_last['date'] +
                              timedelta(days=i+1) for i in range(missing_days)]

            df_poi = pd.concat([df_poi, df_add], axis=0)
            df_poi.sort_values(by='date', ignore_index=True, inplace=True)

        return df_poi


# folder path info
input_foler = 'data/raw'
missing_value_output_folder = 'data/processed'
by_city_output_folder = 'data/bycity'


if __name__ == '__main__':
    for p in glob(os.path.join(input_foler, '*csv')):
        output_path = os.path.join(
            missing_value_output_folder, p.split('/')[-1])
        MissingValueCorrection.data_processing(p, output_path)

    df_all_period = pd.concat([pd.read_csv(p, parse_dates=['date'])
                               for p in glob(os.path.join(missing_value_output_folder, '*csv'))],
                              axis=0).reset_index(drop=True)

    for poi_id in df_all_period['poi_id'].drop_duplicates():
        output_path = os.path.join(by_city_output_folder, f'{poi_id}.csv')
        SeparateByCity.data_processing(df_all_period, poi_id, output_path)
