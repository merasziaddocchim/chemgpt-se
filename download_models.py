import os
import urllib.request

MODEL_FILES = {
    "uspto_model.onnx": "https://zenodo.org/record/7797465/files/uspto_model.onnx?download=1",
    "uspto_templates.csv.gz": "https://zenodo.org/record/7341155/files/uspto_templates.csv.gz?download=1",
    "zinc_stock.hdf5": "https://figshare.com/ndownloader/files/22348896"
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
