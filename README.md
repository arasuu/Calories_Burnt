# Calories_Burnt

Calories Burn Prediction Model

📌 Project Overview

This project aims to predict calories burned during exercise based on key physiological and workout-related factors. By leveraging machine learning, the model provides accurate calorie burn estimations, helping users optimize their workouts for better fitness outcomes.

🎯 Problem Statement

Many individuals struggle to estimate their calories burned during workouts, leading to inefficient exercise routines. This project builds a predictive model using age, height, weight, gender, workout duration, heart rate, and body temperature to offer personalized fitness insights.

🔍 Dataset and Features

Target Variable: Calories burned

Features:

Age

Height

Weight

Gender

Workout Duration

Heart Rate

Body Temperature

🛠️ Technologies and Tools Used

Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost

Machine Learning Models: Decision Trees, Random Forest, Linear Regression, XGBoost

Deployment: Streamlit

🚀 Methodology

Data Preprocessing:

Handled missing values and encoded categorical variables.

Normalized numerical features for better model performance.

Model Training & Evaluation:

Tested multiple models: Decision Trees, Random Forest, Linear Regression, and XGBoost.

Used GridSearchCV for hyperparameter tuning.

Evaluated models using R² Score, MAE, MSE, and RMSE.

Findings:

XGBoost achieved the best performance with the highest accuracy and lowest error.

Heart rate and workout duration showed strong correlations with calorie burn.

📊 Results

Best Model: XGBoost

Performance Metrics:

o	R2 Score: 0.9986863132331905
o	Mean Absolute Error (MAE): 1.5521575984954834
o	Mean Squared Error (MSE): 5.2744122853837005
o	Root Mean Squared Error (RMSE): 2.2966088664340956


🌐 Deployment

The model is deployed using Streamlit, providing an interactive web interface where users can input their details and get real-time calorie burn predictions.

🔥 Future Enhancements

Incorporate additional features such as activity type and intensity level.

Improve model accuracy with more diverse datasets.

Expand deployment for mobile apps and wearable fitness devices.

📌 How to Run the Project

Clone the repository:

git clone https://github.com/your-repo/calories-burn-prediction.git

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Enter your details in the UI and get your calories burned prediction!

🤝 Contributing

Feel free to fork the repository and submit pull requests for improvements!

📜 License

This project is licensed under the MIT License.

🔗 Author: [Your Name]📧 Contact: your.email@example.com🌟 GitHub: [Your GitHub Profile]

