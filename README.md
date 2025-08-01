# BMI Calculator and Recommendations
https://getbmi.streamlit.app/  
This is a Streamlit app that calculates Body Mass Index (BMI) and provides exercise, yoga, pranayama, and food recommendations based on the BMI category.

# Introduction
The BMI Calculator and Recommendations app is designed to help users calculate their BMI and get personalized health recommendations based on their BMI category. The app takes inputs such as weight in kilograms, height in feet and inches, and gender to calculate BMI. It then categorizes the BMI into four categories: "Underweight," "Normal weight," "Overweight," and "Obese." Based on the BMI category, the app provides exercise types, yoga poses, pranayama techniques, and food recommendations to maintain or improve their health.

## Installation and Setup

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
cd bmi-calculator-app
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Place your profile picture named `a.png` and background music named `music.mp3` in the same directory as the `app.py` script.

4. Run the Streamlit app:
   
```bash
streamlit run app.py
```

Access the app in your web browser at http://localhost:8501.

Enter your weight in kilograms, height in feet and inches, and select your gender.

Click the "Calculate" button to get your BMI and personalized health recommendations.

# Features
Calculate BMI based on weight and height inputs.
Categorize BMI into four categories: "Underweight," "Normal weight," "Overweight," and "Obese."
Display personalized exercise recommendations based on BMI category.
Provide yoga poses recommendations based on BMI category.
Suggest pranayama techniques based on BMI category.
Recommend foods to maintain or improve health based on BMI category.

# Technologies Used
Python
Streamlit
PIL (Python Imaging Library)


# Note:
The BMI Calculator and Recommendations app is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult a healthcare professional before making any significant changes to your diet or exercise routine.
