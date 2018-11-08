from setuptools import setup

setup(name='jtnn',
      version='0.1.1',
      url='https://github.com/maxmed/icml18-jtnn',
      license='MIT',
      install_requires=[
          'joblib==0.12.5',
          'numpy==1.15.2',
          'torch==0.3.1',
          'networkx==2.1',
          'scipy==1.1.0',
          'tqdm==4.26.0',
      ],
      python_requires='>=3.6',
      extras_require={
          'rdkit': ['rdkit>=2018.09.1.0'],
      },
      include_package_data=True,
      )
