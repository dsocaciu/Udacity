import numpy as np
import pandas as pd
import os
#import matlibpyplot as plt
import matplotlib.pyplot as plt
import scipy.optimize as spo
from scipy import stats



def load_data(csv):
	
	df = pd.read_csv(csv, index_col='Date',parse_dates=True,
				usecols=['Date','Adj Close'],na_values=['nan'])

	return df

def normalize_data(df):

	return df/df.ix[0,:]

def get_data(symbols,dates):

	df = pd.DataFrame(index=dates)
	
	for symbol in symbols:

		df_temp = load_data("{}.csv".format(symbol))
		df_temp = df_temp.rename(columns={'Adj Close':symbol})

		df = df.dropna()

		df=df.join(df_temp)


	return df


def compute_daily_returns(df):
    """Compute and return the daily return values."""

    df1 = df.copy()

    df1[1:] =  (df[1:]/df[:-1].values) -1
    df1.ix[0,:]=0
    
    return df1




if __name__ ==  "__main__":

	symbols = ['TSLA','NFLX','SPY']

	dates = pd.date_range('2012-01-01','2015-12-31')

	df = get_data(symbols,dates)

	#print df

	ax = df.plot(title = "Stock price",fontsize=12)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")

	#plt.show()







	rm_SPY = pd.rolling_mean(df['SPY'],window=20)

	print rm_SPY

	rm_SPY.plot(label ='Rolling mean',ax=ax)
	plt.show()

	norm_df = normalize_data(df)
	norm_df.plot()
	plt.show()

	daily_returns = compute_daily_returns(df)

	daily_returns.plot()
	plt.show()


	daily_returns['TSLA'].hist(bins=20,label='TSLA')
	daily_returns['NFLX'].hist(bins=20,label='NFLX')
	daily_returns['SPY'].hist(bins=20,label='SPY')

	print "SPY mean: " + str(daily_returns['SPY'].mean())
	print "SPY st dev: " + str(daily_returns['SPY'].std())
	print "SPY kurtosis: " + str(daily_returns['SPY'].kurtosis())

	plt.axvline(daily_returns['SPY'].mean(),color='w',linestyle='dashed',linewidth=2)

	print "TSLA mean: " + str(daily_returns['TSLA'].mean())
	print "TSLA st dev: " + str(daily_returns['TSLA'].std())
	print "TSLA kurtosis: " + str(daily_returns['TSLA'].kurtosis())


	print "NFLX mean: " + str(daily_returns['NFLX'].mean())
	print "NFLX st dev: " + str(daily_returns['NFLX'].std())
	print "NFLX kurtosis: " + str(daily_returns['NFLX'].kurtosis())

	plt.show()

	daily_returns.plot(kind='scatter',x='SPY',y='TSLA')
	beta_TSLA,alpha_TSLA = np.polyfit(daily_returns['SPY'],daily_returns['TSLA'],1)
	plt.plot(daily_returns['SPY'], beta_TSLA*daily_returns['SPY'] + alpha_TSLA, '-',color='r')

	print "TSLA beta: " + str(beta_TSLA) 

	tsla_r2 = tsla_slope, tsla_intercept, tsla_r_value, tsla_p_value, tsla_std_err = stats.linregress(daily_returns['SPY'],daily_returns['TSLA'])

	print "TSLA slope: " + str(tsla_slope)
	print "TSLA r^2: " + str(tsla_r_value**2)
	plt.show()

	daily_returns.plot(kind='scatter',x='SPY',y='NFLX')
	beta_NFLX,alpha_NFLX = np.polyfit(daily_returns['SPY'],daily_returns['NFLX'],1)
	plt.plot(daily_returns['SPY'], beta_NFLX*daily_returns['SPY'] + alpha_NFLX, '-',color='r')
	
	print "NFLX beta : " + str(beta_NFLX)

	plt.show()


	#print df['Adj Close'].plot()
	#plt.show()