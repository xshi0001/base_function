import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import time
pd.set_option('display.max_rows',None)
def df_practice():
    a=[1,-23,4,5,6,7,-4,34,3,5,33]
    b=[-2,55,-5,99,3,-3,55,3,-1,4,7]
    df=pd.DataFrame({'A':a,'B':b})
    print df
    #df.loc[(df['A']>0) & (df['B']<0),'A']=100
    df.ix[(df['A']>0) & (df['B']<0),'A']=100
    print df

def question():
    a = pd.Series([1])
    b = pd.Series([2])
    if (b/a)[0]==2:
        print "ok"

def plot_test():
    s=Series(np.random.rand(20))
    #s.plot()
    #plt.show(s.plot(kind='hist'))
    ax=s.plot(kind='bar')
    fig=ax.get_figure()
    fig.savefig('1.png')


def compare_values():
    a=-10
    c=a+1
    b=-9.299
    if a>=b and b<c:
        print "Got"
def calculate():
    total=[]
    df=pd.read_excel('2017-04-12_all_.xls')
    '''
    i=-10
    dfx= df[(df['changepercent']>=(i+0.1)) & (df['changepercent']<((i+1))*1.000)]
    print dfx
    print dfx['changepercent'].iloc[0]
    print len(dfx)
    '''
    count= len(df[(df['changepercent']>=-10.2) & (df['changepercent']<-9)])
    total.append(count)
    for i in range(-9,9,1):
        #print i
        #print df[(df['changepercent']>=i) & (df['changepercent']<(i+1))]
        count= len(df[(df['changepercent']>=i*1.00) & (df['changepercent']<((i+1))*1.00)])
        #print count
        total.append(count)
        #time.sleep(60)
        #total.append(count)
    count= len(df[(df['changepercent']>=9)])
    total.append(count)
    #print df
    sum=0
    for i in range(len(total)):
        sum=sum+total[i]
    print sum
    print total
    df_figure=pd.Series(total,index=[range(-10,10)])
    print df_figure
    fg=df_figure.plot(kind='bar',y=total)
    plt.show(fg)

#df_practice()
#question()
#plot_test()
calculate()
#compare_values()