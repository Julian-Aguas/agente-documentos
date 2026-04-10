"""
Setup configuration for Agente Local de Documentos
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agente-documentos",
    version="1.0.0",
    author="Julia",
    description="Agente Local de Documentos - Analyze PDFs with AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/agente-documentos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Web Environment :: Streamlit",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit==1.28.1",
        "pymupdf==1.23.8",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
        "reportlab==4.0.7",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "agente-documentos=app:main",
        ],
    },
)
