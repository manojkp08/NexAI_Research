# # main.py -- fastapi backend
# from fastapi import FastAPI
# from research_agent import get_company_info
# from use_case_generator import generate_use_case
# from dataset_finder import find_datasets
# import database

# app = FastAPI()


# @app.get("/generate_report/{company_name}")
# def generate_report(company_name: str):
#     # Research
#     company_info = get_company_info(company_name)
#     database.insert_company_info(company_info)

#     if "error" in company_info:
#         return {"error": company_info["error"]}

#     # Use Case Generation
#     use_case = generate_use_case(company_info)

#     # Dataset Search
#     datasets = find_datasets("supply chain")

#     # Generate report
#     report = {
#         "company_info": company_info,
#         "use_case": use_case,
#         "datasets": datasets
#     }
#     return report
