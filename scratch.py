import streamlit as st
import itertools
import pandas as pd
from itertools import combinations

@st.cache
def r_subset(arr, r):
    return list(combinations(arr, r))

def Convert(string):
    li=list(string.split(",",))
    return li

siteHeader=st.container()
appSelection=st.container()


with siteHeader:
    st.title('Occupancy detection technology selection tool')
    st.text('With this tool you can find out which occupancy sensing technology best suits your '
            'facility management application needs')
with appSelection:
    info_app={'Occ_Res':[4,4,2,3,3,3,2,1,2,1,1,2,2,2],
              'Spatial_Res':[3,3,2,3,3,2,3,2,2,3,4,2,2,2],
              'Accuracy':[3,3,2,3,3,3,2,1,1,3,2,1,1,1],
              }
    info_app_1={'Occ_Res':['Tracking','Tracking','Count','Identity','Identity','Identity','Count','Presence','Count','Presence','Presence','Count','Count','Count'],
              'Spatial_Res':['Room','Room','Floor','Room','Room','Floor','Room','Floor','Floor','Room','Workstation','Floor','Floor','Floor'],
              'Accuracy':['High','High','Medium','High','High','High','Medium','Low','Low','High','Medium','Low','Low','Low'],
              }
    columns=['Occ_Res','Spatial_Res','Accuracy']
    df=pd.DataFrame(data=info_app,columns=columns,index=['Emergency evacuation and rescue','Disease control','Space utilization rate','Access control','Intrusion detection',
        'Surveillance','Smart cleaning','Heating/cooling control','Demand control ventilation','Lighting control','Smart plugs','Heating/cooling energy usage','Lighting energy usage','Plug load energy usage'])
    df_1=pd.DataFrame(data=info_app_1,columns=columns,index=['Emergency evacuation and rescue','Disease control','Space utilization rate','Access control','Intrusion detection',
        'Surveillance','Smart cleaning','Heating/cooling','Demand control ventilation','Lighting control','Smart plugs','Heating/cooling energy usage','Lighting energy usage','Plug load energy usage'])

    info_sensor_0 = {
        'Occ_Res': [1, 2, 3, 4, 4, 2, 1, 2, 1],
        'Spatial_Res': [4, 4, 4, 4, 3, 3, 3, 3, 3],
        'Accuracy': [1, 3, 3, 3, 3, 2, 1, 1, 1],
        'Privacy': [3, 3, 1, 1, 1, 3, 3, 3, 3],
        'Cost': [1, 3, 3, 1, 2, 1, 1, 1, 1]}
    info_sensor_1 = {
        'Occ_Res': ['Presence', 'Count', 'Identity', 'Tracking', 'Tracking', 'Count', 'Presence', 'Count','Presence'],
        'Spatial_Res': ['Workstation', 'Workstation', 'Workstation', 'Workstation', 'Room', 'Room', 'Room', 'Room','Room'],
        'Accuracy': ['Low', 'High', 'High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low'],
        'Privacy': ['High', 'High', 'Low', 'Low', 'Low', 'High', 'High', 'High', 'High'],
        'Cost': ['Low', 'High', 'High', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low']}

    columns_sensor = ['Occ_Res', 'Spatial_Res', 'Accuracy', 'Privacy', 'Cost']
    df_0 = pd.DataFrame(data=info_sensor_0, columns=columns_sensor,
                        index=['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera','Optical camera',
                               'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters', 'Door', 'CO2','Piezoelectric'])
    df1_1 = pd.DataFrame(data=info_sensor_1, columns=columns_sensor,
                         index=['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera','Optical camera',
                                'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters', 'Door', 'CO2','Piezoelectric'])

Menu_Items = ["View all sensors", "Select single type of sensor based on application criteria",
                  "Select combination of sensors based on application criteria"]
with st.form(key="Selecting columns"):
    q1 = st.multiselect('Select facility management application(s)', df_1.index)
    Menu_Choices = st.selectbox('Select the options', Menu_Items)
    submit_button = st.form_submit_button(label='Update')
    if submit_button:
        result_1 = df_1.loc[q1]
        app_selected=pd.DataFrame(data=result_1,columns=columns)
        app_selected.update(df)

        max_occ_res = app_selected.Occ_Res.max()
        max_spatial_res = app_selected.Spatial_Res.max()
        max_acc = app_selected.Accuracy.max()

        min_occ_res = app_selected.Occ_Res.min()
        min_spatial_res = app_selected.Spatial_Res.min()
        min_acc = app_selected.Accuracy.min()

        if Menu_Choices == "View all sensors":
            st.write("Below are all the sensors Available")
            st.dataframe(df1_1)
        if Menu_Choices == "Select single type sensor based on application criteria":
            filter_table1 = df_0.loc[(df_0['Occ_Res'] >= max_occ_res) & (df_0['Accuracy'] >= max_acc) & (
                        df_0['Spatial_Res'] >= max_spatial_res)]
            filter_table1.update(df1_1)
            st.dataframe(filter_table1)

        if Menu_Choices == "Select combination of sensors based on application criteria":
            info_sensor_0 = {'Sensor': ['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera', 'Optical camera',
                           'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters', 'Door/CO2', 'Piezoelectric'],
                            'Occ_Res': [2, 2, 3, 3, 3, 2, 2, 1],
                            'Spatial_Res': [4, 4, 4, 3, 3, 3, 3, 4],
                            'Accuracy': [1, 3, 3, 3, 3, 2, 1, 1],
                            'Privacy': [3, 3, 1, 1, 1, 3, 3, 3],
                            'Cost': [1, 3, 3, 1, 2, 1, 1, 1]}
            columns_0 = ['Sensor', 'Occ_Res', 'Spatial_Res', 'Accuracy', 'Privacy', 'Cost']
            df_0 = pd.DataFrame(data=info_sensor_0, columns=columns_0,
                                index=['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera',
                                       'Optical camera', 'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters',
                                       'Door/CO2', 'Piezoelectric'])
            min_table = df_0.loc[(min_occ_res <= df_0['Occ_Res']) & (min_acc <= df_0['Accuracy']) & (
                        min_spatial_res <= df_0['Spatial_Res'])]
            sensor = min_table['Sensor']
            min_table = df_0.loc[(min_occ_res <= df_0['Occ_Res']) & (min_acc <= df_0['Accuracy']) & (
                        min_spatial_res <= df_0['Spatial_Res'])]

            for f in range(len(sensor) + 1):  # iterate number of items in combination
                if f >= 2:
                    for i in r_subset(sensor, f):  # iterate over every combination
                        is_ok = False
                        for key in i:  # iterate over any item in a combination
                            multi_row = min_table[min_table['Sensor'].isin(Convert(key))]
                            value_occ_res = multi_row.Occ_Res.item()
                            value_spatial_res = multi_row.Spatial_Res.item()
                            value_acc = multi_row.Accuracy.item()
                            if (value_occ_res >= max_occ_res) and (value_spatial_res <= max_spatial_res) and (
                                    value_acc <= max_acc):  # pick any item in a  combination that meets the criteria
                                is_ok = True
                        if is_ok:
                            info = df_0.loc[i, :]
                            info = info.drop(columns='Sensor')
                            info.update(df1_1)
                            st.dataframe(info)



