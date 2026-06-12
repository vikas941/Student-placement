
import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("../placement_model.pkl", "rb"))

# Page Config
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Placement Prediction System")
st.write("Enter student details and predict placement chances")

# Input Fields

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.5
)

internships = st.number_input(
    "Internships",
    min_value=0,
    max_value=10,
    value=1
)

projects = st.number_input(
    "Projects",
    min_value=0,
    max_value=20,
    value=2
)

workshops = st.number_input(
    "Workshops / Certifications",
    min_value=0,
    max_value=20,
    value=1
)

aptitude = st.number_input(
    "Aptitude Test Score",
    min_value=0,
    max_value=100,
    value=75
)

softskills = st.number_input(
    "Soft Skills Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.0
)

extra = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

training = st.selectbox(
    "Placement Training",
    ["No", "Yes"]
)

ssc = st.number_input(
    "SSC Marks",
    min_value=0,
    max_value=100,
    value=70
)

hsc = st.number_input(
    "HSC Marks",
    min_value=0,
    max_value=100,
    value=75
)

# Convert Yes/No to 0/1

extra = 1 if extra == "Yes" else 0
training = 1 if training == "Yes" else 0

# Prediction Button

if st.button("Predict Placement"):

    data = pd.DataFrame([[
        cgpa,
        internships,
        projects,
        workshops,
        aptitude,
        softskills,
        extra,
        training,
        ssc,
        hsc
    ]], columns=[
        "CGPA",
        "Internships",
        "Projects",
        "Workshops/Certifications",
        "AptitudeTestScore",
        "SoftSkillsRating",
        "ExtracurricularActivities",
        "PlacementTraining",
        "SSC_Marks",
        "HSC_Marks"
    ])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is likely to be Not Placed")

    st.write(
        f"Placement Probability: {probability*100:.2f}%"
    )


