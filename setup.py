import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypygifmaker",
    version="0.0.1.1",
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
    license="MIT",
    packages=["pygifmaker"],
    python_requires=">=3.6",
    install_requires=["Pillow"]
)
