### **README.md: MindKet Intelligence Engine**

This README provides a technical overview and setup guide for **MindKet**, an automated competitor intelligence platform designed to transform raw e-commerce and social media data into actionable business insights.

---

## **1. Project Overview**
**MindKet** is an end-to-end data science solution that correlates competitor pricing strategies with customer sentiment. By integrating **Transformers**, **Deep Learning**, and **Machine Learning**, the system identifies market gaps and predicts price elasticity to help businesses optimize their revenue.

## **2. Key Features**
*   **Automated ETL Pipeline:** Uses Apache Airflow to orchestrate scrapers that collect structured price data and unstructured reviews.
*   **Multi-Modal Analysis:**
    *   **Transformers (BERT/RoBERTa):** Fine-tuned for Aspect-Based Sentiment Analysis (ABSA) on reviews.
    *   **Deep Learning (LSTM):** Forecasts historical price trends and identifies cyclical market patterns.
    *   **Machine Learning (XGBoost):** Classifies "Competitor Threat Levels" based on price-to-sentiment correlations.
*   **Interactive Dashboard:** A professional GUI featuring trend visuals, sentiment heatmaps, and automated weekly reports.

## **3. Tech Stack**
*   **Language:** Python 3.13.3
*   **Database:** PostgreSQL (Star Schema design)
*   **Orchestration:** Apache Airflow
*   **ML/DL Frameworks:** TensorFlow, Hugging Face Transformers, Scikit-learn, XGBoost
*   **Frontend:** Streamlit or React

## **4. System Architecture**
1.  **Extraction:** Scrapy and BeautifulSoup scripts target business profiles and e-commerce sites.
2.  **Transformation:** Preprocessing involves tokenization for NLP and normalization for numerical price data.
3.  **Loading:** Data is stored in PostgreSQL for historical tracking and analysis.
4.  **Inference:** Models process the cleaned data to generate popularity scores and growth metrics.

## **5. Setup & Installation**

### **Prerequisites**
*   PostgreSQL installed and running.
*   Python environment (Anaconda or venv recommended).

### **Installation Steps**
```
# Clone the repository
git clone https://github.com/nhs-shah/market-intell.git

# Navigate to project directory
cd market-intell

# Install required dependencies
pip install -r requirements.txt

# Setup the database schema
python scripts/setup_db.py

# Launch the Airflow scheduler
airflow scheduler

# Run the dashboard
npm dev run
```

## **6. Implementation Results**
The system is designed to visualize significant market shifts, such as a **15% drop in product popularity** followed by recovery trends through 2026. Users can generate weekly PDF reports summarizing customer feedback and competitor growth.

## **7. Future Enhancements**
*   **Image Analytics:** Analyzing competitor branding imagery using Computer Vision.
*   **Real-time Alerts:** WhatsApp/Email integration for instant price change notifications.

---

**Developer:** Noor Hassan Shah (norson)  
**Affiliation:** BS Data Science, SMIU
