import setuptools

with open("README.md", "r", encoding="utf-8_sig") as fh:
    long_description = fh.read()

setuptools.setup(
    name="romajitable",
    version="0.0.1",
    author="KotRik",
    author_email="supadmin@kotrik.ru",
    description="A converted one small script from JS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KotRikD/romajitable",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
