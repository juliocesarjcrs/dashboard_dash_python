import pandas as pd
import pickle
format_date = '%Y-%m-%d'
category_path = 'data/df_category.csv'
categories = pd.read_csv(category_path)
df_category_regional = pd.read_csv('data/df_category_regional.csv')


def plot_predict(train, test, forecast):
    train_plot = train
    train_plot['type'] = 'train'
    train_plot.rename(columns = {'train':'value'}, inplace = True)
    test_plot = test
    test_plot['type'] = 'test'
    test_plot.rename(columns = {'test':'value'}, inplace = True)
    # forecast
    forecast_plot = forecast
    forecast_plot['type'] = 'predict'
    forecast_plot.rename(columns = {'Prediction':'value'}, inplace = True)
    result = pd.concat([test_plot,train_plot, forecast_plot ],ignore_index=True)
    return result

# separete train
df_category = pd.read_csv(category_path)

cat = 'MANGANESO'
df_for_model = df_category[['date', cat]]
train = df_for_model[ pd.to_datetime(df_for_model['date'], format=format_date) < pd.to_datetime("2022-02-28", format=format_date) ].copy()
train['train'] = train[cat]
train.index=train['date']

del train['date']
del train['MANGANESO']

test = df_for_model[pd.to_datetime(df_for_model['date'], format=format_date) >= pd.to_datetime("2022-02-28", format=format_date)].copy()
test.index=test['date']
del test['date']
test['test'] = test['MANGANESO']
del test['MANGANESO']

loaded_model = pickle.load(open('data/models/finalized_model.sav', 'rb'))
forecast_load = loaded_model.predict(n_periods=len(test))
forecast_load = pd.DataFrame(forecast_load,index = test.index,columns=['Prediction']).reset_index()
send_train = train.reset_index()
send_test = test.reset_index()
forecast_plot = plot_predict(send_train, send_test, forecast_load)

def load_model(file_name):
    path_models = 'data/models/'
    path_models += file_name
    smodel = pickle.load(open(path_models, 'rb'))
    return smodel

def predict_data(smodel, cal_period, type_freq ='M'):
    fitted, confint = smodel.predict(n_periods=cal_period, return_conf_int=True)
    index_of_fc = pd.date_range(train.index[-1], periods = cal_period, freq=type_freq)
    # make series for plotting purpose
    fitted_series = pd.Series(fitted, index=index_of_fc)
    return fitted_series




