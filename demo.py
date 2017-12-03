import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
rollnumber=np.arange(1,7)
Men=np.random.randint(40,98,50)
Women=np.random.randint(40,98,50)
student=list(zip(rollnumber,Men,Women))
df=DataFrame(data=student,columns=['register number','Men','Women'])
selected=df.iloc[1:6]
df2=pd.DataFrame(selected,columns=['Men','Women'])
#df2.plot.hist(alpha=0.5)df2.plot.box()
#df2.plot.area(stacked=True)
#df2.plot.pie(subplots=True, figsize=(8,8),autopct='%.2f')
fig, ax = plt.subplots(1, 1)
ax.get_xaxis().set_visible(True)   # Hide Ticks
df2.plot.bar(ax=ax)
#df2.plot(table=True, ax=ax,linestyle='dashed')
#df2.plot.barh(stacked=True,ax=ax)
ax.set_title('scores by group and gender')
ax.set_ylabel('scores')
ax.set_xlabel('Students')
plt.show()
