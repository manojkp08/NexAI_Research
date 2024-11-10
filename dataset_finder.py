import os
from kaggle.api.kaggle_api_extended import KaggleApi
import database

# Set up Kaggle API authentication
os.environ["KAGGLE_CONFIG_DIR"] = "C:/Users/manoj/Desktop/Market_Research_Project/kaggle.json"  # Make sure to set this correctly

api = KaggleApi()
api.authenticate()

def find_datasets(main_theme):
    datasets = api.dataset_list(search=main_theme)
    # If no datasets are found, retry with a broader fallback
    if not datasets:
        datasets = api.dataset_list(search="AI")
    dataset_links = [f"https://www.kaggle.com/{dataset.ref}" for dataset in datasets[:5]]
    dataset_info = {"keyword": main_theme, "links": dataset_links}
    database.insert_datasets(dataset_info)
    return dataset_links


