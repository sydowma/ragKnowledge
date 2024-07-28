import pandas as pd
import pyarrow.parquet as pq


# 读取 Parquet 文件
def read_parquet_file(file_path):
    # 使用 pandas
    df_pandas = pd.read_parquet(file_path)
    print("Using pandas:")
    print(df_pandas.head())
    print(df_pandas.to_dict())

    # 使用 pyarrow
    table = pq.read_table(file_path)
    df_pyarrow = table.to_pandas()
    print("\nUsing pyarrow:")
    print(df_pyarrow.head())




if __name__ == '__main__':
    file_path = './ragtest/output/20240728-182757/artifacts/create_base_text_units.parquet'
    read_parquet_file(file_path)
