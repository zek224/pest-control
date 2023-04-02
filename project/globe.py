#getting my public IP (from the internet provider)
import requests
import pandas as pd
import plotly.graph_objects as go

# Get public IP address and location
my_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
ip_json = requests.get('http://ip-api.com/json/' + my_ip).json()
latitude = ip_json['lat']
longitude = ip_json['lon']

# Read the spreadsheet
df = pd.read_excel('20210923_World_P_data_JW.xlsx')
df = df.dropna(subset=['TP ICP-OES'])

# Get the latitude, longitude, and phosphate levels from the spreadsheet
lats = df['Latitude'].tolist()
lons = df['Longitude'].tolist()
phosphate_levels = df['TP ICP-OES'].tolist()

# Create a list of colors based on the phosphate levels
colors = ['rgb({0}, 0, 0)'.format(int(level * 255)) for level in phosphate_levels]

# Create a scattergeo trace with the latitude, longitude, and colors
trace = go.Scattergeo(
    lat=lats,
    lon=lons,
    mode='markers',
    marker=dict(
        size=23,
        color=colors,
        opacity=0.1,
        reversescale=False,
        colorbar=dict(
            title='Phosphate Levels'
        ),
        line=dict(
            width=1,
            color='rgba(102, 102, 102)'
        )
    )
)

# Create the plot
fig = go.Figure(trace)
fig.update_geos(projection_type="orthographic")
fig.update_layout(width=800, height=800, margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html("3d_plot.html")
fig.show()

#making the plot
#if you are passing just one lat and lon, put it within "[]"
#    fig = go.Figure(go.Scattergeo(lat=[latitude], lon=[longitude]))
#editing the marker
#    fig.update_traces(marker_size=20, line=dict(color='Red'))
# this projection_type = 'orthographic is the projection which return 3d globe map'
#    fig.update_geos(projection_type="orthographic")
#layout, exporting html and showing the plot
#    fig.update_layout(width= 800, height=800, margin={"r":0,"t":0,"l":0,"b":0})
#    fig.write_html("3d_plot.html")
#    fig.show()
