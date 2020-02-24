import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voice_assistant", # Replace with your own username
    version="0.0.1",
    author="Leonard Loh Kin Yung",
    author_email="leonard_loh@hotmail.com",
    description="A voice assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonardlohky/voice_assistant",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

