from setuptools import setup, find_packages

setup(
    version="1.0",
    name="generate_subtitle",
    packages=find_packages(),
    py_modules=["generate_subtitle"],
    author="Markell Popov",
    install_requires=[
        'openai-whisper',
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['gen_subtitle=subtitle.cli:main'],
    },
    include_package_data=True,
)
