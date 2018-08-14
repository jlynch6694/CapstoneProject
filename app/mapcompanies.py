from app.forms import InputGDP
from app.convert import CalculateGDP
import pandas as pd
import folium

def addCircle(d, x):
    corporations_df = pd.read_csv('app/static/media/corporations.csv')
    lat = list(corporations_df['lat'])
    lon = list(corporations_df['lon'])
    name = list(corporations_df['name'])
    marketcap = list(corporations_df['marketcap'])
    evsales = list(corporations_df['EVSales'])
    loc = list(corporations_df['location'])
    form = InputGDP()
    for lat, lon, name, marketcap, evsales, loc in zip(lat, lon, name, marketcap, evsales, loc):
        if form.validate_on_submit:
            if x > int(evsales):
                folium.Circle(
                location=[lat,lon], popup="<b>"+ name + "</b>" + "<br>" + "Location: " + loc + "<br>" + "Market Capitalization: " + "$" +
                str("{:,.2f}".format(marketcap)) + "<br>" + "EV/Sales Ratio: " + str(evsales) + "<br>" + "This company has a lower EV/Sales ratio than yours. You should <b>consider</b> acquiring it!", radius=marketcap/60,
                fill='True', color='#228b22', fill_color='#228b22', fill_opacity=0.5, opacity=0.9).add_to(d)
            elif x < int(evsales):
                folium.Circle(
                location=[lat,lon], popup="<b>"+ name + "</b>" + "<br>" + "Location: " + loc + "<br>" + "Market Capitalization: " + "$" +
                str("{:,.2f}".format(marketcap)) + "<br>" + "EV/Sales Ratio: " + str(evsales) + "<br>" + "This company has a higher EV/Sales ratio than yours. You should <b>avoid</b> acquiring it!", radius=marketcap/60,
                fill='True', color='red', fill_color='red', fill_opacity=0.5, opacity=0.9).add_to(d)
        else:
            return None
