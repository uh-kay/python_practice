import plotly.express as px
import plotly.graph_objects as go
from refactoring import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Create a scatter plot using Plotly.
    point_numbers = list(range(rw.num_points))
    fig = go.Figure()

    # Add scatter plot for all points
    fig.add_trace(go.Scatter(
        x=rw.x_values,
        y=rw.y_values,
        mode='markers',
        marker=dict(
            size=3,
            color=point_numbers,
            colorscale='Blues',
            showscale=False,
        )
    ))

    # Emphasize the first and last points.
    fig.add_trace(go.Scatter(
        x=[0],
        y=[0],
        mode='markers',
        marker=dict(
            size=10,
            color='green'
        ),
        name='Start'
    ))
    fig.add_trace(go.Scatter(
        x=[rw.x_values[-1]],
        y=[rw.y_values[-1]],
        mode='markers',
        marker=dict(
            size=10,
            color='red'
        ),
        name='End'
    ))

    # Update layout to remove axes and set aspect ratio.
    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        autosize=False,
        width=1000,
        height=600,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
