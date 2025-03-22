from flask import Flask, request, render_template
import joblib

# Load trained model and vectorizer
model = joblib.load("cnb.pk")
vectorizer = joblib.load("TfIdf_Vectorizer.pk")

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>News Classifier</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
                font-family: Arial, sans-serif;
            }
            .container {
                max-width: 600px;
                margin-top: 50px;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            textarea {
                width: 100%;
                height: 150px;
                resize: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2 class="text-center">News Article Classifier</h2>
            <form action="/predict" method="post">
                <div class="mb-3">
                    <label for="article" class="form-label">Enter Your Article</label>
                    <textarea name="text" id="article" class="form-control"></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">Classify</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get("text")
    
    if not text:
        return "<h3>Error: No text provided</h3>", 400
    
    # Transform input text
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    
    return f'''
    <html>
    <head>
        <title>Prediction Result</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="d-flex justify-content-center align-items-center" style="height:100vh; background-color: #f8f9fa;">
        <div class="container text-center">
            <h2>Predicted Category</h2>
            <div class="alert alert-success" role="alert">
                {prediction[0]}
            </div>
            <a href="/" class="btn btn-secondary">Go Back</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)