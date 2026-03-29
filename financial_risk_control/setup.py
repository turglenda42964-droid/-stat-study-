from setuptools import find_packages, setup

setup(
    name="financial-risk-control",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["fastapi", "uvicorn", "pydantic", "pandas", "scikit-learn"],
)
