# This file is an initial API for the BayBWatch project- main flow

# Assumptions:
# There's a function\ class responsible for video calls
# There exists a module that's responsible for handling the camera

import manager


if __name__ == '__main__':
    new_manager = manager.manager()
    new_manager.run()