from setuptools import find_packages, setup

setup(
    name="financial-risk-control",
    version="0.2.0",
    description="Industrial-grade financial risk control scaffold",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pydantic-settings",
        "pandas",
        "scikit-learn",
    ],
)
