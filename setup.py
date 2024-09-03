from setuptools import setup, find_packages
from typing import List

setup(
    name = "WebScraperChatBot",
    version="0.0.1",
    author="sawan yadav",
    author_email="sawan.gomia@gmail.com",
    install_requires=["streamlit","torch","transformers","flask","beautifulsoup4","requests"],
    packages=find_packages()
)