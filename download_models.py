import os
import urllib.request

MODEL_FILES = {
    "uspto_model.onnx": "https://figshare.com/ndownloader/files/54815900",
    "uspto_templates.csv.gz": "https://figshare.com/ndownloader/files/54815909",
    "zinc_stock.hdf5": "https://figshare.com/ndownloader/files/54815918"
}



def ensure_models():
    os.makedirs("models", exist_ok=True)
    for fname, url in MODEL_FILES.items():
        path = os.path.join("models", fname)
        if not os.path.isfile(path):
            print(f"Downloading {fname} ...")
            urllib.request.urlretrieve(url, path)

if __name__ == "__main__":
    ensure_models()
