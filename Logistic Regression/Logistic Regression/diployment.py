import pickle
import pandas as pd
import streamlit as st

# loading model
regression_model=pickle.load(open('regressor.pkl','rb'))

# prediction
def prediction(Passengerid,Pclass,Sex,Age,SibSp,Parch,Embarked):
    if Sex == "Male":
        Sex = 0
    else:
        Sex = 1
    if Embarked == "Cherbourg":
        Embarked = 0
    elif Embarked == "Queenstown":
        Embarked = 1   
    else:
        Embarked=2
    data=pd.DataFrame({'PassengerId':[Passengerid],
          'Pclass':[Pclass],
          'Sex':[Sex],
          'Age':[Age],
          'SibSp':[SibSp],
          'Parch':[Parch],
          'Embarked':[Embarked]
          })

# Make predictions
    prediction=regression_model.predict(data)
    if prediction==0:
        pred='Passenger is Dead'
    else:
        pred='Passenger is Alive'
    return pred

def main():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#42f590;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Survival Prediction of Titanic passengers</h1> 
    </div> 
    """
    
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # data required for prediction
    Passengerid=st.number_input(label='Enter the passenger Id',min_value=0,max_value=900)
    Pclass=st.slider(label="Select the passenger class",min_value=1,max_value=3)
    st.text(f'Selected:{Pclass}')
    Sex=st.selectbox('Gender',("Male","Female"))
    Age=st.number_input(label="Enter passenger's age",min_value=0,max_value=80)
    SibSp=st.slider("Select siblings/spouse",0,8)
    st.text(f'Selected:{SibSp}')
    Parch=st.slider("Select parent/childern",0,6)
    st.text(f'Selected:{Parch}')
    Embarked=st.selectbox("Port of Embarkation ",['Cherbourg','Queenstown','Southampton'])
    result=''

    # when predict is clicked,make predictionand store it
    if st.button("Get status"):
        result=prediction(Passengerid,Pclass,Sex,Age,SibSp,Parch,Embarked)
        st.success(result)

if __name__=='__main__':
   main()