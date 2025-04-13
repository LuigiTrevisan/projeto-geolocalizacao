import requests
import zipfile
import os


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Downloaded: {output_path}")
    else:
        print(
            f"Failed to download from {url}. Status code: {response.status_code}")
      
def unzip(file, folder):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(folder)
    print(f"Unzipped: {file} to {folder}")


files_to_download = [
    ("https://www.kaggle.com/api/v1/datasets/download/markfinn1/bairros-de-so-paulo",
     "./files/bairros-de-sao-paulo"),
    ("https://www.kaggle.com/api/v1/datasets/download/renatosn/sao-paulo-housing-prices",
        "./files/sao-paulo-housing-prices")
]

for url, output_path in files_to_download:
    download_file(url, f'{output_path}.zip')
    unzip(f'{output_path}.zip', output_path)

os.rename("./files/bairros-de-sao-paulo/bairros.geojson", "./files/bairros.geojson")
os.rename("./files/sao-paulo-housing-prices/data.csv", "./files/prices.csv")