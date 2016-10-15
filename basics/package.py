#Variables usually go inside functions. Functions and global variables usually go inside modules.
# What if you wanted to organize modules? That’s where packages come into the picture.

#Packages are just folders of modules with a special __init__.py file
# that indicates to Python that this folder is special because it contains Python modules.
#
# -world/
#         -__init__.py
#         -asia/
#               -__init__.py
#               -india/
#                      -__init__.py
#                        -foo.py
#
#          -africe/
#                   -__init__.py
#                   -madagascar/
#                               -__init__.py
#                               -bar.py

#packages are just convenience to hierarchically organize modules