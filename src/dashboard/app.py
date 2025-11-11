from dash import Dash, html, dcc, Input, Output

app = Dash()

app.layout = html.Div([
    # Phase 1 Heading
    html.H2("Phase 1: Configuration"),

    # CSTR Simulation parameter config
    html.Div([
        html.H3("CSTR Parameters"),
        html.Div([
            html.Label("Reactor volume (m3):"),
            dcc.Input(id='volume', type='number', value=1.0),
        ]),
        html.Div([
            html.Label("Heat Capacity (kJ/kg.K):"),
            dcc.Input(id='cp', type='number', value=4.18),
        ]),
        html.Div([
            html.Label("Density of reactant (g/L):"),
            dcc.Input(id='density', type='number', value=1000),
        ]),
        html.Div([
            html.Label("Pre-exponential factor (/min):"),
            dcc.Input(id='prexp', type='number', value=100),
        ]),
        html.Div([
            html.Label("Activation Energy (J/mol):"),
            dcc.Input(id='act_energy', type='number', value=50000),
        ]),
        html.Div([
            html.Label("Reaction enthalpy (J/mol):"),
            dcc.Input(id='enthalpy', type='number', value=60000),
        ]),
        html.Div([
            html.Label("Heat Transfer Coefficient:"),
            dcc.Input(id='htrans', type='number', value=500),
        ]),
    ]),

    # PID Controller
    html.Div([
        html.H3("PID Controller"),
        html.Div([
            html.Label("KP:"),
            dcc.Input(id='kp', type='number', placeholder='kp', value=5.0),
        ]),
        html.Div([
            html.Label("KI:"),
            dcc.Input(id='ki', type='number', placeholder='ki', value=0.2),
        ]),
        html.Div([
            html.Label("KD:"),
            dcc.Input(id='kd', type='number', placeholder='kd', value=1.0),
        ]),
    ]),

    # Neural Network Architecture
    html.Div([
        html.H3("Neural Network Architecture"),
        dcc.Dropdown(
            id='nn_type',
            options=[
                {'label': 'LSTM', 'value': 'lstm'},
                {'label': 'GRU', 'value': 'gru'},
                {'label': 'LSTM-Transformer Hybrid', 'value': 'hybrid'}
            ],
            value='hybrid'
        ),
        dcc.Slider(id='hidden_units', min=50, max=500, step=50, value=200),
        dcc.Input(id='learning_rate', type='number', value=0.001),
    ]),

    html.Button('Submit Configuration', id='submit_config', n_clicks=0),
])

if __name__ == '__main__':
    app.run(debug=True)

