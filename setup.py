import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="box_space",
    version="0.0.1",
    author="tumzied",
    author_email="tumziedrahman@gmial.com",
    description="A small box in space play ee-err",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "box_space"},
    packages=setuptools.find_packages(where="box_space"),
    python_requires=">=3.6",
    install_requires=[
        'pynput',
        'playsound',
    ],
    include_package_data=True,
)