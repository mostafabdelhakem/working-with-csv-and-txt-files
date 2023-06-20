# import needed libraries
import pandas as pd

##### creating a data_frame ######
data_frame = pd.DataFrame({'categorical': pd.Categorical(['s', 't', 'u']),
                    'numeric': [2, 3, 4],
                    'abject': ['p', 'q', 'r']
                    })
print('\nData Frame')
print(data_frame)                                    # all data_frame will printed

print('\nNumeric Data')
print(data_frame.describe())                         # only numeric will be described

print('\nData Frame Describe')
print(data_frame.describe(include = 'all'))          # all data_frame will be described

print('\nCategorical Describe')
print(data_frame.describe(include = ['category']))   # only categorical pary will described

print('\nDescribe Without Object')
print(data_frame.describe(exclude = [object]))       # all will described without object

print('----------- Done ✔ -----------')