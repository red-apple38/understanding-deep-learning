from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm



def visualize_surface_3d(
    x_mesh: np.ndarray,
    y_mesh: np.ndarray,
    z_values: np.ndarray,
    x_label: str,
    y_label: str,
    z_label: str,
    title: str,
    ax=None,
    cmap=cm.coolwarm,
    alpha: float = 0.85,
    linewidth: float = 0,
    antialiased: bool = True,
    z_lim: tuple[float, float] | None = None,
    show_colorbar: bool = True,
    colorbar_label: str | None = None,
    colorbar_shrink: float = 0.5,
    colorbar_aspect: int = 8,
    z_major_locator: int | None = 10,
    z_formatter: str | None = "{x:.02f}",
    view_elev: float | None = None,
    view_azim: float | None = None,
):
    """
    Visualizes a 3D surface.

    Args:
        x_mesh (np.ndarray):
            Meshgrid values for the x-axis
        y_mesh (np.ndarray):
            Meshgrid values for the y-axis
        z_values (np.ndarray):
            Surface values with the same shape as x_mesh and y_mesh
        x_label (str):
            Label for the x-axi
        y_label (str):
            Label for the y-axis
        z_label (str):
            Label for the z-axis
        title (str):
            Plot title
        ax:
            Optional 3D axes object. If None, a new figure and 3D axes are created.
        cmap:
            Matplotlib colormap for the surface.
        alpha (float):
            Surface transparency.
        linewidth (float):
            Line width of the surface grid
        antialiased (bool):
            Whether to smooth surface edges
        z_lim:
            Optional tuple specifying the z-axis limits
        show_colorbar (bool):
            Whether to add a colorbar
        colorbar_label:
            Optional label for the colorbar
        colorbar_shrink (float):
            Shrink factor for the colorbar
        colorbar_aspect (int):
            Aspect ratio for the colorbar
        z_major_locator:
            Optional number of major ticks on the z-axis
        z_formatter:
            Optional formatter string for z-axis values
        view_elev:
            Optional elevation angle for the 3D view
        view_azim:
            Optional azimuth angle for the 3D view

    Returns:
        fig, ax, surf:
            Matplotlib figure, axes and surface object
    """
    assert x_mesh.shape == y_mesh.shape == z_values.shape, (
        "x_mesh, y_mesh and z_values must have the same shape"
    )

    if ax is None:
        fig = plt.figure(figsize=(14, 7))
        ax = fig.add_subplot(111, projection="3d")
    else:
        fig = ax.figure

    surf = ax.plot_surface(
        x_mesh,
        y_mesh,
        z_values,
        cmap=cmap,
        alpha=alpha,
        linewidth=linewidth,
        antialiased=antialiased,
        zsort="average"
    )

    if z_lim is not None:
        ax.set_zlim(z_lim)

    if z_major_locator is not None:
        ax.zaxis.set_major_locator(LinearLocator(z_major_locator))

    if z_formatter is not None:
        ax.zaxis.set_major_formatter(z_formatter)

    if view_elev is not None or view_azim is not None:
        ax.view_init(elev=view_elev, azim=view_azim)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.set_title(title)

    if show_colorbar:
        colorbar = fig.colorbar(
            surf,
            ax=ax,
            shrink=colorbar_shrink,
            aspect=colorbar_aspect
        )

        if colorbar_label is not None:
            colorbar.set_label(colorbar_label)

    return fig, ax, surf