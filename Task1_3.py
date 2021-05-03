import pandas as pd
import sys

excel1 = 'data.xlsx'
excel2 = 'data_1.xlsx'


parsed_file = pd.DataFrame({})  # Initializing an Empty data frame


def combine_Excel_files(excel_file):
    # Opening of excel1 file
    dta_frame = pd.ExcelFile(excel_file, engine='openpyxl')
    p_file = pd.DataFrame({})
    # initializing empty temporary Empty dataframe to be returned
    for i in dta_frame.sheet_names:
        if 'DetailTemp_67_' in i:
            temporary_dataFrame = dta_frame.parse(i)
            # appending details at the end of file
            p_file = p_file.append(temporary_dataFrame)
    return p_file  # returning the final value of p_file

# function call to retrieve all the columns from the sheet DetailTemp_67_
file_1 = combine_Excel_files(excel1)
# appending contents of file 1 to parsed_file
parsed_file = parsed_file.append(file_1)
# function call to retrieve all the columns from the sheet DetailTemp_67_
file_2 = combine_Excel_files(excel2)
# appending contents of file 2 to parsed_file
parsed_file = parsed_file.append(file_2)
# printing  parsed_file or final output
print (parsed_file)
# converting to csv file
parsed_file.to_csv(r'E:\NUNAM ASSIGN\detailVol.csv')


