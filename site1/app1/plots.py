import datetime
import glob
import logging
import os

import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

logger = logging.getLogger(__name__)


def plot1d():
    x_data = np.arange(0, 120, 0.1)
    trace1 = go.Scatter(
        x=x_data,
        y=np.sin(x_data)
    )

    data = [trace1]
    layout = go.Layout(
        # autosize=False,
        # width=900,
        # height=500,

        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div


def plot2d():
    t = np.linspace(-1, 1, 2000)
    x = (t**2) + (0.5 * np.random.randn(2000))
    y = (t**2) + (0.5 * np.random.randn(2000))

    trace1 = go.Scatter(
        x=x, y=y, mode='markers', name='points',
        marker=dict(color='rgb(0,0,0)', size=2, opacity=0.4)
    )
    trace2 = go.Histogram2d(
        x=x, y=y, name='density',
        nbinsx=100, nbinsy=100,
        colorscale='Jet', reversescale=False, showscale=True
    )
    trace3 = go.Histogram(
        x=x, name='x density',
        marker=dict(color='blue'),
        yaxis='y2'
    )
    trace4 = go.Histogram(
        y=y, name='y density', marker=dict(color='blue'),
        xaxis='x2'
    )
    data = [trace1, trace2, trace3, trace4]

    layout = go.Layout(
        showlegend=False,
        autosize=False,
        width=800,
        height=700,
        xaxis=dict(
            domain=[0, 0.85],
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            domain=[0, 0.85],
            showgrid=False,
            zeroline=False
        ),
        margin=dict(
            t=50
        ),
        hovermode='closest',
        bargap=0,
        xaxis2=dict(
            domain=[0.85, 1],
            showgrid=False,
            zeroline=False
        ),
        yaxis2=dict(
            domain=[0.85, 1],
            showgrid=False,
            zeroline=False
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plot3d():
    data = [
        go.Surface(
            z=[
                [27.80985, 49.61936, 83.08067, 116.6632, 130.414, 150.7206,
                220.1871, 156.1536, 148.6416, 203.7845, 206.0386, 107.1618,
                68.36975, 45.3359, 49.96142, 21.89279, 17.02552, 11.74317,
                14.75226, 13.6671, 5.677561, 3.31234, 1.156517, -0.147662],
                [27.71966, 48.55022, 65.21374, 95.27666, 116.9964, 133.9056,
                152.3412, 151.934, 160.1139, 179.5327, 147.6184, 170.3943,
                121.8194, 52.58537, 33.08871, 38.40972, 44.24843, 69.5786,
                4.019351, 3.050024, 3.039719, 2.996142, 2.967954, 1.999594],
                [30.4267, 33.47752, 44.80953, 62.47495, 77.43523, 104.2153,
                102.7393, 137.0004, 186.0706, 219.3173, 181.7615, 120.9154,
                143.1835, 82.40501, 48.47132, 74.71461, 60.0909, 7.073525,
                6.089851, 6.53745, 6.666096, 7.306965, 5.73684, 3.625628],
                [16.66549, 30.1086, 39.96952, 44.12225, 59.57512, 77.56929,
                106.8925, 166.5539, 175.2381, 185.2815, 154.5056, 83.0433,
                62.61732, 62.33167, 60.55916, 55.92124, 15.17284, 8.248324,
                36.68087, 61.93413, 20.26867, 68.58819, 46.49812, 0.2360095],
                [8.815617, 18.3516, 8.658275, 27.5859, 48.62691, 60.18013,
                91.3286, 145.7109, 116.0653, 106.2662, 68.69447, 53.10596, 37.92797, 47.95942, 47.42691, 69.20731, 44.95468, 29.17197, 17.91674, 16.25515, 14.65559, 17.26048, 31.22245, 46.71704], [6.628881, 10.41339, 24.81939, 26.08952, 30.1605, 52.30802, 64.71007, 76.30823, 84.63686, 99.4324, 62.52132, 46.81647, 55.76606, 82.4099, 140.2647, 81.26501, 56.45756, 30.42164, 17.28782, 8.302431, 2.981626, 2.698536, 5.886086, 5.268358], [21.83975, 6.63927, 18.97085, 32.89204, 43.15014, 62.86014, 104.6657, 130.2294, 114.8494, 106.9873, 61.89647, 55.55682, 86.80986, 89.27802, 122.4221, 123.9698, 109.0952, 98.41956, 77.61374, 32.49031, 14.67344, 7.370775, 0.03711011, 0.6423392], [53.34303, 26.79797, 6.63927, 10.88787, 17.2044, 56.18116, 79.70141, 90.8453, 98.27675, 80.87243, 74.7931, 75.54661, 73.4373, 74.11694, 68.1749, 46.24076, 39.93857, 31.21653, 36.88335, 40.02525, 117.4297, 12.70328, 1.729771, 0], [25.66785, 63.05717, 22.1414, 17.074, 41.74483, 60.27227, 81.42432, 114.444, 102.3234, 101.7878, 111.031, 119.2309, 114.0777, 110.5296, 59.19355, 42.47175, 14.63598, 6.944074, 6.944075, 27.74936, 0, 0, 0.09449376, 0.07732264], [12.827, 69.20554, 46.76293, 13.96517, 33.88744, 61.82613, 84.74799, 121.122, 145.2741, 153.1797, 204.786, 227.9242, 236.3038, 228.3655, 79.34425, 25.93483, 6.944074, 6.944074, 6.944075, 7.553681, 0, 0, 0, 0], [0, 68.66396, 59.0435, 33.35762, 47.45282, 57.8355, 78.91689, 107.8275, 168.0053, 130.9597, 212.5541, 165.8122, 210.2429, 181.1713, 189.7617, 137.3378, 84.65395, 8.677168, 6.956576, 8.468093, 0, 0, 0, 0], [0, 95.17499, 80.03818, 59.89862, 39.58476, 50.28058, 63.81641, 80.61302, 66.37824, 198.7651, 244.3467, 294.2474, 264.3517, 176.4082, 60.21857, 77.41475, 53.16981, 56.16393, 6.949235, 7.531059, 3.780177, 0, 0, 0], [0, 134.9879, 130.3696, 96.86325, 75.70494,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             58.86466, 57.20374, 55.18837, 78.128, 108.5582, 154.3774, 319.1686, 372.8826, 275.4655, 130.2632, 54.93822, 25.49719, 8.047439, 8.084393, 5.115252, 5.678269, 0, 0, 0], [0, 48.08919, 142.5558, 140.3777, 154.7261, 87.9361, 58.11092, 52.83869, 67.14822, 83.66798, 118.9242, 150.0681, 272.9709, 341.1366, 238.664, 190.2, 116.8943, 91.48672, 14.0157, 42.29277, 5.115252, 0, 0, 0], [0, 54.1941, 146.3839, 99.48143, 96.19411, 102.9473, 76.14089, 57.7844, 47.0402, 64.36799, 84.23767, 162.7181, 121.3275, 213.1646, 328.482, 285.4489, 283.8319, 212.815, 164.549, 92.29631, 7.244015, 1.167, 0, 0], [0, 6.919659, 195.1709, 132.5253, 135.2341, 89.85069, 89.45549, 60.29967, 50.33806, 39.17583, 59.06854, 74.52159, 84.93402, 187.1219, 123.9673, 103.7027, 128.986, 165.1283, 249.7054, 95.39966, 10.00284, 2.39255, 0, 0], [0, 21.73871, 123.1339, 176.7414, 158.2698, 137.235, 105.3089, 86.63255, 53.11591, 29.03865, 30.40539, 39.04902, 49.23405, 63.27853, 111.4215, 101.1956, 40.00962, 59.84565, 74.51253, 17.06316, 2.435141, 2.287471, -0.0003636982, 0], [0, 0, 62.04672, 136.3122, 201.7952, 168.1343, 95.2046, 58.90624, 46.94091, 49.27053, 37.10416, 17.97011, 30.93697, 33.39257, 44.03077, 55.64542, 78.22423, 14.42782, 9.954997, 7.768213, 13.0254, 21.73166, 2.156372, 0.5317867], [0, 0, 79.62993, 139.6978, 173.167, 192.8718, 196.3499, 144.6611, 106.5424, 57.16653, 41.16107, 32.12764, 13.8566, 10.91772, 12.07177, 22.38254, 24.72105, 6.803666, 4.200841, 16.46857, 15.70744, 33.96221, 7.575688, -0.04880907], [0, 0, 33.2664, 57.53643, 167.2241, 196.4833, 194.7966, 182.1884, 119.6961, 73.02113, 48.36549, 33.74652, 26.2379, 16.3578, 6.811293, 6.63927, 6.639271, 8.468093, 6.194273, 3.591233, 3.81486, 8.600739, 5.21889, 0], [0, 0, 29.77937, 54.97282, 144.7995, 207.4904, 165.3432, 171.4047, 174.9216, 100.2733, 61.46441, 50.19171, 26.08209, 17.18218, 8.468093, 6.63927, 6.334467, 6.334467, 5.666687, 4.272203, 0, 0, 0, 0], [0, 0, 31.409, 132.7418, 185.5796, 121.8299, 185.3841, 160.6566, 116.1478, 118.1078, 141.7946, 65.56351, 48.84066, 23.13864, 18.12932, 10.28531, 6.029663, 6.044627, 5.694764, 3.739085, 3.896037, 0, 0, 0], [0, 0, 19.58994, 42.30355, 96.26777, 187.1207, 179.6626, 221.3898, 154.2617, 142.1604, 148.5737, 67.17937, 40.69044, 39.74512, 26.10166, 14.48469, 8.65873, 3.896037, 3.571392, 3.896037, 3.896037, 3.896037, 1.077756, 0], [0.001229679, 3.008948, 5.909858, 33.50574, 104.3341, 152.2165, 198.1988, 191.841, 228.7349, 168.1041, 144.2759, 110.7436, 57.65214, 42.63504, 27.91891, 15.41052, 8.056102, 3.90283, 3.879774, 3.936718, 3.968634, 0.1236256, 3.985531, -0.1835741], [0, 5.626141, 7.676256, 63.16226, 45.99762, 79.56688, 227.311, 203.9287, 172.5618, 177.1462, 140.4554, 123.9905, 110.346, 65.12319, 34.31887, 24.5278, 9.561069, 3.334991, 5.590495, 5.487353, 5.909499, 5.868994, 5.833817, 3.568177]]
        )
    ]
    layout = go.Layout(
        title='3d Plot of the Mt Bruno Elevation',
        autosize=False,
        width=800,
        height=800,
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plot1d_multiple(n):
    '''
    n = number of plots. It is a random number coming from JS.
    This basically tests the speed of PlotLy for multiple plots.
    '''
    x_array = []
    y_array = []
    n_points = 100
    x = np.arange(0.001, 1, 1/n_points)
    for i in range(n):
        x_array.append(x)
        y_array.append(np.sin(x*np.pi*(i+2)))
    data = []
    for x, y in zip(x_array, y_array):
        trace = go.Scatter(x=x, y=y)
        data.append(trace)

    layout = go.Layout(
        height=600,
        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plotIq():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_files = glob.glob(current_dir + '/data/scan*_Iq.txt')

    data = []
    for filename in data_files:
        csv = np.genfromtxt(filename, delimiter=None,  comments='#')
        x = csv[:, 0]
        y = csv[:, 1]
        trace = go.Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            name=filename.split('/')[-1],
            error_y=dict(
                type='data',
                visible=True,
                array=np.sqrt(csv[:, 1]),
                thickness=1.5,
                width=3,
                opacity=0.5
            ),
        )
        data.append(trace)

    layout = go.Layout(
        height=600,
        xaxis=dict(
            autorange=True,
            type='log',
        ),
        yaxis=dict(
            autorange=True,
            type='log',
        ),
        title="Iq chart"
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def live_plot_get_x_y_data():
    """
    Generates normal distributed 2D points
    Numer of points depends on the real time seconds.
    """
    now = datetime.datetime.now()
    n_points = 100 * now.second
    mean = [0, 0]
    cov = [[1, 0], [0, 1]]  # diagonal covariance
    x, y = np.random.multivariate_normal(mean, cov, n_points).T
    return x, y


def live_plot_get_data():
    """
    Data to generate the first plot
    """
    x, y = live_plot_get_x_y_data()
    data = dict(
        x=x, y=y, mode='markers', name='points',
        marker=dict(color='rgb(0,0,0)', size=4, opacity=0.4)
    )
    return data


def live_plot_get_data_serialized():
    """
    Data to generate the updated plot.
    It will serialized by the Django view
    """
    x, y = live_plot_get_x_y_data()
    data = dict(
        x=x.tolist(), y=y.tolist(), mode='markers', name='points',
        marker=dict(color='rgb(0,0,0)', size=4, opacity=0.4)
    )
    return data


def plotLive():

    trace = go.Scatter(live_plot_get_data())
    data = [trace]

    layout = go.Layout(
        showlegend=False,
        autosize=False,
        width=800,
        height=700,
        xaxis=dict(
            range=[-4, 4],
        ),
        yaxis=dict(
            range=[-4, 4],
        ),
        margin=dict(
            t=50
        ),
        hovermode='closest',
        bargap=0,
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
