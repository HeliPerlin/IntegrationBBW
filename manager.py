import camera
import alarm


class manager:

    def __init__(self):
        """
        initiates a new manager object
        """
        self.alarm_device = alarm.alarm()
        self.camera_device = camera.camera()

    def run(self):
        """
        Runs the whole program
        :return: None
        """
        while True:
            if self.camera_device.is_detecting():
               self.alarm_device.switch_alarm()

