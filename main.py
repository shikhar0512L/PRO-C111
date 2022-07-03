import csv
import random
import pandas as pd 
import statistics
import plotly.graph_objects as go 
import plotly.figure_factory as ff 

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist() 


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean 

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()

def set_up():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

set_up()
mean=statistics.mean(data)
print('mean of sampling distribution',mean)

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
standard_deviation()
std_deviation=statistics.stdev(data)
print('stadard deviation of sampling distrabution',std_deviation)
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

#######

first_sd_start,first_sd_end=mean-std_deviation,mean+std_deviation
second_sd_start,second_sd_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_sd_start,third_sd_end=mean-(3*std_deviation),mean+(3*std_deviation)

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
mean_of_sample1=statistics.mean(data)
print('mean of sample 1',mean_of_sample1)
fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode='lines',name='MEAN OF SAMPLE 1'))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 END'))


fig.show()
z_score=(mean_of_sample1-mean)/std_deviation
print('the z score is=',z_score)

# df=pd.read_csv('data.csv')
# data=df['reading_time'].tolist()
# mean_of_sample2=statistics.mean(data)
# print('mean of sample 2',mean_of_sample2)
# fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
# fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode='lines',name='MEAN OF SAMPLE 2'))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 END'))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 END'))
# fig.show()

# df=pd.read_csv('data.csv')
# data=df['reading_time'].tolist()
# mean_of_sample3=statistics.mean(data)
# print('mean of sample 3',mean_of_sample3)
# fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
# fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode='lines',name='MEAN OF SAMPLE 3'))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 END'))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 END'))
# fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3 END'))
# fig.show()


