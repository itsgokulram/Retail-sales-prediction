import streamlit as st
import datetime as dt
import json
import numpy as np
import pickle

st.set_page_config(page_title = "Retail Sales Price Prediction",
                   page_icon = "",
                   layout = "wide",
                   initial_sidebar_state = "expanded",
                   menu_items = None)

st.title(":blue[Retail Sales Price Prediction]")

def regression_model(test_data):
    with open(r'/Users/gokul/My Apple/vs_code_practice/retail_sales_forecast/rf_regression_model.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = model.predict(test_data)[0]
        return data
    

store_value = [i for i in range(1, 46)]

Type = {'A': 1, "B": 2, 'C': 3}

dept = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
         33, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 
         83, 85, 87, 90, 91, 92, 93, 94, 95, 97, 78, 96, 99, 39, 77, 50, 43, 65, 98]

Size_value = [151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078, 125833, 126512, 207499, 112238, 219622, 200898, 123737,  
              57197, 93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107, 152513, 204184, 206302,  93638,  42988, 203750,
                203007,  39690, 158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221]

holiday = {'No Holiday': 0, 'Super Bowl': 1, 'Labor Day': 2, 'Thanksgiving': 3, 'Christmas': 4}

col1, col2 = st.columns(2, gap= 'large')

with col1:

    date_ = st.date_input('Select the **Date**',  dt.date(2012, 12,5), min_value= dt.date(2010, 2,5), max_value= dt.date.today())

    store = st.selectbox('Select the **Store Number**', store_value)

    type_ = st.selectbox('Select the **Store Type**', ['A', 'B', 'C'])

    department = st.selectbox('Select the **Deparment**', dept, index = 80)

    Size = st.selectbox('Select the **Store Size** in square meter', Size_value)

    fuel = st.number_input('Enter the **Fuel Price** in Dollar', value =3.408, min_value= 1.5, max_value= 10.00)

    temp = st.number_input('Enter the **Temperature** in Celsius', value =151315, min_value= 34875, max_value= 219622)

with col2:

    cpi = st.number_input('Enter the **CPI**', value =172.57, min_value= 126.00, max_value= 250.00)

    unemployment = st.number_input('Enter the **Unempolyment** in Percentage', value =7.66, min_value= 2.00, max_value= 15.00)

    markdown1 = st.number_input('Enter the **MarkDown1** in Dollar', value = 7437.49)

    markdown2 = st.number_input('Enter the **MarkDown2** in Dollar', value = 2517.4)

    markdown3 = st.number_input('Enter the **MarkDown3** in Dollar', value = 1310.9)

    markdown4 = st.number_input('Enter the **MarkDown4** in Dollar', value = 10.00)

    markdown5 = st.number_input('Enter the **MarkDown5** in Dollar', value = 3318)


if markdown1<0 or markdown2<0 or markdown3<0 or markdown4<0 or markdown5<0:
    markup = 1
else: 
    markup = 0

Day = date_.day
Month = date_.month
Year = date_.year
week_number = date_.isocalendar()[1]

holiday = {'No Holiday':0, 'Super Bowl':1, 'Labor Day':2, 'Thanksgiving':3, 'Christmas':4}
if week_number == 6:
    holiday_value = 'Super Bowl'

elif week_number == 36:
    holiday_value = 'Labor Day'

elif week_number == 47:
    holiday_value = 'Thanksgiving'

elif week_number == 51:
    holiday_value = 'Christmas'

else:
    holiday_value = 'No Holiday'

test_data = np.array([[store, Type[type_],  department, Size, temp, fuel, markdown1, markdown2, markdown3, markdown4, markdown5,
                  markup, week_number, holiday[holiday_value], cpi, unemployment, Day, Month, Year]])

st.markdown('Click below button to predict the **Weekly Sales**')
pred = st.button('**Predict**')

if pred:
    # Perform prediction and display result
    predicted_sales = regression_model(test_data)
    st.markdown(f"### :blue[Weekly Sales is] :green[$ {predicted_sales}]")