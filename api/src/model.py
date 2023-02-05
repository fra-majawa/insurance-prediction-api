import pickle
from pydantic import BaseModel

class InsuranceExpenseModel(BaseModel):
    age : int
    children: int
    bmi: int
    sex: int
    smoker: int
    northeast: float
    northwest: float
    southeast: float
    southwest: float


### Loading the insurance_expenses model
model_loc = "insurance_expense_model.sav"
insurance_expenses_model = pickle.load(open(model_loc, "rb"))