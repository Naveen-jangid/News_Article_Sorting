News Article Sorting  

## Abstract  
In today’s digital era, the internet is flooded with vast amounts of news from various sources. With the ever-growing demand for information, **automated news classification** is crucial to help users access relevant content efficiently.  

This project presents a **machine learning-based news classification model** that categorizes articles into **five categories**:  
- **Business**  
- **Entertainment**  
- **Politics**  
- **Sport**  
- **Tech**  

We used a **labeled dataset from BBC News (1,490 articles)** and experimented with various machine learning algorithms. Our evaluation revealed that **Complement Naïve Bayes (CNB) performs the best**, achieving:  
 **Precision** > 95%  
 **Recall** > 98%  
 **F1-score** > 97%  
 **Overall accuracy**: **98%**  

## Problem Statement  
Data is a valuable resource, and news organizations store vast amounts of it. The challenge is to extract insights that enhance decision-making and user experience. **Manually sorting news articles is time-consuming**, so an **automated classification system** can:  
- Identify topics of interest  
- Suggest relevant news articles  
- Organize content effectively  

By leveraging **machine learning**, we can efficiently classify articles into predefined categories, enabling **better news recommendations and insights**.  

## Solution  
We trained and tested multiple machine learning models on a **public BBC News dataset** and found that **Complement Naïve Bayes** consistently outperformed other models. This classifier provides **high precision, recall, and F1-score**, making it ideal for **real-time classification tasks**.  

 **Dataset Used:** BBC News Classification  
 **Dataset URL:** [Kaggle - BBC News](https://www.kaggle.com/c/learn-ai-bbc/data)  

###  Dataset Details  
- **ArticleId** - Unique identifier for each record  
- **Article** - News article text  
- **Category** - Label of the article (**Tech, Business, Sport, Entertainment, Politics**)  

## 🏗 Implementation  

###  Model Training (Jupyter Notebook)  
[News Articles Sorting - Jupyter Notebook](https://github.com/ujjwalkar0/News-Article-Sorting/blob/main/Notebook/News%20Articles%20Sorting.ipynb)  

###  Web Interface & REST API  
[Deployed Web Interface](https://github.com/Uncoded-AI/Website/)  
 
---

## Installation & Setup  

### Clone the Repository  
```bash
git clone https://github.com/yourusername/news-article-sorting.git
cd news-article-sorting
```

### Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Run Locally  
```bash
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.  

---

## Deployment on Render  

### 1️ Push to GitHub  
```bash
git add .
git commit -m "Initial commit"
git push origin main
```
### 2️ Deploy on Render  
- Go to **[Render](https://render.com/)**  
- Create a new **Web Service**  
- Connect your GitHub repository  
- Set the **Start Command**:  
  ```bash
  gunicorn app:app
  ```
- Click **Deploy**  

---

## API Usage  

### **POST /predict**  
#### **Request:**  
```json
{
  "text": "Enter your news article here..."
}
```
#### **Response:**  
```json
{
  "prediction": "Business"
}
```

---

## Documentation  
 **High-Level Overview:** [Google Docs](https://docs.google.com/document/d/1f4_BJspf6wXsawMi1vHoZkMkk4PWjFlPsZHTI2_bP-E/edit?usp=sharing)  
 **Low-Level Documentation:** [Google Docs](https://docs.google.com/document/d/1n0RJkNYiCL0B-QmsyrFOrA6blMN4L5ELcA2IBU7fGjU/edit?usp=sharing)  
 **System Architecture:** [Architecture Document](https://docs.google.com/document/d/1QlN0c_42aEuHt3pdqmaKYR5gsiQbyJvYRwRLL3E3F3Y/edit?usp=sharing)  
 **Wireframe & UI Design:** [Wireframe Document](https://docs.google.com/document/d/1bx3jvYHALnrLafYu9zvsOHpIUuvJNixxue7Ta968AXU/edit?usp=sharing)  
 **Project Report:** [Detailed Report](https://docs.google.com/presentation/d/1RGH8av_n46_2G2Kv7Ta1wzvdRq097lw-/edit?usp=sharing)  

---

## 🛠 Technologies Used  
- **Python**   
- **Flask**   
- **Machine Learning (Naïve Bayes, TF-IDF)**   
- **Render (for deployment)**   
- **Gunicorn (for production server)**   

---

##  Contributing  
Contributions are welcome! Feel free to:  
- Submit issues   
- Suggest improvements   
- Fork and enhance the project   

---

## License  
This project is open-source under the **MIT License**.  

**For any queries, feel free to reach out!** 

---
