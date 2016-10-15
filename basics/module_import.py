import module_create

module_create.sayHai()
print('version = ', module_create.__version__)


#another way of importing, here we import only rrequired ones
from module_create import sayHai, __version__
sayHai()
print('Version', __version__)