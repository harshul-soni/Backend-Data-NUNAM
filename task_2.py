import pandas as pd

def convert_to(path,param):# function to convert index to DateTimeIndex and then downsampling data to per minute
    dataset = pd.read_csv(path) # read csv from path passed as parameter
    
    dataset.set_index(param, inplace= True) 
    dataset.index = pd.to_datetime(dataset.index)
    
    new_sample = dataset.resample('T').mean()
    
    return new_sample #returning the reduced dataframe


#Each dataframe

details = convert_to(r'E:\NUNAM ASSIGN\detail.csv','Absolute Time')
detail_temp = convert_to(r'E:\NUNAM ASSIGN\detailTemp.csv','Realtime')
detail_vol = convert_to(r'E:\NUNAM ASSIGN\detailVol.csv','Realtime')


#exporting to csv file
details.to_csv(r'E:\NUNAM ASSIGN\detailDownsampled.csv')
detail_vol.to_csv(r'E:\NUNAM ASSIGN\detailVolDownsampled.csv')
detail_temp.to_csv(r'E:\NUNAM ASSIGN\detailTempDownsampled.csv')