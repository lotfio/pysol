from distutils.core import setup
setup(
  name = 'pysol',         # How you named your package folder (MyLib)
  packages = ['pysol'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'pysol python console applications made easy',   # Give a short description about your library
  author = 'lotfio lakehal',                   # Type in your name
  author_email = 'contact@lotfio.net',      # Type in your E-Mail
  url = 'https://github.com/lotfio/pysol',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/lotfio/pysol/archive/master.zip',    # I explain this later on
  keywords = ['console app', 'pysol', 'python console apps', 'terminal'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development',
    'License :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)