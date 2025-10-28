from dash import Dash, html

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = html.Div([html.H2("CSTR Control Dashboard")])

if __name__ == '__main__':
    app.run(debug=True)
