from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="pravee kumar",
    author_email="p.kumar31036@gmail.com",
    install_requires=["huggingface_hub","transformers","accelerate","bitsandbytes","langchain","langchain_community","streamlit","python-dotenv","PyPDF2"]
)