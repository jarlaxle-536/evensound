import inspect
import sys

import logic

functionality_packages_names = [name for name in sorted(sys.modules)
    if name.startswith('logic.') and name.count('.') == 1]
functionality_packages_names.sort()
for module_name in functionality_packages_names:
    print(module_name.upper())
    defined = dict(inspect.getmembers(sys.modules[module_name]))
    print(defined)
