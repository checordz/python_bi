import pandas as pd
import datetime as dt

df = pd.read_csv('ENTREGA_AL20JUN18_Limpia.csv')

df['FCH_ING']=pd.to_datetime(df['FCH_ING'], dayfirst=True)
df['FCH_DEC']=pd.to_datetime(df['FCH_DEC'], dayfirst=True)
df['FCH_ESTATUS']=pd.to_datetime(df['FCH_ESTATUS'], dayfirst=True)

df.to_csv('ENTREGA_AL20JUN18_Limpia_2.csv')