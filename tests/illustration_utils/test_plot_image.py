import pytest
import sys
import os
from unittest.mock import MagicMock
from illustration_utils.plot_image import show_illustration

# Add src to path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))


def test_show_illustration_image_only(mocker):
    # Patch dependencies using the mocker fixture (requires pytest-mock)
    mock_plt = mocker.patch("illustration_utils.plot_image.plt")
    mock_mpimg = mocker.patch("illustration_utils.plot_image.mpimg")
    mock_assets = mocker.patch("illustration_utils.plot_image.ASSETS_DIR")

    # Setup fig, ax
    mock_fig, mock_ax = MagicMock(), MagicMock()
    mock_plt.subplots.return_value = (mock_fig, mock_ax)

    # Fake image path
    mock_image_path = MagicMock()
    mock_image_path.exists.return_value = True
    mock_assets.__truediv__.return_value = mock_image_path

    fig, ax = show_illustration("image.png")

    mock_mpimg.imread.assert_called_once_with(str(mock_image_path))
    mock_ax.imshow.assert_called_once()
    mock_ax.axis.assert_called_once_with("off")

    assert fig is mock_fig
    assert ax is mock_ax

def test_show_illustration_with_source(mocker):
    mock_plt = mocker.patch("illustration_utils.plot_image.plt")
    mock_mpimg = mocker.patch("illustration_utils.plot_image.mpimg")
    mock_assets = mocker.patch("illustration_utils.plot_image.ASSETS_DIR")

    mock_fig, mock_ax = MagicMock(), MagicMock()
    mock_plt.subplots.return_value = (mock_fig, mock_ax)

    mock_image = MagicMock()
    mock_image.exists.return_value = True

    mock_source = MagicMock()
    mock_source.exists.return_value = True
    mock_source.read_text.return_value = "Test Source"

    # Clean side_effect using a lambda dictionary lookup
    mock_assets.__truediv__.side_effect = lambda p: {
        "image.png": mock_image,
        "source.txt": mock_source,
    }[p]

    show_illustration("image.png", "source.txt")

    mock_plt.figtext.assert_called_once()
    args, _ = mock_plt.figtext.call_args
    assert "Test Source" in args[2]
