import streamlit as st
from research_agent import get_company_info
from use_case_generator import generate_use_case
from dataset_finder import find_datasets
import database

st.markdown("""
    <style>
    /* Background and General Settings */
    body {
        background: linear-gradient(135deg, #1e1e2f, #0a0a1a);
        color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 3.5rem;
        color: #ff6f61;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
        margin-bottom: 1rem;
    }
    
    /* Input Fields Styling */
    .stTextInput>div>div>input {
        background-color: #2c2c3e;
        color: #f0f0f0;
        border-radius: 8px;
        font-size: 1.2rem;
        padding: 0.7rem;
        border: 1px solid #ff6f61;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        border-color: #ff4c3b;
        box-shadow: 0 0 5px rgba(255, 76, 59, 0.5);
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #ff6f61;
        color: #ffffff;
        border-radius: 8px;
        padding: 0.8rem 1.6rem;
        font-size: 1.2rem;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #EBA59FFF;
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(255, 76, 59, 0.4);
    }
    
    /* Section Styling */
    .section {
        background-color: #2c2c3e;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.4);
        animation: slideInUp 1s ease forwards;
    }
    
    h2 {
        font-size: 2.5rem;
        color: #ff6f61;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    /* Table Styling */
    .stTable {
        font-size: 1.1rem;
        color: #f0f0f0;
        background-color: #2b2b3d;
        border-radius: 10px;
        border-collapse: collapse; 
    }

    .stTable th, .stTable td {
        padding: 12px; 
        text-align: left; 
    }

    .stTable th {
        background-color: #ff6f61; 
      color:#ffffff; 
      border-bottom: solid #ff4c3b; 
      font-weight:bold; 
      text-transform uppercase; 
      letter-spacing:.05em
     }

     /* Hover Effects */
     .section:hover {
         transform: translateY(-5px);
         transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; 
         box-shadow :0px8px20pxrgba(255,76,59,.4)
     }

     /* Responsive Design */
     @media (max-width:768px) {
         h1 {
             font-size :2.5rem
         }

         h2{
             font-size :2rem
         }

         .stButton > button{
             padding : .6rem
         }

         .section{
             padding : .8rem
         } 
     }
    
    </style>
""", unsafe_allow_html=True)

st.title("✨ Market Research & Use Case Generator ✨")

company_name = st.text_input("Enter Company Name", "")

if st.button("Generate Report"):
    # Get company information
    company_info = get_company_info(company_name)
    database.insert_company_info(company_info)

    # Generate AI-based use case
    use_case = generate_use_case(company_info)

    # Use the main theme to find relevant datasets
    main_theme = use_case.get("main_theme")
    datasets = find_datasets(main_theme)

    # Display Company Information in a Readable Format
    st.markdown("<div class='section'><h2>Company Info:</h2>", unsafe_allow_html=True)
    for key, value in company_info.items():
        if key not in ["_id", "section"]:  # Skip the ID and 'section' fields
            st.write(f"**{key.capitalize()}:** {value}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Display Use Case in a Readable Format
    st.markdown("<div class='section'><h2>Use Case:</h2>", unsafe_allow_html=True)
    st.write(f"**Use Case Title:** {use_case.get('use_case', 'N/A')}")
    # st.write(f"**Description:** {use_case.get('description', 'N/A')") 
    st.markdown("</div>", unsafe_allow_html=True)

   
    st.markdown("<div class='section'><h2>Datasets:</h2>", unsafe_allow_html=True)
    if datasets:
        # Create a concise, clickable dataset display
        for i, link in enumerate(datasets):
            st.markdown(
                f"""
                <div style='padding: 12px; margin: 8px 0; border-radius: 6px; background-color: #2c2c3e;'>
                    <h3 style='color: #ff7f50; margin: 0;'>Dataset {i + 1}</h3>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'>Click the link below to access the dataset:</p>
                    <a href="{link}" target="_blank" style='color: #ff7f50; font-size: 1rem; font-weight: 500; text-decoration: none;'>Open Dataset</a><br>
                    <small style='color: #999; font-size: 0.85rem;'>{link}</small>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("No relevant datasets found.")
    st.markdown("</div>", unsafe_allow_html=True)