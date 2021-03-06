from distutils.core import setup

setup(
  name = 'LinkToExe',         # How you named your package folder (MyLib)
  packages = ['LinkToExe'],   # Chose the same as "name"
  version = '0.11',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package will help you use mediapipe tools easily',
  long_description="LinkToExe is a python package that will help you to use a link in form of a pyqt5 app and the "
                   "with the help of pyinstaller, you can convert the app to a desktop exe. For more information. For "
                   "more information, check the repository https://github.com/chinmay18030/linktoexe",

  author = 'Ace Tech Academy',                   # Type in your name
  author_email = 'aceteachacademy@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/chinmay18030/linktoexe',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Link to exe', 'LinkToExe'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'PyQt5',
          'PyQtWebEngine',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)