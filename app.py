import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import os

def calculate_bmi(weight_kg, height_ft, height_in, gender):
    height_inch_total = height_ft * 12 + height_in
    height_m = height_inch_total * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_exercise_recommendation(bmi_category):
    exercise_recommendations = {
        "Underweight": "Try strength training exercises to build muscle mass.",
        "Normal weight": "Continue doing regular exercises to maintain a healthy weight.",
        "Overweight": "Incorporate cardio exercises like running, cycling, or swimming.",
        "Obese": "Focus on low-impact exercises like walking and gradually increase intensity."
    }
    return exercise_recommendations[bmi_category]

def get_yoga_recommendation(bmi_category):
    yoga_recommendations = {
        "Underweight": "Practice yoga poses that promote digestion and increase appetite.",
        "Normal weight": "Maintain your regular yoga practice for overall well-being.",
        "Overweight": "Engage in yoga poses that help improve metabolism and digestion.",
        "Obese": "Try yoga poses that focus on flexibility and gentle movements."
    }
    return yoga_recommendations[bmi_category]

def get_food_recommendation(bmi_category):
    food_recommendations = {
        "Underweight": "Consume calorie-dense foods like nuts, avocados, and full-fat dairy.",
        "Normal weight": "Maintain a balanced diet with a variety of fruits, vegetables, and plant-based proteins.",
        "Overweight": "Focus on portion control and reduce intake of sugary and fatty foods.",
        "Obese": "Choose nutrient-dense foods and limit processed and high-calorie foods."
    }
    return food_recommendations[bmi_category]

def get_exercise_types(bmi_category):
    exercise_types = {
        "Underweight": ["Weightlifting", "Resistance training", "Yoga"],
        "Normal weight": ["Cardio exercises", "Swimming", "Hiking"],
        "Overweight": ["Running", "Cycling", "Dancing"],
        "Obese": ["Low-impact aerobics", "Walking", "Pilates"]
    }
    return exercise_types[bmi_category]

def get_yoga_types(bmi_category):
    yoga_types = {
        "Underweight": ["Bhujangasana (Cobra Pose)", "Vajrasana (Diamond Pose)", "Pavanamuktasana (Wind-Relieving Pose)"],
        "Normal weight": ["Tadasana (Mountain Pose)", "Virabhadrasana (Warrior Pose)", "Balasana (Child's Pose)"],
        "Overweight": ["Ardha Matsyendrasana (Half Lord of the Fishes Pose)", "Naukasana (Boat Pose)", "Utkatasana (Chair Pose)"],
        "Obese": ["Baddha Konasana (Butterfly Pose)", "Setu Bandhasana (Bridge Pose)", "Sukhasana (Easy Pose)"]
    }
    return yoga_types[bmi_category]

def get_pranayama(bmi_category):
    pranayama = {
        "Underweight": ["Kapalabhati Pranayama", "Bhastrika Pranayama", "Anulom Vilom Pranayama"],
        "Normal weight": ["Sheetali Pranayama", "Bhramari Pranayama", "Nadi Shodhana Pranayama"],
        "Overweight": ["Ujjayi Pranayama", "Surya Bhedana Pranayama", "Shitali Pranayama"],
        "Obese": ["Bhramari Pranayama", "Nadi Shodhana Pranayama", "Kapalabhati Pranayama"]
    }
    return pranayama[bmi_category]

def get_food_list(bmi_category):
    food_list = {
        "Underweight": ["Almonds", "Avocado", "Greek yogurt", "Quinoa", "Lentils"],
        "Normal weight": ["Apples", "Broccoli", "Oats", "Spinach", "Chickpeas"],
        "Overweight": ["Berries", "Cauliflower", "Brown rice", "Kale", "Black beans"],
        "Obese": ["Chia seeds", "Lentils", "Sweet potatoes", "Beets", "Quinoa"]
    }
    return food_list[bmi_category]

# Function to crop image in circular shape
def crop_to_circle(image):
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

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

        st.subheader("Exercise Types")
        exercise_types = get_exercise_types(bmi_category)
        st.write(exercise_types)

        st.subheader("Yoga Recommendation")
        yoga_recommendation = get_yoga_recommendation(bmi_category)
        st.write(yoga_recommendation)

        st.subheader("Yoga Types")
        yoga_types = get_yoga_types(bmi_category)
        st.write(yoga_types)

        st.subheader("Pranayama Recommendation")
        pranayama_recommendation = get_pranayama(bmi_category)
        st.write(pranayama_recommendation)

        st.subheader("Food Recommendation")
        food_recommendation = get_food_recommendation(bmi_category)
        st.write(food_recommendation)

        st.subheader("Food List")
        food_list = get_food_list(bmi_category)
        st.write(food_list)

if __name__ == "__main__":
    main()
