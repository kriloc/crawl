from flask import render_template
from flask import Flask

import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    pyplt = py.offline.plot

    # trace0 =  go.bar(
    #     x = ['A類', 'B類', 'C類'],
    #     y = [20, 14, 23],
    #     text = ['27%佔有率', '24%佔有率', '19%佔有率'],
    #     market = dict(
    #         color = 'rgb(158,202,225)',
    #         line = dict(
    #             color='rgb(8,48,107)',
    #             width=1.5,
    #         )
    #     ),
    #     opacity=0.6
    # )
    trace0 = go.Bar(
        x=['A類戶型', 'B類戶型', 'C類戶型'],
        y=[20, 14, 23],
        text=['27%佔有率', '24%佔有率', '19%佔有率'],
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title = '2017.01不同類型房屋單價情況',
    )
    fig = go.Figure(data = data, layout=layout)
    div = pyplt(fig, output_type='div', auto_open=False, show_link=False, link_text=False,
                include_plotlyjs=False,
                # config=dict(displaylogo=False, modeBarButtonsToRemove=['sendDataToCloud'])
                config = dict(displaylogo=False, displayModeBar=False)
                )
    context = {}
    context['graph'] = div

    import sys
    print('参数div占用内存大小为 %d bytes' % sys.getsizeof(div))

    return render_template("index2.html", title='Home', context=context)


if __name__ == '__main__':
    app.run()