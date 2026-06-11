from importlib import import_module


def test_installed_packages_are_importable():
    modules = [
        "understand_deep_learning",
        "understand_deep_learning.beginner.gradient_descent.gradient_descent",
        "understand_deep_learning.beginner.perceptron.perceptron",
        "understand_deep_learning.illustration_utils.plot_image",
    ]

    for module in modules:
        import_module(module)
