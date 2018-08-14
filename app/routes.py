#need to import app variable itself
import os
import json
import pandas as pd
from app import app
from flask import render_template, Markup, send_file #need to render html files
from app.forms import currencyForm, InputGDP
from werkzeug.urls import url_parse
from app.convert import convertThis, CalculateGDP
from app.mapcompanies import addCircle
import folium
from folium.plugins import MarkerCluster


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Markets/Currencies', methods=['GET', 'POST'])
def chart():
    form = currencyForm()
    labels = ['US Dollar', 'Chinese Yuan', 'Canadian Dollar', 'Mexican Peso', 'Japanese Yen', 'Germany (Euro)', 'South Korean Won', 'British Pound', 'France (Euro)', 'Indian Rupee', 'New Taiwan Dollar']
    values = [1.000, 6.658, 1.313, 19.200, 110.67, 0.860, 1119.530, 1.322, 0.860, 68.890, 30.530]
    if form.validate_on_submit():
        lang = form.language.data
        values = convertThis(lang, values)
    return render_template('chart.html', form=form, values=values, labels=labels)

@app.route('/Markets/Bonds')
def chart2():
    labels = ['China', 'Canada', 'Mexico', 'Japan', 'Germany', 'South Korea', 'United Kingdom', 'France', 'India', 'Taiwan']
    values = [3.520, 2.150, 7.660, 0.0380, 0.300, 2.545, 1.260, 0.640, 7.660, 0.920]
    return render_template('chart2.html', values=values, labels=labels)

@app.route('/Markets/Commodities', methods=['GET', 'POST'])
def chart3():
    form = currencyForm()
    labels = ['US Dollar', 'Chinese Yuan', 'Canadian Dollar', 'Mexican Peso', 'Japanese Yen', 'Germany (Euro)', 'South Korean Won', 'British Pound', 'France (Euro)', 'Indian Rupee', 'New Taiwan Dollar']

    energy_labels = ['Crude Oil', 'Brent', 'Natural Gas', 'Gasoline', 'Heating Oil', 'Ethanol', 'Naphtha', 'Propane', 'Uranium']
    energy_values = [73.991, 77.661, 2.849, 2.125, 2.188, 1.425, 650.08, 0.960, 22.850]
    if form.validate_on_submit():
        lang = form.language.data
        energy_values = convertThis(lang, energy_values)


    metals_labels = ['Gold', 'Silver', 'Platinum', 'Palladium', 'Manganese', 'Rhodium']
    metals_values = [1264.55, 16.145, 857.30, 961.85, 38.500, 2260.00]
    if form.validate_on_submit():
        lang = form.language.data
        metals_values = convertThis(lang, metals_values)


    agriculture_labels = ['Soybeans', 'Wheat', 'Cotton', 'Rice', 'Cheese', 'Palm Oil', 'Milk', 'Wool', 'Oat', 'Tea', 'Lumber', 'Rubber', 'Coffee', 'Orange Juice', 'Sugar', 'Cocoa', 'Canola', 'Corn']
    agriculture_values = [850.581, 495.298, 86.83, 11.889, 1.508, 2210.00, 14.16, 1994.00, 257.971, 2.880, 529.00, 166.20, 111.05, 167.50, 11.49, 2438.00, 504.70, 341.965]
    if form.validate_on_submit():
        lang = form.language.data
        agriculture_values = convertThis(lang, agriculture_values)


    livestock_labels = ['Live Cattle', 'Feeder Cattle', 'Lean Hogs', 'Beef', 'Poultry']
    livestock_values = [105.912, 151.232, 80.19, 9.50, 3.74]
    if form.validate_on_submit():
        lang = form.language.data
        livestock_values = convertThis(lang, livestock_values)


    industrial_labels = ['Copper', 'Bitumen', 'Steel', 'Cobalt', 'Coal', 'Lead', 'Aluminum', 'Tin', 'Zinc', 'Nickel', 'Molybdenum', 'Iron Ore', 'Soda Ash', 'Lithium']
    industrial_values = [2.819, 3162.00, 3955.00, 73000, 113.270, 2327.25, 2145.50, 19670.00, 2716.00, 13850.50, 25000.00, 66.50, 2028.57, 126.84]
    if form.validate_on_submit():
        lang = form.language.data
        industrial_values = convertThis(lang, industrial_values)

    return render_template('commcharts.html', energy_labels=energy_labels, energy_values=energy_values, metals_labels=metals_labels, metals_values=metals_values, agriculture_labels=agriculture_labels, agriculture_values=agriculture_values, livestock_labels=livestock_labels, livestock_values=livestock_values, industrial_labels=industrial_labels, industrial_values=industrial_values, form=form, labels=labels)

@app.route('/GDP', methods=['GET', 'POST'])
def corporations():
    form = InputGDP()
    calc = None
    result = 0
    if form.validate_on_submit():
        calc = CalculateGDP(form.num1.data, form.num2.data, form.num3.data, form.num4.data, form.num5.data)
        result = (form.num1.data + form.num2.data + form.num3.data - form.num4.data)/form.num5.data
    return render_template('corporations.html', calc=calc, form=form, result=result )

@app.route('/TradeBalances')
def trade():
    df = pd.read_csv("./app/static/media/trade.csv")
    countries = df['country']
    totals = df['total']
    years = df['year']
    countries2015 = countries.loc[years == 2015]
    countries2016 = countries.loc[years == 2016]
    countries2017 = countries.loc[years == 2017]
    totals2015 = totals.loc[years == 2015]
    totals2016 = totals.loc[years == 2016]
    totals2017 = totals.loc[years == 2017]
    labels2015 = countries2015
    labels2016 = countries2016
    labels2017 = countries2017
    values2015 = totals2015
    values2016 = totals2016
    values2017 = totals2017
    return render_template('trade.html', labels2015=labels2015, values2015=values2015, labels2016=labels2016, values2016=values2016, labels2017=labels2017, values2017=values2017)


@app.route('/show_map/<result>')
def show_map(result):
    form = InputGDP()
    mapthis= folium.Map(location=[42.456, -71.345], zoom_start=5, tiles='Stamen Terrain', control_scale=True)
    marker_cluster = folium.plugins.MarkerCluster().add_to(mapthis)
    addCircle(marker_cluster, int(float(result)))
    return mapthis.get_root().render()
    # return render_template('map.html', mapthis=mapthis)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
