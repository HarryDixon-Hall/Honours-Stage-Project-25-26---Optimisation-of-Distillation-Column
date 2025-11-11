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
            dcc.Slider(id='volume', min=0.5, max=5, step=0.1, value=1.0),
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
])

if __name__ == '__main__':
    app.run(debug=True)
