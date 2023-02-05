from fastapi import FastAPI
import json

from model import InsuranceExpenseModel, insurance_expenses_model 


app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello World"

# @app.post("/data")
# def data(arg: dict()):
#     print(arg)

### Creating the API
@app.post("/insurance_expenses_prediction")
def insurance_prediction(params: InsuranceExpenseModel):
    # print(params)

    data = params.json()
    # print(data)
    input_data = json.loads(data)
    # print(input_data)
    age = input_data["age"]
    children = input_data["children"]
    bmi = input_data["bmi"]
    sex = input_data["sex"]
    smoker = input_data["smoker"]
    northeast = input_data["northeast"]
    northwest = input_data["northwest"]
    southeast = input_data["southeast"]
    southwest = input_data["southwest"]

    list_params = [age, children, bmi, sex, smoker, northeast, northwest, southeast, southwest]
    print("List parameters: ", list_params)

    prediction = insurance_expenses_model.predict([list_params])

    # print(prediction[0])

    return f"{prediction[0]}"