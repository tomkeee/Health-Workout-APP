import base64
from io import BytesIO
import matplotlib.pyplot as plt

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(data,**kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(11,4))
    
    x_axis=kwargs.get('x')
    y_axis=kwargs.get('y')
    plt.plot(data[x_axis],data[y_axis],color='green',marker='o')


    plt.tight_layout()
    chart=get_graph()
    return chart