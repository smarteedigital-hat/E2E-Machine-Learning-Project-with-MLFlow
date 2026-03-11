import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "E2E-Machine-Learning-Project-with-MLFlow"
AUTHOR_USER_NAME = "smarteedigital-hat"
SRC_REPO = "MLProject"
AUTHOR_EMAIL = "haluk.a.turan@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "mlflow",
        "notebook",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "python-box",
        "pyYAML",
        "tqdm",
        "ensure",
        "joblib",
        "types-pyYAML",
        "Flask",
        "Flask-Cors",
    ],
)