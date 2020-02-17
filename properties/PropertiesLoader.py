import conftest


class PropertiesLoader:

    def __init__(self):
        if not conftest.host() is None:
            self._host = conftest.host()
        self._ip = conftest.ip()
        self._staff_port = 81
        self._users_port = 80
        self._ssh_user = "autotest"
        self._ssh_port = 22
        self._wait_delay = 20

    @property
    def properties(self):
        return self

    @property
    def ip(self):
        return self._ip

    @property
    def host(self):
        return self._host

    @property
    def staff_port(self):
        return self._staff_port

    @property
    def users_port(self):
        return self._users_port

    @property
    def ssh_user(self):
        return self._ssh_user

    @property
    def ssh_port(self):
        return self._ssh_port

    @property
    def wait_delay(self):
        return self._wait_delay

