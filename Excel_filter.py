import pandas as pd

# reads file into a pandas data frame
data = pd.read_excel("/Users/Nicole/Documents/Orders/orders.xls")

# list unique values in column
values = data.Item.unique()

#
# store data frames for each unique value in a dictionary
values_dict = {i: pd.DataFrame for i in values}
for k in values_dict.keys():
    values_dict[k] = data[:][data.Item == k]

# turn each dictionary key's data frame into its own file
def make_xl(dict):
    for k in dict.keys():
        d = pd.DataFrame(dict[k])
        d.to_excel(excel_writer="/Users/Nicole/Documents/Orders/item_" + k + ".xlsx")

# call function
make_xl(values_dict)
