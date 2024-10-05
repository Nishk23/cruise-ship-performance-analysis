import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the cleaned dataset
df = pd.read_csv('../data/data_cleaned.csv')

# Ensure 'Start Time' is in datetime format
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Dynamically get the min and max dates from 'Start Time'
min_date = df['Start Time'].min()
max_date = df['Start Time'].max()

# Create aggregated columns for Diesel Generator Power and HVAC Power Consumption
df['Total Diesel Generator Power (MW)'] = (
        df['Diesel Generator 1 Power (MW)'] +
        df['Diesel Generator 2 Power (MW)'] +
        df['Diesel Generator 3 Power (MW)'] +
        df['Diesel Generator 4 Power (MW)']
)

df['Total HVAC Power (MW)'] = (
        df['HVAC Chiller 1 Power (MW)'] +
        df['HVAC Chiller 2 Power (MW)'] +
        df['HVAC Chiller 3 Power (MW)']
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Vessel Performance Trends Comparison", style={'color': 'white', 'textAlign': 'center'}),

    # Dropdown for selecting KPI
    dcc.Dropdown(
        id='kpi-dropdown',
        options=[
            {'label': 'Propulsion Power', 'value': 'Propulsion Power (MW)'},
            {'label': 'Fuel Flow Rate (Main Engine 1)', 'value': 'Main Engine 1 Fuel Flow Rate (kg/h)'},
            {'label': 'Fuel Flow Rate (Main Engine 2)', 'value': 'Main Engine 2 Fuel Flow Rate (kg/h)'},
            {'label': 'Fuel Flow Rate (Main Engine 3)', 'value': 'Main Engine 3 Fuel Flow Rate (kg/h)'},
            {'label': 'Fuel Flow Rate (Main Engine 4)', 'value': 'Main Engine 4 Fuel Flow Rate (kg/h)'},
            {'label': 'Diesel Generator Power', 'value': 'Total Diesel Generator Power (MW)'},
            {'label': 'HVAC Power Consumption', 'value': 'Total HVAC Power (MW)'},
            {'label': 'Speed Over Ground', 'value': 'Speed Over Ground (knots)'}
        ],
        value='Propulsion Power (MW)',  # Default value
        clearable=False,
        style={'width': '50%'}
    ),

    # Dropdown for selecting Vessel view
    dcc.Dropdown(
        id='vessel-dropdown',
        options=[
            {'label': 'Vessel 1', 'value': 'Vessel 1'},
            {'label': 'Vessel 2', 'value': 'Vessel 2'},
            {'label': 'Vessels Overlap View', 'value': 'Overlap'},
        ],
        value='Vessel 1',  # Default value
        clearable=False,
        style={'width': '50%', 'marginTop': '20px'}
    ),

    # Date Range picker for filtering data, now with dynamic min/max
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=min_date,  # Dynamically set min date
        end_date=max_date,  # Dynamically set max date
        display_format='YYYY-MM-DD',
        style={'marginTop': '20px'}
    ),

    # Graph placeholder
    dcc.Graph(id='kpi-graph'),

], style={'backgroundColor': '#000', 'padding': '20px'})


# Callback for updating the graph based on selected KPI, Vessel view, and Date range
@app.callback(
    Output('kpi-graph', 'figure'),
    [Input('kpi-dropdown', 'value'),
     Input('vessel-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_graph(selected_kpi, selected_vessel, start_date, end_date):
    # Filter data by date range
    global fig
    filtered_df = df[(df['Start Time'] >= start_date) & (df['Start Time'] <= end_date)]

    # Handle Vessel View options
    if selected_vessel == 'Vessel 1':
        filtered_df = filtered_df[filtered_df['Vessel Name'] == 'Vessel 1']
        fig = px.line(filtered_df, x='Start Time', y=selected_kpi, title=f'{selected_kpi} for Vessel 1')
    elif selected_vessel == 'Vessel 2':
        filtered_df = filtered_df[filtered_df['Vessel Name'] == 'Vessel 2']
        fig = px.line(filtered_df, x='Start Time', y=selected_kpi, title=f'{selected_kpi} for Vessel 2')
    elif selected_vessel == 'Overlap':
        vessel_1_df = filtered_df[filtered_df['Vessel Name'] == 'Vessel 1']
        vessel_2_df = filtered_df[filtered_df['Vessel Name'] == 'Vessel 2']
        fig = px.line(vessel_1_df, x='Start Time', y=selected_kpi, title=f'{selected_kpi} Overlap View')
        fig.add_scatter(x=vessel_2_df['Start Time'], y=vessel_2_df[selected_kpi], mode='lines', name='Vessel 2')

    # Style the graph with black background and white labels
    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        height=842,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
