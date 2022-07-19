value = 0
def ML_climate():
    try:
        from datetime import date, datetime
        from sklearn.linear_model import LinearRegression
        import matplotlib.pyplot as plt
        from meteostat import Point, Daily
        from geopy.geocoders import Nominatim
        from sklearn.model_selection import train_test_split
        import numpy as np
        geolocator = Nominatim(user_agent="Climate Change")
        place = input("Enter place name:")
        place = place.lower()
        year = int(input("Enter start year:") or 1970)
        month = int(input("Enter start month:") or 1)
        day = int(input("Enter start date:") or 1)
        date_today = date.today()
        start = datetime(year, month, day)
        year_end = int(input("Enter end year:") or date_today.year)
        month_end = int(input("Enter end month:") or date_today.month)
        day_end = int(input("Enter end date:") or date_today.day)
        end = datetime(year_end, month_end, day_end)
        no_predict = input("Input yes for only plots without prediction:") or False
        location = geolocator.geocode(place)
        locs = Point(location.latitude, location.longitude)
        data = Daily(locs, start, end)
        data = data.fetch()

        if(no_predict == False):
            try:
                max_x = data[["tmax", "tmin", "tavg", "pres"]]
                max_x.columns = ["max", "min", "avg", "pre"]
                max_x = max_x.dropna()

                y = np.array(max_x['avg']).reshape(-1, 1)
                X = np.array(max_x["pre"]).reshape(-1, 1)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99)
                regr = LinearRegression()
                regr.fit(X_train, y_train)
                x_pred = regr.predict(X)
                y_pred = regr.predict(y)
                max_x = max_x.assign(predicted=x_pred)
                max_x.plot(y=['avg', 'predicted'],color=('#DF6589FF', '#3C1053FF'))
                plt.show()

                y = np.array(max_x['max']).reshape(-1, 1)
                X = np.array(max_x["pre"]).reshape(-1, 1)
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.99)
                regr = LinearRegression()
                regr.fit(X_train, y_train)
                x_pred = regr.predict(X)
                y_pred = regr.predict(y)
                max_x = max_x.assign(predicted=x_pred)
                max_x.plot(y=['max', 'predicted'],color=('#DF6589FF', '#3C1053FF'))
                plt.show()

                y = np.array(max_x['min']).reshape(-1, 1)
                X = np.array(max_x["pre"]).reshape(-1, 1)
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.99)
                regr = LinearRegression()
                regr.fit(X_train, y_train)
                x_pred = regr.predict(X)
                y_pred = regr.predict(y)
                max_x = max_x.assign(predicted=x_pred)
                max_x.plot(y=['min', 'predicted'],color=('#DF6589FF', '#3C1053FF'))
                plt.show()
            except:
                value = 1

        else:
            try:
                data.plot(y=["tavg"])
                plt.show()
                data.plot(y=["tmin"])
                plt.show()
                data.plot(y=["tmax"])
                plt.show()
            except:
                value = 1

    except:
        value = 1


if(value == 1):
    print("Data for this place doesn't exist")


if __name__ == "__main__":
    ML_climate()
