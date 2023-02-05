import streamlit as st
import json
import requests

st.title("Insurance Expense Estimate")

st.header("Welcome to our API Demo")
st.write("""
    - We try to estimate the cost of insurance based on your characteristics.
""")

st.write("- Enter your information below:")


base_url = "http://127.0.0.1:8000"

def make_post(age, children, bmi, sex, smoker, region):
    global base_url
    data = dict()
    print(age, children, bmi, sex, smoker, region)
    data['age'] = int(age)
    data['children'] = int(children)
    data['bmi'] = int(bmi)

    if sex == 'Male':
        sex = 0
    else:
        sex = 1

    if smoker == 'No':
        smoker = 0
    else:
        smoker = 1

    if region == "Northeast":
        northeast = 1
        northwest = 0
        southeast = 0
        southwest= 0
    elif region == "Northwest":
        northeast= 0
        northwest= 1
        southeast = 0
        southwest= 0
    elif region == "Southeast":
        northeast= 0
        northwest= 0
        southeast = 1
        southwest= 0
    else:
        northeast= 0
        northwest= 0
        southeast = 0
        southwest= 1

    # # data_json = json.dumps(data)
    # # print("The data: ", data_json)

    # # response = requests.post(base_url + "/insurance_expenses_prediction/", data=data_json)
    # base_url =  "http://127.0.0.1:8000"

    data = {
        "age" : int(age),
        "children": int(children),
        "bmi": int(bmi),
        "sex": int(sex),
        "smoker": int(smoker),
        "northeast": float(northeast),
        "northwest": float(northwest),
        "southeast": float(southeast),
        "southwest": float(southwest),
    }

    # datum = {
    #     "age" : 45,
    #     "children": 3,
    #     "bmi": 25,
    #     "sex": 1,
    #     "smoker": 1,
    #     "northeast": 1,
    #     "northwest": 0,
    #     "southeast": 0,
    #     "southwest": 0
    # }

    data_json = json.dumps(data)

    print(data_json)

    response = requests.post(base_url + "/insurance_expenses_prediction/", data=data_json)

    # response = requests.get(base_url)

    # print(response.text)

    return response.text

with st.form("my_form"):
    age = st.number_input("Age: ", min_value=0, max_value=100, value=20)
    children = st.number_input("Number of children: ", min_value=0, max_value=10, value=1)
    bmi = st.number_input("BMI: ", min_value=1, max_value=100, value=15)
    sex = st.selectbox("Sex: ", ("Male", "Female"))
    smoker = st.selectbox("Smoker: ", ("Yes", "No"))
    region = st.selectbox("Region: ", ("Northeast", "Northwest", "Southeast", "Southwest"))

    # print(age, children, bmi, sex, smoker, region)

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"""
            Your insurance cost: 
            - ${round(float(make_post(age, children, bmi, sex, smoker, region).replace('"','')), 2)}
        """)




                        
