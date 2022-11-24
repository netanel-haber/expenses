from enum import Enum
from typing import Dict
import pandas as pd

class HebrewCategory(str, enum):
    DIRECT = "דירקט"
    DIRECT_BATCHED = "דירקט- מצטבר"
    CREDIT_CARD = "מקס איט פיננסי"
    SALARY = "משכורת"
    SALARY_NET = "משכורת-נט"
    BIT = "bit העברת כסף"
    UNEMPLOYMENT = "בטוח לאומי חד"
    IB = "אינטראקטיב ברוקרס אל אל"
    CHECK = "שיק"

class Category(str, Enum):
    Direct = "direct"
    CreditCard = "credit card"
    Salary = "salary"
    Bit = "bit"
    Unemployment = "unemployment"
    IB = "IB"


class Col(str, Enum):
    Date = "Date"
    Balance = "Balance"
    Minus = "Minus"
    Plus = "Plus"
    For = "For"
    Action = "Action"
    Origin = "Origin"
    Executor = "Executor"

straight_forward_replacments: Dict[HebrewCategory, Category] = {

} 


df = pd.read_csv("balance.csv")


def find_sub_replace_all(df, term, to):
    return df.replace(rf"(^.*{term}.*$)", to)

df.loc[df[Col.Executor] == IB, Col.Action] = "IB"

df = df.replace(
    {
        DIRECT: "direct",
        DIRECT_BATCHED: "direct",
        CREDIT_CARD: "credit card",
        SALARY: "salary",
        SALARY_NET: "salary",
        BIT: "bit",
        UNEMPLOYMENT: "unemployment",
        IB: "IB",
        
    }
)
df = find_sub_replace_all(df, "שכר דירה", "rent")



df.to_csv("balance-transformed.csv")