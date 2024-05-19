import tkinter as tk 
from tkinter import messagebox
import joblib


#Load the trained model
model = joblib.load('bc_model.pkl')


def predict_cancer():
    #Get user inputs
    radius_mean = float(entry1.get())
    texture_mean = float(entry2.get())
    perimeter_mean = float(entry3.get())
    area_mean = float(entry4.get())
    smoothness_mean = float(entry5.get())
    compactness_mean = float(entry6.get())
    concavity_mean = float(entry7.get())
    concave_points_mean = float(entry8.get())
    symmetry_mean = float(entry9.get())
    fractal_dimension_mean = float(entry10.get())

    #Make prediction
    prediction = model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, 
                                 concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])

    #Display prediction
    if prediction == 'B':
        messagebox.showinfo("Prediction", "The tumor is predicted to be Benign")
    else:
        messagebox.showinfo("Prediction", "The tumor is predicted to be Malignant")

def exit_window():
    window.destroy()


window = tk.Tk()
window.title("Breast cancer classification")
window.geometry("1300x900")
window.resizable(False,False)
#window.configure(bg="gray")


tk.Label(window, text="Please fill out the following form for breast cancer prediction", font=("Ariel",20)).grid(row=0, column=0,columnspan=2, padx=10, pady=10)


#Create entry fields
tk.Label(window, text="Cell mean radius", font=("Arial", 20)).grid(row=1, column=0, padx=220, pady=20)
entry1 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry1.grid(row=1, column=1)

tk.Label(window, text="Cell mean texture", font=("Arial", 20)).grid(row=2, column=0, padx=220, pady=20)
entry2 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry2.grid(row=2, column=1)

tk.Label(window, text="Cell mean perimeter", font=("Arial", 20)).grid(row=3, column=0, padx=220, pady=20)
entry3 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry3.grid(row=3, column=1)

tk.Label(window, text="Cell mean area", font=("Arial", 20)).grid(row=4, column=0, padx=220, pady=20)
entry4 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry4.grid(row=4, column=1)

tk.Label(window, text="Cell mean smoothness", font=("Arial", 20)).grid(row=5, column=0, padx=220, pady=20)
entry5 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry5.grid(row=5, column=1)

tk.Label(window, text="Cell mean compactness", font=("Arial", 20)).grid(row=6, column=0, padx=220, pady=20)
entry6 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry6.grid(row=6, column=1)

tk.Label(window, text="Cell mean concavity", font=("Arial", 20)).grid(row=7, column=0, padx=220, pady=20)
entry7 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry7.grid(row=7, column=1)

tk.Label(window, text="Cell mean concave points", font=("Arial", 20)).grid(row=8, column=0, padx=220, pady=20)
entry8 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry8.grid(row=8, column=1)

tk.Label(window, text="Cell mean symmetry", font=("Arial", 20)).grid(row=9, column=0, padx=220, pady=20)
entry9 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry9.grid(row=9, column=1)

tk.Label(window, text="Cell mean fractal dimension", font=("Arial", 20)).grid(row=10, column=0, padx=220, pady=20)
entry10 = tk.Entry(window, bg="#5fa777", font=("Arial", 20), width=30)
entry10.grid(row=10, column=1)



#Prediction button
predict_button = tk.Button(window, text="Predict", bg="#ff7799",width=20,font=("Arial",25), command=predict_cancer)
predict_button.grid(row=11, column=0,  pady=50)

#Exit button
exit_button = tk.Button(window, text="Exit", width=20,font=("Arial",25),bg ="#1fba1f", command = exit_window)
exit_button.grid(row=11, column=1)



window.mainloop()
