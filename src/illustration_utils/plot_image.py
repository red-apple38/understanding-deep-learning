import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# Define the path to the assets directory using pathlib
ASSETS_DIR = Path(__file__).resolve().parents[2] / "docs" / "assets"

def show_illustration(
    image_relative_path,
    source_relative_path=None,
    *,
    assets_dir=None,
    **kwargs,
):
    """
    Loads an image from the assets directory and displays it, optionally with a source citation.

    This function reads an image relative to the `docs/assets` directory and displays it
    using matplotlib. If `source_relative_path` is provided, the content of the text file
    is added as a citation below the image.

    Args:
        image_relative_path (str): The path to the image file, relative to `docs/assets`
                                   (e.g., 'illustrations/beginner/perceptron/perceptron.ppm').
        source_relative_path (str, optional): The path to the text file with the source,
                                              relative to `docs/assets`. Defaults to None.
        assets_dir (str or Path, optional): Override the directory from which assets
                                           are loaded. Defaults to the repository's
                                           `docs/assets` directory.
        **kwargs: Additional arguments passed to `plt.subplots()` (e.g., figsize=(10, 5)).

    Returns:
        tuple: (fig, ax) The matplotlib Figure and Axes objects.
    """

    # Construct full paths using pathlib (cleaner path joining)
    assets_root = Path(assets_dir) if assets_dir is not None else ASSETS_DIR
    full_image_path = assets_root / image_relative_path

    # Check if image exists
    if not full_image_path.exists():
        print(f"Error: Image file not found at: {full_image_path}")
        print(f"Looking in assets directory: {assets_root}")
        return None, None

    figsize = kwargs.get('figsize', (7, 4))
    fig, ax = plt.subplots(figsize=figsize)

    # Load and display image
    try:
        img = mpimg.imread(str(full_image_path))
        ax.imshow(img)
        ax.axis('off')
    except Exception as e:
        print(f"Error loading image: {e}")
        return fig, ax

    # Add source if provided
    if source_relative_path:
        full_source_path = assets_root / source_relative_path
        if full_source_path.exists():
            try:
                # Read text directly using pathlib
                source_text = full_source_path.read_text(encoding='utf-8').strip()
                plt.figtext(0.5, 0.01, f"Source: {source_text}", ha="center", fontsize=8,
                            bbox={"facecolor":"white", "alpha":0.5, "pad":5})
            except Exception as e:
                print(f"Could not read source file: {e}")
        else:
            print(f"Warning: Source text file not found at: {full_source_path}")

    return fig, ax
