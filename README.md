📺 OTT Platforms Analysis Dashboard
Overview

The OTT Platforms Analysis Dashboard is an interactive data analysis project developed using Python and Streamlit. It analyzes popular OTT platforms based on various attributes such as monthly active users, subscription prices, ratings, content types, and video quality.

The dashboard enables users to explore the dataset through interactive visualizations and compare different OTT platforms.

Features
🏠 Interactive Home Dashboard
🗂️ Dataset Exploration
🌞 Sunburst Visualization
💰 Subscription Price vs Monthly Active Users Comparison
📊 Interactive Filters
📈 Plotly Visualizations
🖥️ Responsive Streamlit Interface
Technologies Used
Python
Streamlit
Pandas
Plotly
Matplotlib
Dataset

The project uses datasets containing information about OTT platforms, including:

Platform Name
Monthly Active Users
Subscription Price
Rating
Content Type
Video Quality

Additional datasets:

Amazon Prime Titles
Netflix Titles
Project Structure
OTT-Analysis-Dashboard/
│
├── Datasets/
│   ├── OTT_Platforms.csv
│   ├── amazon_prime_titles.csv
│   └── netflix_titles.csv
│
├── Home.py
├── Dataset.py
├── Visualization.py
├── Comparison.py
├── app.py
├── images.jpg
├── requirements.txt
├── README.md
└── .gitignore
Installation
Clone the repository.
Install the required libraries:
pip install -r requirements.txt
Run the Streamlit application:
streamlit run app.py
Dashboard Pages
🏠 Home
🗂️ Dataset
🌞 Visualization
💰 Comparison
Future Improvements
Add more OTT platforms
Perform advanced data cleaning
Include additional visualizations
Add real-time data integration
Build predictive analytics using machine learning
Author

Piya Kapoor

B.Tech Computer Science Engineering

License

This project is developed for educational and portfolio purposes.