#Mathematics and Statistics, Monsoon 2019
#Assignment 2
import plotly.graph_objects as go
import chart_studio.plotly as py
#Question 1
years = [1989, 1990, 1991, 1992, 1993, 1994, 1995]
males = [23742, 26752, 30725, 34072, 35551, 37369, 26375]
females = [2613, 3182, 3926, 4741, 5526, 6615, 4881]

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=males,
                    mode='lines+markers',
                name='Male Deaths', line=dict(color='firebrick', width=4)))

fig.update_layout(title='Male Deaths per Year',
                   xaxis_title='Year',
                   yaxis_title='Number Of Deaths')

fig.write_html('Line_Graph_Depicting_Male_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=females,
                    mode='lines+markers',
                name='Female Deaths', line=dict(color='firebrick', width=4)))

fig.update_layout(title='Female Deaths per Year',
                   xaxis_title='Year',
                   yaxis_title='Number Of Deaths')

fig.write_html('Line_Graph_Depicting_Female_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()

fig.add_trace(go.Scatter(x=years, y=females,
                    mode='lines+markers',
                name='Females', line=dict(color='firebrick', width=4)))

fig.add_trace(go.Scatter(x=years, y=males,
                    mode='lines+markers',
                name='Males', line=dict(color='royalblue', width=4)))

fig.update_layout(title='Deaths per Year',
                   xaxis_title='Year',
                   yaxis_title='Number Of Deaths')

fig.write_html('Line_Graph_Depicting_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=years,
    y=males,
    name='Males',
    marker_color='firebrick'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(title = 'Male Deaths per Year', xaxis_title='Year',
yaxis_title='Number Of Deaths', barmode='group')
fig.write_html('Bar_Graph_Depicting_Male_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=years,
    y=females,
    name='Females',
    marker_color='firebrick'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(title = 'Female Deaths per Year', xaxis_title='Year',
yaxis_title='Number Of Deaths', barmode='group')
fig.write_html('Bar_Graph_Depicting_Female_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=males,
                name='Males',
                marker_color='rgb(55, 83, 109)'
                ))

fig.add_trace(go.Bar(x=years,
                y=females,
                name='Females',
                marker_color='firebrick'
                ))

fig.update_layout(
    title='Deaths per Year',
    xaxis_tickfont_size=14,
    yaxis_title='Number of Deaths',
    xaxis_title = 'Year',
    barmode='group',
)
fig.write_html('Bar_Graph_Depicting_Deaths_per_Year.html', auto_open=False)

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=males,
                name='Males',
                marker_color='rgb(55, 83, 109)'
                ))

fig.add_trace(go.Bar(x=years,
                y=females,
                name='Females',
                marker_color='firebrick'
                ))

fig.update_layout(
    title='Deaths per Year',
    xaxis_tickfont_size=14,
    yaxis_title='Number of Deaths',
    xaxis_title = 'Year',
    barmode='stack',
)
fig.write_html('Component_Bar_Graph_Depicting_Deaths_per_Year.html', auto_open=False)

total = sum(males) + sum(females)
malespercentage = [x*100/total for x in males]
femalespercentage = [x*100/total for x in females]

fig = go.Figure()

fig.add_trace(go.Bar(x=years,
                y=malespercentage,
                name='Males',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=years,
                y=femalespercentage,
                name='Females',
                marker_color='firebrick'
                ))


fig.update_layout(
    title='Deaths per Year',
    xaxis_tickfont_size=14,
    yaxis_title='Percentage of Deaths',
    xaxis_title = 'Year',
    barmode='stack',
)
fig.write_html('Component_Bar_Graph_Depicting_Percentage_Deaths_per_Year.html', auto_open=False)

labels = [str(x)+"-Males" for x in years]
labels = labels + [str(x)+"-Females" for x in years]
data = malespercentage + femalespercentage

fig = go.Figure(data=[go.Pie(labels=labels,
                             values=data)])
fig.update_traces( hoverinfo='label', textinfo='value', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Percentage of deaths by year and sex')
fig.write_html('Pie_Graph_Depicting_Percentage_Deaths_per_Year_and_Sex.html', auto_open=False)

femurLengths = [3.8, 3.6, 4.3, 3.5, 4.3, 3.3, 4.3, 3.9, 4.3, 3.8, 3.9, 4.4, 3.8, 4.7, 3.6, 4.1, 4.4, 4.5, 3.6, 3.8, 4.4, 4.1, 3.6, 4.2, 3.9]

fig = go.Figure(data=[go.Histogram(x=femurLengths, marker_color='#330C73',
    opacity=0.75)])
fig.update_layout(
    title_text='Histogram Of Femur Lengths', # title of plot
    xaxis_title_text='Femur Length (x 10^{-1})',xaxis_title_font_size=15, # xaxis label
    yaxis_title_text='Count', # yaxis label
)


fig.show()
