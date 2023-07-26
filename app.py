import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import os
from IPython.display import Audio

def calculate_bmi(weight_kg, height_ft, height_in, gender):
    height_inch_total = height_ft * 12 + height_in
    height_m = height_inch_total * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    # Your implementation of BMI categories

def get_exercise_recommendation(bmi_category):
    # Your implementation of exercise recommendations

def get_yoga_recommendation(bmi_category):
    # Your implementation of yoga recommendations

def get_food_recommendation(bmi_category):
    # Your implementation of food recommendations

# Function to crop image in circular shape
def crop_to_circle(image):
    # Your implementation of the crop function

# Streamlit App
def main():
    st.title("BMI Calculator and Recommendations")

    # Load the user's profile image
    profile_image = Image.open("a.png")
    profile_image = crop_to_circle(profile_image)

    # Display the profile image in the sidebar
    st.sidebar.image(profile_image, use_column_width=True)

    # Add background music from the current directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    audio_file_path = os.path.join(base_path, "music.mp3")
    audio_file = open(audio_file_path, "rb")
    audio_bytes = audio_file.read()

    # Use IPython to automatically play audio without user interaction
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    weight_kg = st.number_input("Enter your weight in kg", min_value=1.0, step=0.1)
    height_ft = st.number_input("Enter your height in feet", min_value=1, step=1)
    height_in = st.number_input("Enter the remaining height in inches", min_value=0, max_value=11, step=1)
    gender = st.selectbox("Select your gender", ["Male", "Female"])

    if st.button("Calculate"):
        bmi = calculate_bmi(weight_kg, height_ft, height_in, gender)
        st.write(f"Your BMI: {bmi:.2f}")

        bmi_category = get_bmi_category(bmi)
        st.write(f"Category: {bmi_category}")

        st.subheader("Exercise Recommendation")
        exercise_recommendation = get_exercise_recommendation(bmi_category)
        st.write(exercise_recommendation)

        st.subheader("Yoga Recommendation")
        yoga_recommendation = get_yoga_recommendation(bmi_category)
        st.write(yoga_recommendation)

        st.subheader("Food Recommendation")
        food_recommendation = get_food_recommendation(bmi_category)
        st.write(food_recommendation)

if __name__ == "__main__":
    main()
