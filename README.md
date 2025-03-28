## News Article Sorting  

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

## Implementation  

###  Model Training (Jupyter Notebook)  
[News Articles Sorting - Jupyter Notebook](https://github.com/Naveen-jangid/News_Article_Sorting/blob/15aeccaaf214ffbc61865d06df59adc5290f59f4/News_Articles_Sorting.ipynb)  

###  Web Interface & REST API  
[Deployed Web Interface](https://news-article-sorting-754r.onrender.com)  
 
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
![image](https://github.com/user-attachments/assets/37859bd5-9675-416f-b64a-58b42e568fd0)
![image](https://github.com/user-attachments/assets/6c04510c-5d9e-4ae0-be8f-be3b6f44b253)

---

## Documentation  
 **High-Level Overview:** [Google Docs](https://docs.google.com/document/d/1_O5jjssenEaPWzLetzS88bDILzdFb8r3/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true)  
 **Low-Level Documentation:** [Google Docs](https://docs.google.com/document/d/1exAaeCQaQqn2tYfirrgChFdOt94nfBFJ/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true)  
 **System Architecture:** [Architecture Document](https://docs.google.com/document/d/1I9uThHjJJZp4rOPlevdT2o8qovE3ZY3M/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true)  
 **Wireframe & UI Design:** [Wireframe Document](https://docs.google.com/document/d/1Ls6TJ8-FXJeEW14UHHqV4dyKeGoBNbUt/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true)  
 **Project Report:** [Detailed Report](https://docs.google.com/presentation/d/1qZKCw8JrrLZurPeF1NmOJfDCyA6zJTHV/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true)  

---

## Technologies Used  
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
