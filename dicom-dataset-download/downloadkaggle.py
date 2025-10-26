import kagglehub

# Download latest version
kagglehub
path = kagglehub.dataset_download("aryashah2k/hippocampal-sparing-dataset")

print("Path to dataset files:", path)