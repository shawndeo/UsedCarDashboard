
import pandas as pd
from sklearn import linear_model
import streamlit as st

st.title('Used Car Price Estimator')

st.info("""
• Thus far, all data has been collected manually using CarGurus.com. \n
• All vehicles for which data was collected were in the price range of $0 to $30,000. \n
• Filtering options WILL have an impact on coefficients.
""")

data = pd.read_csv('UsedCarsWorking.csv')

st.sidebar.header('Filter')

st.sidebar.warning('None of these filtering options are currently implemented.')

vehicle_body = st.sidebar.selectbox('Body Style: ',
                                        ('All', 'Convertible', 'Coupe', 'SUV'))

if vehicle_body == 'All':
    data = data
elif vehicle_body == 'Coupe':
    data = data[data['Body'] == 'Coupe']
elif vehicle_body == 'Convertible':
    data = data[data['Body'] == 'Convertible']
elif vehicle_body == 'SUV':
    data = data[data['Body'] == 'SUV']

vehicle_drivetrain = st.sidebar.selectbox('Drivetrain: ',
                                            ('All', '4WD', 'AWD', 'FWD', 'RWD'))


if vehicle_drivetrain == 'AWD':
    data = data[data['Drivetrain'] == 'AWD']
elif vehicle_drivetrain == 'FWD':
    data = data[data['Drivetrain'] == 'FWD']
elif vehicle_drivetrain =='RWD':
    data = data[data['Drivetrain'] == 'RWD']

vehicle_engine = st.sidebar.selectbox('Engine: ',
                                        ('All', 'H4', 'H6', 'I4', 'I6', 'V6', 'V8'))

if vehicle_engine == 'All':
    data = data
elif vehicle_engine == 'H4':
    data = data[data['Engine'] == 'H4']
elif vehicle_engine == 'H6':
    data = data[data['Engine'] == 'H6']
elif vehicle_engine == 'I4':
    data = data[data['Engine'] == 'I4']
elif vehicle_engine == 'I6':
    data = data[data['Engine'] == 'I6']
elif vehicle_engine == 'V6':
    data = data[data['Engine'] == 'V6']
elif vehicle_engine == 'V8':
    data = data[data['Engine'] == 'V8']

vehicle_origin = st.sidebar.selectbox('Manufacturer Origin: ',
                                        ('All', 'Germany', 'Italy', 'Japan', 'Korea', 'UK', 'USA'))

if vehicle_origin == 'All':
    data = data
elif vehicle_origin == 'Germany':
    data = data[data['Country'] == 'Germany']
elif vehicle_origin == 'Italy':
    data = data[data['Country'] == 'Italy']
elif vehicle_origin == 'Japan':
    data = data[data['Country'] == 'Japan']
elif vehicle_origin == 'South Korea':
    data = data[data['Country'] == 'South Korea']
elif vehicle_origin == 'UK':
    data = data[data['Country'] == 'UK']
elif vehicle_origin == 'USA':
    data = data[data['Country'] == 'USA']

st.sidebar.header('Features: ')

vehicle_age = st.sidebar.number_input('Model Year: ', 1989, 2022) * -1 + 2021

vehicle_mileage = st.sidebar.number_input('Mileage: ', 0, 500000)

vehicle_manual = st.sidebar.checkbox('Does this vehicle have a manual transmission?')

vehicle_horsepower = st.sidebar.number_input('Horsepower: ', 138, 556)

vehicle_displacement = st.sidebar.slider('Displacement: ', 1.4, 6.2)

vehicle_mpg = st.sidebar.slider('MPG: ', 15, 31)

vehicle_accidents = st.sidebar.checkbox('Does the vehicle have an accident history?')

vehicle_owners = st.sidebar.number_input('Past Owners: ', 1, 7)

vehicle_rental = st.sidebar.checkbox('Was the vehicle ever used as a rental?')

vehicle_fleet = st.sidebar.checkbox('Was the vehicle ever used in a fleet?')

st.header('Original Data: ')

st.dataframe(data)

price_predictor = linear_model.LinearRegression()
price_predictor.fit(data[['Age', 'Mileage', 'ManualTF', 'HP', 'Displacement', 'Combined MPG', 'AccidentsTF', 'Owners', 'Rental Use?', 'Fleet Use?']], data['ListedPrice'])

st.header('Variables')

st.write(f"""
Variable 00: Vehicle Age - {vehicle_age} \n
Variable 01: Mileage - {vehicle_mileage} \n
Variable 02: Is Manual? - {vehicle_manual} \n
Variable 03: Horsepower - {vehicle_horsepower} \n
Variable 04: Displacement - {vehicle_displacement} \n
Variable 05: Combined MPG - {vehicle_mpg} \n
Variable 06: Accident History - {vehicle_accidents} \n
Variable 07: # of Past Owners - {vehicle_owners} \n
Variable 08: Rental History - {vehicle_rental} \n
Variable 09: Fleet History - {vehicle_fleet}
""")

price_predictor.coef_

st.write('Intercept: ')
price_predictor.intercept_
value = price_predictor.predict([[vehicle_age, vehicle_mileage, vehicle_manual, vehicle_horsepower, vehicle_displacement, vehicle_mpg, vehicle_accidents, vehicle_owners, vehicle_rental, vehicle_fleet]])

st.title(f'Estimated Vehicle Worth: ${round(value[0], 2)}')
#st.write(value[0])

st.header('Notes: ')
st.write("""
• 10/20/2021 10:21pm: Added sort features. \n
• 10/20/2021 09:38pm: First iteration. Not surprised there's an inverse relationship between vehicle age and price (-$180 per year).
Mileage has little to no effect but this makes sense because a lot of older cars are sought after regardless of mileage.
A vehicle having a manual transmission has a $3.3k effect on price which makes sense because car enthusiasts seem to LOVE manual transmissions.
Horsepower definitely makes sense (+$60 per HP). Most cheaper / easily accessible vehicles have less horsepower.
Displacement having an inverse relationship as price doesn't really surprise me as much either. Porsches, BMWs, etc tend to stay around 3.0L and are still plenty fast and expensive.
MPG having a correlation (+$70) is no surprise.
Accident history having an inverse relationship makes absolute sense but I was expecting a much more significant impact.
More owners has a negative impact on price (-$79 per owner).
I'm actually surprised at the positive relationship between rental / fleet ownership. Perhaps because these vehicles were professionally kept / expected to be well maintained.
""")

st.write(vehicle_body)

#spam
