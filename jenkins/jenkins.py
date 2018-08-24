# -*- coding: utf-8 -*-
import jenkins


class JenkinsAPI:
    """
    Installing:
        pip install python-jenkins

    Import:
        import jenkins
    """

    def __init__(self):
        # 使用时修改url、username和密码
        self.url = 'http://127.0.0.1:8080/'
        self.username = 'admin'
        self.password = 'admin'
        self.server = self._connect()

    def _connect(self):
        return jenkins.Jenkins(self.url, username=self.username, password=self.password)

    def get_version(self):
        """get jenkins version"""
        print(self.server.get_version())


if __name__ == '__main__':
    jenkins_obj = JenkinsAPI()
    jenkins_obj.get_version()
