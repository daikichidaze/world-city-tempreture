# World City Temperature - Python Scripts

This repository contains Python scripts related to the collection and processing of city temperature data.

## Scripts Overview

### 1. data_collection.py

- **Purpose**: A script to fetch temperature data from external sources and save it as CSV files.
- **Key Features**:
  - `DataCollector` class: Contains methods to fetch data for a specified date and save it to a CSV file.
  - `base_url` and `output_folder` variables: Specify the URL for data fetching and the folder for saving the fetched data.
  - Main execution: Fetches data for a specified duration and saves each date's data as individual CSV files.

### 2. data_processing.py

- **Purpose**: A script for preprocessing the fetched temperature data and filling in missing values.
- **Key Features**:
  - `MissingValueCorrection` class: Contains methods for filling in missing values and preprocessing the data.
  - `SeparateByCity` class: Contains methods to separate data by city and save it.
  - `input_folder`, `missing_value_output_folder`, `by_city_output_folder` variables: Specify the input data folder, the folder to save data after missing value correction, and the folder to save data separated by city.
  - Main execution: Fills in missing values and separates data by city for saving.

---

# World City Temperature - Python スクリプト

このリポジトリは、都市の気温データの収集および処理に関連する Python スクリプトを含んでいます。

## スクリプトの概要

### 1. data_collection.py

- **目的**: 外部のデータソースから気温データを取得し、CSV ファイルとして保存するためのスクリプト。
- **主な機能**:
  - `DataCollector` クラス: 指定された日付のデータを取得し、CSV ファイルに保存するためのメソッドを持つクラス。
  - `base_url` と `output_folder` 変数: データの取得先の URL とデータの保存先のフォルダを指定。
  - メインの実行部分: 指定された期間のデータを取得し、それぞれの日付のデータを CSV ファイルとして保存。

### 2. data_processing.py

- **目的**: 取得した気温データの前処理と欠損値の補完を行うためのスクリプト。
- **主な機能**:
  - `MissingValueCorrection` クラス: 欠損値の補完とデータの前処理を行うためのメソッドを持つクラス。
  - `SeparateByCity` クラス: データを都市ごとに分割して保存するためのメソッドを持つクラス。
  - `input_folder`、`missing_value_output_folder`、`by_city_output_folder` 変数: 入力データのフォルダ、欠損値補完後のデータの保存先、都市ごとのデータの保存先を指定。
  - メインの実行部分: 欠損値の補完を行い、都市ごとにデータを分割して保存。
