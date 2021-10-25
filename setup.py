from setuptools import setup
from setuptools import find_packages

setup(name='Rotation-Equivariant-Deforestation-Segmentation',
      version='1.0',
      description='Rotation-Equivariant-Deforestation-Segmentation in PyTorch',
      author='Josh Mitton',
      author_email='j.mitton.1@research.gla.ac.uk',
      url='https://joshuamitton.github.io',
      download_url='https://github.com//JoshuaMitton/Rotation-Equivariant-Deforestation-Segmentation',
      license='MIT',
      install_requires=['numpy>=1.20.3',
                        'torch>=1.7.1',
                        'torchvision>=0.8.2',
                        'tqdm>=4.62.3',
                        'Shapely>=1.7.1',
                        'pandas>=1.3.2',
                        'opencv-python>=4.5.3.56',
                        'matplotlib>=3.3.4',
                        'e2cnn>=0.1.5',
                        'scipy>=1.6.0'                                                ],
      package_data={'Rotation-Equivariant-Deforestation-Segmentation': ['README.md']},
      packages=find_packages())
