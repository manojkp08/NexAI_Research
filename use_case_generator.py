import cohere
import database

# Set your Cohere API key
cohere_api_key = "FrfgqMDGk9txAEsUJzSShTvYoEhIB3HGloWsq0SX"

# Initialize the Cohere client
client = cohere.Client(cohere_api_key)

def generate_use_case(company_info):
    # Prepare the prompt using all available company information
     # Prepare a concise prompt focusing on key elements only
    prompt = f"Generate a structured, concise AI use case for '{company_info['company_name']}', an automotive company. Focus on the main objectives, benefits, and implementation details. Try to include everything under 90 to 100 words only."

    # # Add company introduction if available
    # if 'intro' in company_info:
    #     prompt += f"\n\nCompany Introduction: {company_info['intro']}"

    # Add a single line for the task description
    prompt += "\n\nTask: Describe a specific AI use case with key details, avoiding repetition. And also provide me a small response within 50 words."

    
    # Generate the AI-based use case using Cohere API
    response = client.generate(
        model="command-xlarge-nightly",  # Adjust to any Cohere model available in your account
        prompt=prompt,
        max_tokens=300,  # Adjust max tokens as necessary
        temperature=0.4  # Adjust temperature for creativity level, if needed
    )
    
    use_case_text = response.generations[0].text.strip()

    # Generate main theme specifically for dataset search
    main_theme_response = client.generate(
        model="command-xlarge-nightly",  # Ensure the model name matches
        prompt=f"Extract a concise heading or topic name from the following text for dataset search: {use_case_text}. Provide only the main topic name without additional context or phrases.",
        max_tokens=50,  # Limit tokens since we want a concise theme
        temperature=0.3
    )
    main_theme = main_theme_response.generations[0].text.strip()


    # Prepare and save the use case in the database
    use_case = {
        "company": company_info["company_name"],
        "use_case": use_case_text,
        "main_theme": main_theme
    }
    database.insert_use_case(use_case)
    return use_case


