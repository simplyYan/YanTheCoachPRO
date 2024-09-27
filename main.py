import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from math import pow

def calculate_metrics():
    name = name_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    age = int(age_entry.get())
    gender = gender_combo.get()
    activity_level = activity_combo.get()

    bmi = weight / pow(height, 2)

    if gender == 'Male':
        body_fat_deurenberg = 1.20 * bmi + 0.23 * age - 16.2
    else:
        body_fat_deurenberg = 1.20 * bmi + 0.23 * age - 5.4

    if gender == 'Male':
        body_fat_navy = (1.39 * bmi) + (0.16 * age) - 19.34
    else:
        body_fat_navy = (1.39 * bmi) + (0.16 * age) - 9

    body_fat_percentage = (body_fat_deurenberg + body_fat_navy) / 2

    fat_mass = weight * body_fat_percentage / 100
    lean_mass = weight - fat_mass

    if gender == 'Male':
        bmr_hb = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr_hb = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)

    if gender == 'Male':
        bmr_msj = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr_msj = 10 * weight + 6.25 * height * 100 - 5 * age - 161

    bmr = (bmr_hb + bmr_msj) / 2

    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Extremely active": 1.9
    }
    tdee = bmr * activity_multipliers[activity_level]

    calories_to_lose = tdee - 500
    calories_to_gain = tdee + 500

    protein = weight * 1.8  
    carbs = tdee * 0.55 / 4  
    fat = tdee * 0.25 / 9  

    recommended_water = weight * 35  

    max_heart_rate = 220 - age

    if gender == 'Male':
        ideal_weight = 50 + 2.3 * ((height * 100 - 152.4) / 2.54)
    else:
        ideal_weight = 45.5 + 2.3 * ((height * 100 - 152.4) / 2.54)

    result_label.config(text=f"""
    Name: {name}
    BMI: {bmi:.2f}
    Body Fat Percentage (Avg): {body_fat_percentage:.2f}%
    Lean Mass: {lean_mass:.2f} kg
    Fat Mass: {fat_mass:.2f} kg
    BMR (Avg): {bmr:.2f} kcal/day
    TDEE: {tdee:.2f} kcal/day
    Calories to lose weight: {calories_to_lose:.2f} kcal/day
    Calories to gain weight: {calories_to_gain:.2f} kcal/day
    Recommended Water Intake: {recommended_water:.2f} ml/day
    Recommended Protein: {protein:.2f} g/day
    Recommended Carbs: {carbs:.2f} g/day
    Recommended Fat: {fat:.2f} g/day
    Maximum Heart Rate: {max_heart_rate} bpm
    Ideal Weight: {ideal_weight:.2f} kg
    """)

app = ThemedTk(theme="breeze")
app.title("YanTheCoach Professional")

app.geometry("500x700")
ttk.Style().configure("TButton", font=("Helvetica", 10))

ttk.Label(app, text="Name:").pack(pady=5)
name_entry = ttk.Entry(app)
name_entry.pack()

ttk.Label(app, text="Height (m):").pack(pady=5)
height_entry = ttk.Entry(app)
height_entry.pack()

ttk.Label(app, text="Weight (kg):").pack(pady=5)
weight_entry = ttk.Entry(app)
weight_entry.pack()

ttk.Label(app, text="Age:").pack(pady=5)
age_entry = ttk.Entry(app)
age_entry.pack()

ttk.Label(app, text="Gender:").pack(pady=5)
gender_combo = ttk.Combobox(app, values=["Male", "Female"])
gender_combo.pack()

ttk.Label(app, text="Activity Level:").pack(pady=5)
activity_combo = ttk.Combobox(app, values=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extremely active"])
activity_combo.pack()

calculate_btn = ttk.Button(app, text="Calculate", command=calculate_metrics)
calculate_btn.pack(pady=20)

result_label = ttk.Label(app, text="", font=("Helvetica", 10))
result_label.pack(pady=10)

app.mainloop()