#!/usr/bin/env python3
import altair as alt


@alt.theme.register("kai_theme", enable=True)
def theme_kai():
    mark_color = ("#f7d060",)
    palette = dict(
        black="#000000",
        white="#ffffff",
        bg="#202124",
    )
    return {
        "config": {
            "view": {"strokeOpacity": 0},
            "background": palette["bg"],
            "mark": {"color": "red", "fill": mark_color, "stroke": mark_color, "fillOpacity": 1},
            "rule": {"color": mark_color, "stroke": mark_color},
            "title": {"color": "white"},
            "header": {"labelColor": "white", "titleColor": "white"},
            "axis": {"labelColor": "white", "titleColor": "white", "gridOpacity": 0.2},
            "range": {
                "category": [
                    "#f7d060",
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c",
                    "#d62728",
                    "#9467bd",
                    "#8c564b",
                    "#e377c2",
                    "#7f7f7f",
                    "#17becf",
                ],
            },
        }
    }
