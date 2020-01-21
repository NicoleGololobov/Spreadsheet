from simple_salesforce import Salesforce
import pandas as pd

# username in SF
myUser = "user@company.com"
# password, which will be prompted for (Note: password will be visible)
myPass = input("Password: ")
# security token, which is on SF profile, can also reset it
myToken = "token"

# log into SF
sf = Salesforce(username=myUser, password=myPass, security_token=myToken)

# read file into a pandas data frame
data = pd.read_excel("/Users/folder/file.xls")

# AccountID18digit__c needed to edit record
# Account.Name


# retrieve values from records based on criteria, append to data frame, turn into new file
def get_values(df):
    crit = "ID"
    get = "Email"
    df["Column"] = ""
    for i in range(0, len(df)):
        crit_val = str(df.ID[i])
        q = sf.query("SELECT " + get + " FROM Account WHERE " + crit + " = '" + crit_val + "'")
        if "'" + get + "'" in str(q):
            val = str(q).split("'" + get + "', ", 1)[1].split(")]", 1)[0]
            df.Column[i] = val
        else:
            df.Column[i] = ""
    df.to_excel(path_or_buf="/Users/folder/file.xlsx")


# retrieve values from records based on criteria, append to list
def get_list(df):
    crit = "ID"
    get = "Email"
    values = []
    for i in range(0, len(df)):
        crit_val = str(df.ID[i])
        q = sf.query("SELECT " + get + " FROM Account WHERE " + crit + " = '" + crit_val + "'")
        if "'" + get + "'" in str(q):
            val = str(q).split("'" + get + "', ", 1)[1].split(")]", 1)[0]
            values.append(val)
        else:
            values.append("")


# update field in record using record's id
def update(id_list):
    for i in id_list:
        sf.Account.update(i, {'Field': ''})


get_list()
