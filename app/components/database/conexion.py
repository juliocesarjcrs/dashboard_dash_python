import pandas as pd
import pickle
import os.path
from os.path import exists
format_date = '%Y-%m-%d'
category_path = 'data/df_category.csv'
categories = pd.read_csv(category_path)
df_category_regional = pd.read_csv('data/df_category_regional.csv').rename(columns={'bill_date':'date'})
df_category_regional.date = pd.to_datetime(pd.to_datetime(df_category_regional.date).dt.date)

max_date = df_category_regional.date.max()
last_date_train = {
'year': max_date.year,
'day': max_date.day,
'month': max_date.month
}


def load_model(file_name,type_freq= 'mensual'):
    path_models = 'data/models/' + type_freq+'/'
    path_models += file_name
    file_exists = exists(path_models)
    if not file_exists:
        return None
    smodel = pickle.load(open(path_models, 'rb'))
    return smodel
def predict_data_1(smodel, future_periods, col_name, type_freq ='M'):
    fitted, confint = smodel.predict(n_periods=future_periods, return_conf_int=True)
    df = df_category_regional[['date',col_name]].rename(columns={col_name:'value'})
    df_sample = df.reset_index().resample(type_freq, on='date').sum()
    train =train_test_time_series(df_sample)
    index_of_fc = pd.date_range(train.index[-1], periods = future_periods, freq=type_freq)
    # make series for plotting purpose
    fitted_series = pd.Series(fitted, index=index_of_fc)
    forecast = pd.DataFrame(fitted_series, index = index_of_fc, columns=['value'])
    send_train = train.reset_index()
    return generate_df_to_plot_predict(send_train, forecast)

def predict_data(smodel, future_periods, col_name, type_period ='M'):
    fitted, confint = smodel.predict(n_periods=future_periods, return_conf_int=True)
    df = df_category_regional[['date',col_name]].rename(columns={col_name:'value'})
    df_sample = df.reset_index().resample(type_period, on='date').sum()
    index_of_fc = pd.date_range(df_sample.index[-1], periods = future_periods, freq=type_period)
    fitted_series = pd.Series(fitted, index=index_of_fc)
    return generate_df_to_plot(df_sample, fitted_series, index_of_fc)

def train_test_time_series(df, percent= 0.8):
    len_df = len(df)
    size = int( len_df*percent )
    train = df.iloc[:size]
    return train

def generate_df_to_plot_predict(train, forecast):
    forecast['date'] = forecast.index
    forecast['type'] = 'predict'
    send_train = train[['value', 'date']]
    train_plot = send_train
    train_plot['type'] = 'train'
    predict_df = pd.concat([train_plot, forecast ], ignore_index=True)
    return predict_df

def generate_df_to_plot(df_sample, fitted_series, index_of_fc):
    forecast = pd.DataFrame(fitted_series, index = index_of_fc, columns=['value'])
    forecast['date'] = forecast.index
    forecast['type'] = 'predict'
    data={'date':df_sample.index,'value':df_sample.value}
    train_plot = pd.DataFrame(data,columns=['date', 'value'])
    train_plot['type'] = 'train'
    len_df = len(df_sample)
    size = int( len_df*0.8 )
    test =  df_sample.iloc[size:]
    data_test={'date':test.index,'value':test.value}
    test_plot = pd.DataFrame(data_test,columns=['date', 'value'])
    test_plot['type'] = 'test'
    predict_df = pd.concat([train_plot, forecast, test_plot ], ignore_index=True)
    return predict_df


