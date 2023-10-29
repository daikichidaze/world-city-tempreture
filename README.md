# World City Temperature

This repository contains Jupyter notebooks related to the analysis of city temperature data.

## Notebooks Overview

### 1. Data Collection

- **Summary**:
  - Data collection from external sources and saving it to CSV files.
  - Performing API requests to fetch data for specific dates.
  - Saving the fetched data into CSV files.

### 2. Single Day Analysis (After null dropped)

- **Summary**:
  - Combining data from multiple CSV files.
  - Displaying memory usage of current variables.
  - Ensuring no duplications in `poi_id`.
  - Checking for missing dates in the yearly dataset.

### 3. City Data Correction

- **Summary**:
  - Correcting city data.
  - Including codes to fill missing data.

### 4. GDP Correlation

- **Summary**:
  - Analyzing correlation between GDP and temperature.
  - Fetching POI information from each CSV file.
  - Calculating average temperature for each city and country.
  - Visualizing correlation between average temperature and GDP for each country.
  - Displaying yearly trend of correlation between temperature and GDP.

## Usage

Each notebook operates independently. Open and execute the notebook of your interest. Information regarding required data and library imports can be found inside the notebooks.

## Miscellaneous

For questions or feedback regarding this repository, please create an issue or contact the repository owner directly.

---

# World City Temperature

このリポジトリは、都市の気温データに関する解析を行うための Jupyter notebook を含んでいます。

## ノートブックの内容

### 1. Data Collection

- **概要**:
  - 外部からのデータの取得と CSV への保存を行っています。
  - 特定の日付のデータを取得するための API リクエストを行っています。
  - 取得したデータを CSV ファイルに保存しています。

### 2. Single Day Analysis (After null dropped)

- **概要**:
  - 複数の CSV ファイルからデータを読み込んで結合しています。
  - 現在の変数のメモリ使用量を表示しています。
  - `poi_id`の重複がないことを確認しています。
  - 1 年間のデータセット内で欠落している日付を確認しています。

### 3. City Data Correction

- **概要**:
  - 都市データの補正を行っています。
  - 欠損データを補完するためのコードが含まれています。

### 4. GDP Correlation

- **概要**:
  - GDP と気温の相関を解析しています。
  - 各 CSV ファイルから POI の情報を取得しています。
  - 各都市および国の平均気温を計算しています。
  - 各国の平均気温と GDP の相関を可視化しています。
  - 年間の気温と GDP の相関のトレンドを表示しています。

## 使用方法

各ノートブックは独立しているため、興味のある解析を行いたいノートブックを開いて実行してください。必要なデータやライブラリのインポートに関する情報もノートブック内に記載されています。

## その他

このリポジトリに関する質問やフィードバックは、issue を作成するか、リポジトリの所有者に直接連絡してください。
