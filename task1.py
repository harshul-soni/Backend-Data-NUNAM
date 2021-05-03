import pandas as pd
import sys
a = ['E:\\Anaconda\\python37.zip',
     'E:\\Anaconda\\DLLs', 
     'E:\\Anaconda\\lib', 
     'E:\\Anaconda', 
     'E:\\Anaconda\\lib\\site-packages', 
     'E:\\Anaconda\\lib\\site-packages\\win32', 
     'E:\\Anaconda\\lib\\site-packages\\win32\\lib', 
     'E:\\Anaconda\\lib\\site-packages\\Pythonwin']

for i in a:
    sys.path.append(i)
 
    
excel1 = 'data.xlsx'
excel2 = 'data_1.xlsx'


parsed_file = pd.DataFrame({}) #Initializing an Empty data frame

def combine_Excel_files(excel_file):
    dta_frame = pd.ExcelFile(excel_file, engine='openpyxl') #Opening of excel1 file
    p_file = pd.DataFrame({}) #initializing empty temporary Empty dataframe to be returned
    for i in dta_frame.sheet_names:
        if 'Detail_67_' in i:
            temporary_dataFrame = dta_frame.parse(i)
            p_file = p_file.append(temporary_dataFrame) #appending details at the end of file
    return p_file #returning the final value of p_file
    

file_1 = combine_Excel_files(excel1) #function call to retrieve all the columns from the sheet detail_67_
parsed_file = parsed_file.append(file_1) #appending contents of file 1 to parsed_file

file_2 =combine_Excel_files(excel2) #function call to retrieve all the columns from the sheet detail_67_
parsed_file = parsed_file.append(file_2) #appending contents of file 2 to parsed_file

print (parsed_file) # printing  parsed_file or final output



parsed_file.to_csv(r'E:\NUNAM ASSIGN\detail.csv') # converting to csv file


