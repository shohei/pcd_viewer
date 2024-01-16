import streamlit as st


import open3d as o3d
import numpy as np
import plotly.graph_objects as go
import tempfile 
import os

st.title("Point Cloud Viewer")
tempfile_dir = tempfile.TemporaryDirectory()
file = st.sidebar.file_uploader("Choose file")

if file is not None:
    pcd_file_path = os.path.join(tempfile_dir.name, file.name) 
    with open(pcd_file_path,"wb") as f:
        f.write(file.getbuffer())

    pcd = o3d.io.read_point_cloud(pcd_file_path)
    points = np.asarray(pcd.points)

    fig = go.Figure(
            data=[
                go.Scatter3d(
                    x=points[:,0], y=points[:,1], z=points[:,2],
                    mode='markers',
                    marker=dict(size=2)
                    )
                ],
            layout=dict(
                autosize=False,
                width=600,
                height=600,
                paper_bgcolor="#fafafa",
                scene=dict(
                    xaxis=dict(visible=False),
                    yaxis=dict(visible=False),
                    zaxis=dict(visible=False)
                    )
                )
            )

    st.write(pcd)
    st.plotly_chart(fig, use_container_width=True)

