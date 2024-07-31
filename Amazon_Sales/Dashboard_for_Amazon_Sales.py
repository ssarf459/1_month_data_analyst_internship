from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load your data
data = pd.read_csv('Amazon Sales data.csv')

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    
    html.Div([
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in data['Region'].unique()],
            value=data['Region'].unique()[0]
        )
    ]),
    
    dcc.Graph(id='revenue-by-region'),
    dcc.Graph(id='revenue-by-item-type'),
    dcc.Graph(id='feature-importance')
])

# Define callback to update the graphs
@app.callback(
    [Output('revenue-by-region', 'figure'),
     Output('revenue-by-item-type', 'figure'),
     Output('feature-importance', 'figure')],
    [Input('region-dropdown', 'value')]
)
def update_graphs(selected_region):
    # Filter data based on selected region
    filtered_data = data[data['Region'] == selected_region]
    
    # Total Revenue by Region
    revenue_by_region_fig = px.bar(data.groupby('Region')['Total Revenue'].sum().reset_index(),
                                  x='Region', y='Total Revenue', title='Total Revenue by Region')
    
    # Total Revenue by Item Type
    revenue_by_item_type_fig = px.bar(data.groupby('Item Type')['Total Revenue'].sum().reset_index(),
                                     x='Item Type', y='Total Revenue', title='Total Revenue by Item Type')
    
    # Feature Importance (dummy example, replace with real data)
    feature_importance = pd.DataFrame({
        'Feature': ['Feature 1', 'Feature 2', 'Feature 3'],
        'Importance': [0.6, 0.3, 0.1]
    })
    feature_importance_fig = px.bar(feature_importance, x='Feature', y='Importance',
                                   title='Feature Importance')
    
    return revenue_by_region_fig, revenue_by_item_type_fig, feature_importance_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
