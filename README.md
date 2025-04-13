# 🧠 NexAI Research

<div align="center">
  <h3>🚀 AI Use Case Generator for Products</h3>
  <p>A powerful AI tool that helps companies discover innovative AI use cases for their existing products</p>
</div>

---

## ✨ Features

- 🤖 **AI-Powered Use Cases**: Generate innovative AI implementation ideas for existing products
- 📊 **Market Research**: Analyze potential applications in your industry
- 🔍 **Dataset Discovery**: Find relevant datasets via Kaggle API integration
- 🌐 **Company Analysis**: Automatic information retrieval via web scraping
- 📝 **Use Case Documentation**: Well-structured AI implementation suggestions

## 🛠️ Tech Stack

- 🐍 Python
- 🧠 Cohere API (AI use case generation)
- 📊 Streamlit (UI)
- 📁 Kaggle API (dataset discovery)
- 🔍 BeautifulSoup4 (web scraping)

## 📷 Screenshorts
![Screenshot from 2025-04-13 22-27-13](https://github.com/user-attachments/assets/ed7b772d-ac71-4062-8400-3f65f7cd2682)
![Screenshot from 2025-04-13 22-38-50](https://github.com/user-attachments/assets/19fd72cb-cc7d-41df-9543-c795362dcc61)
![Screenshot from 2025-04-13 22-38-56](https://github.com/user-attachments/assets/1508ab57-dd40-4707-88bc-918bef43f97b)
![Screenshot from 2025-04-13 22-39-01](https://github.com/user-attachments/assets/7378d7cf-33b8-4ac0-8713-ded91f17861c)

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/manojkp08/NexAI_Research.git
cd NexAI_Research

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## ⚙️ Configuration

Before running the tool, update the following in your `.env` file:

```
COHERE_API_KEY=your_cohere_api_key
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_key
```

## 🚀 Usage

```bash
# Start the Streamlit interface
streamlit run app.py
```

## 📋 How It Works

1. **Input Company Information**: Enter your company name and product details
2. **AI Analysis**: The system analyzes your product through Cohere API
3. **Use Case Generation**: Creates innovative AI implementation scenarios
4. **Dataset Discovery**: Finds relevant datasets through Kaggle API
5. **Implementation Plan**: Generates a structured plan for each use case

## 📁 Project Structure

```
NEXAI_RESEARCH/
├── __pycache__/
├── market_research_env/
├── .env
├── .gitignore
├── app.py
├── database.py
├── dataset_finder.py
├── docker-compose.yml
├── Dockerfile.streamlit
├── requirements.txt
├── research_agent.py
└── use_case_generator.py
```

## 🔍 Key Components

- **app.py**: Main Streamlit application interface
- **research_agent.py**: Core AI research orchestration
- **use_case_generator.py**: AI use case generation logic
- **dataset_finder.py**: Kaggle dataset discovery module
- **database.py**: Data storage and retrieval

## 📊 Use Case Examples

- **Predictive Maintenance**: AI monitoring of equipment to predict failures
- **Customer Segmentation**: Advanced clustering for targeted marketing
- **Natural Language Interfaces**: Voice or text interfaces for products
- **Computer Vision Integration**: Visual recognition capabilities
- **Recommendation Systems**: Personalized suggestion engines

---

<div align="center">
  <p>⭐ Star this repository if you find it useful! ⭐</p>
  <p>Made with ❤️ by Manoj</p>
</div>
