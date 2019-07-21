# -*- coding: utf-8 -*-

"""
TODO
"""

import json
import logging

import plotly
import plotly.graph_objs as go

from speedtest_reader import util

__author__ = "Tobias Frei"
__copyright__ = "Tobias Frei"
__license__ = "mit"

logger = logging.getLogger(__name__)


@util.stopwatch
def plot(df, title):
    """
    TODO
    Upon success a plotly-JSON-encoded graph is returned.
    """
    graph = dict(
        data=[
            go.Scatter(
                x=df["tslocal"],
                y=df["Download"],
                mode="lines",
                connectgaps=False,
                name="Download"
            ),
            go.Scatter(
                x=df["tslocal"],
                y=df["Upload"],
                mode="markers",
                name="Upload"
            ),
        ],
        # TODO Graph width/ height: plotly only accepts px values so far,
        #      so set these with care and watch out for API improvements.
        layout=go.Layout(
            title=f"{title}",
            yaxis={"title": "speed (Mbit/s)"},
            # legend={"x": 0, "y": 1},
            ),
        )

    return json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
