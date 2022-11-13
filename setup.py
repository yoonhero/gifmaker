import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_gifmaker",
    version="0.0.1",
    author="Yoonhero",
    author_email="yoonhero06@naver.com",
    description="You can make a simple gif easily with this GIFMAKER",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoonhero/gifmaker",
    project_urls={
        "Bug Tracker": "https://github.com/schooldevops/gifmaker",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)