import joblib
import streamlit as st
import numpy as np

# loading the trained model
loaded_model = joblib.load('model_classifier_rf.pkl')

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope):

 # Pre-processing user input    
    if Sex == "M":
        Sex = 0
    else:
        Sex = 1
 
    if ChestPainType == "TA":
        ChestPainType = 0
    elif ChestPainType == "ATA":
        ChestPainType = 1
    elif ChestPainType == "NAP":
        ChestPainType = 2
    elif ChestPainType == "ASY":
        ChestPainType = 3

    if RestingECG == "Normal":
        RestingECG = 0
    elif RestingECG == "ST":
        RestingECG = 1
    elif RestingECG == "LVH":
        RestingECG = 2

    if ExerciseAngina == "N":
        ExerciseAngina = 0
    elif ExerciseAngina == "Y":
        ExerciseAngina = 1
   
    if ST_Slope == "Up":
        ST_Slope = 0
    elif ST_Slope == "Flat":
        ST_Slope = 1
    elif ST_Slope == "Down":
        ST_Slope = 2
 
    # Making predictions 
    
    prediction = loaded_model.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope]])
     
    if prediction == 0:
        pred = 'Yeayyy anda sehat, jangan lupa tetap jaga kesehatan!'
    else:
        pred = 'Anda terdeteksi menderita penyakit jantung, ayo segera periksa ke dokter dan jangan lupa tetap jaga kesehatan!'
    return pred
      
  
    # this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    st.title("Deploying machine learning models to predict heart disease")
    st.subheader("made by : Indah Sulistiya")
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:grey;text-align:center;">HEART DISEASE PREDICTION</h1> 
    <h2 style ="color:grey;text-align:center;">ayo prediksi kesehatan jantung anda!</h2> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    st.subheader("Umur (diisi dalam tahun)")
    Age = st.number_input("umur")
    
    st.subheader("Jenis Kelamin")
    ("keterangan --> M = Laki-laki, F = Perempuan")
    Sex = st.radio('Jenis Kelamin',("M","F"))
    
    st.subheader("Resting Blood Pressure (Tekanan Darah saat Istirahat [mm/Hg])")
    RestingBP = st.number_input("Resting Blood Pressure")
    
    st.subheader("Kadar Kolesterol [mm/dl])")
    Cholesterol = st.number_input("Kadar Cholesterol")
    
    st.subheader("Max Heart Rate (Detak jantung maksimum [60-202])")
    MaxHR = st.number_input("Max Heart Rate")
    
    st.subheader("Chest Pain Type (Type Nyeri Dada)")
    ("keterangan --> TA = nyeri dada khas, ATA = nyeri dada tidak khas, NAP = tidak nyeri dada, ASY = asimtomatik")
    ChestPainType = st.radio('Chest Pain Type',("TA", "ATA", "NAP", "ASY"))
    
    st.subheader("Resting Electrocardiogram (tes diagnostik umum yang digunakan untuk menmeriksa fungsi jantung termasuk aktivitas kelistrikannya)")
    ("keterangan --> Normal = normal, ST = memiliki kelainan gelombang ST-T (gelombang T inversi dan/atau peningkatan atau penurunan ST > 0,05 mV), LVH = menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri berdasarkan kriteria Estes")
    RestingECG = st.radio('Resting Electrocardiogram',("Normal","ST","LVH"))
    
    st.subheader("Fasting Blood Sugar (Gula darah saat istirahat)")
    ("keterangan --> 1 = jika Gula darah saat istirahat > 120 mg/dl, 0 =  lainnya")
    FastingBS = st.radio('Fasting Blood Sugar',(0,1))
    
    st.subheader("Exercise-induced Angina (nyeri dada akibat olahraga)")
    ("keterangan --> N = tidak, Y= iya")
    ExerciseAngina = st.radio('Exercise-induced Angina',("N","Y"))
    
    st.subheader("Old peak (depresi ST yang diakibatkan oleh latihan relative terhadap saat istirahat)")
    ("keterangan --> diisi dalam angka desimal")
    OldPeak = st.number_input("Old peak")
    
    st.subheader("ST Slope (Kemiringan segmen latihan puncak ST)")
    ("keterangan --> Up = upsloping, Flat = flat, Down = downsloping")
    ST_Slope = st.radio('ST Slope',("Up","Flat","Down"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("predict"): 
        result = prediction(Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope) 
        st.success('Hasil Prediksi Kesehatan Jantung Anda Adalah : {}'.format(result))
        
        
        st.balloons()
     
if __name__=='__main__': 
    main()