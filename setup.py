from setuptools import find_packages, setup

setup(
      name='robotframework-screen-recorder',
      version="0.2",
      description='Robotframework listener to record execution screen',
      long_description='Robotframework listener to record execution screen using ScreenCapLibrary',
      classifiers=[
          'Framework :: Robot Framework',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='robotframework screen recorder',
      author='Shiva Prasad Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/robotframework-screen-recorder',
      license='MIT',

      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'robotframework',
          'robotframework-screencaplibrary'
      ],
)