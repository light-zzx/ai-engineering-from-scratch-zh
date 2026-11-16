from datasets import load_dataset

dataset = load_dataset(path="./data/imdb", split="train")

# 进行格式转换
# dataset.to_csv("./data/imdb_convert/imdb_train.csv")
# dataset.to_json("./data/imdb_convert/imdb_train.json")
# dataset.to_parquet("./data/imdb_convert/imdb_train.parquet")

split = dataset.train_test_split(test_size=0.2, seed=42)
train_val = split["train"].train_test_split(test_size=0.125, seed=42)

train_ds = train_val["train"]
val_ds = train_val["test"]
test_ds = split["test"]

print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")
