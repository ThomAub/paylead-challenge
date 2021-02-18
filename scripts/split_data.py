from pathlib import Path

import pandas as pd

raw_csv = Path("data/raw/BINNING_data_set.csv")
if not raw_csv.exists():
    raise FileNotFoundError("\nPlease make sure to have the BINNING_data_set in the folder `data/raw`")

raw_df = pd.read_csv(raw_csv.as_posix(), sep=";", index_col=0)

train_df = raw_df.query("set == 'TRAIN'")
test_df = raw_df.query("set == 'TEST'")

assert train_df.shape == (
    20000,
    12,
), f"Please make sure to have the correct version of the dataset. Should contain 20000x12 entry but there is {train_df.shape}"
assert test_df.shape == (
    4871,
    12,
), f"Please make sure to have the correct version of the dataset. Should contain 4871x12 entry but there is {train_df.shape}"

output_dir = Path("data/process")
output_dir.mkdir(parents=True, exist_ok=True)
train_df.drop(columns="set").to_csv(f"{output_dir.as_posix()}/BINNING_train.csv", index=False)
test_df.drop(columns="set").to_csv(f"{output_dir.as_posix()}/BINNING_test.csv", index=False)
