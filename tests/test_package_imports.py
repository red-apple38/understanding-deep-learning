from importlib import import_module


def test_installed_packages_are_importable():
    modules = [
        "beginner.gradient_descent.gradient_descent",
        "beginner.perceptron.perceptron",
        "illustration_utils.plot_image",
    ]

    for module in modules:
        import_module(module)
