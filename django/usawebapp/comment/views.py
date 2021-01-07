from django.shortcuts import render, HttpResponse,redirect
from .models import Comment
import plotly.io as pio
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


# Create your views here.
def index(request):

    wide_df = pd.read_csv('C:/Users/Baha/Desktop/django/usawebapp/tablo8.csv')

    fig = px.bar(wide_df, x="Candidate",
             y=["Total Vote (Million)", "Total Delegate Count", "Total Vote Percentage (%)"],
            facet_col="variable",color="Candidate",title="2020 US Election Results Bar Charts",
             color_discrete_map = {"Joe Biden": "blue", "Donald Trump": "red", "Others":"green"}
             )
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    barChart = pio.to_html(fig,include_plotlyjs=False, full_html = False)

    df = pd.read_csv('C:/Users/Baha/Desktop/django/usawebapp/tablo9.csv')

    
    for col in df.columns:
        df[col] = df[col].astype(str)

    df['text'] = df['state'] + '<br>' + \
        'Winner : ' + df['winner'] + '<br>' + \
        'Biden Votes ' + df['dem_votes'] + ' Biden Percent ' + df['dem_percent'] + '<br>' + \
        'Trump Votes ' + df['rep_votes'] + ' Trump Percent ' + df['rep_percent'] + '<br>'

    figMap = go.Figure(data=go.Choropleth(
        locations=df['stateid'],
        z=df['winner_num'],
        locationmode='USA-states',
        colorscale='Bluered_r',
        autocolorscale=False,
        text=df['text'], # hover text
        showscale=False,
        marker_line_color='white', # line markers between states
        colorbar_title="Joe Biden"
    ))

    figMap.update_layout(
        title_text='2020 US Election Results Map<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor='rgb(255, 255, 255)'),
    )
    usaMap = pio.to_html(figMap,include_plotlyjs=False, full_html = False)

    comments = Comment.objects.all()

    return render(request,"index.html",{"barChart" : barChart,"usaMap" : usaMap ,"comments" : comments})


def addComment(request):
    if request.method ==  "GET":
        return redirect("/")
    else:
        nickName = request.POST.get("nickName")
        userComment = request.POST.get("comment")
        newComment = Comment(nickName = nickName, userComment = userComment)

        newComment.save()
        return redirect("/")

# def barChart(request):

    
#     return render(request,"plotly_demo.html",{"div" : div})