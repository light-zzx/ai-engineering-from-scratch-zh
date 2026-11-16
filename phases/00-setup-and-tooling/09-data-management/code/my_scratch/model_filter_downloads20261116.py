from huggingface_hub import snapshot_download

model_dir = snapshot_download(
    "sentence-transformers/all-MiniLM-L6-v2",
    cache_dir="/home/zzx/workspace/data/code/ai-engineering-from-scratch-zh/models/mini-lm-torch-only",
    allow_patterns=["*.json", "*.txt", "*.safetensors", "1_Pooling/*"],
)
print(model_dir)
