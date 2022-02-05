import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv('studn.csv')

data = df['reading score'].to_list()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)

firstsdstart,firstsdend=mean-sd,mean+sd
secondsdstart,secondsdend=mean-(2*sd),mean+(2*sd)
thirdsdstart,thirdsdend=mean-(3*sd),mean+(3*sd)

listoffirstsd = [result for result in data if result>firstsdstart and result<firstsdend]
listofsecondsd = [result for result in data if result>secondsdstart and result<secondsdend]
listofthirdsd = [result for result in data if result>thirdsdstart and result<thirdsdend]

print('mean = {}'.format(mean))
print('mode = {}'.format(mode))
print('median = {}'.format(median))
print('standarddev = {}'.format(sd))

print("{} % is within the first standard deviation".format(len(listoffirstsd)*100/len(data)))
print("{} % is within the second standard deviation".format(len(listofsecondsd)*100/len(data)))
print("{} % is within the third standard deviation".format(len(listofthirdsd)*100/len(data)))