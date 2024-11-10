import os
from kaggle.api.kaggle_api_extended import KaggleApi
import database

# Set environment variables from Streamlit secrets
os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

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


