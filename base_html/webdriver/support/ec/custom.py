class ExecScript(object):
    """
    """
    def __init__(self, script):
        self._script = script

    def __call__(self, driver):
        element = driver.execute_script(self._script)
        if element == 0:
            return True
        else:
            return False
