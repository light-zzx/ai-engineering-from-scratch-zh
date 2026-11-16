from datasets import load_dataset

dataset_imdb = load_dataset("stanfordnlp/imdb", cache_dir="./data/imdb")
print(dataset_imdb)
print(dataset_imdb["train"][0])


# 流式读取大数据集
dataset_wikipedia = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True, cache_dir="./data/wikipedia")
for i, example in enumerate(dataset_wikipedia):
    print(example["title"])
    if i >= 4:
        break


