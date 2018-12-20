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
        # 目前python-jenkins模块调用get_version()存在bug，故加入get_whoami()
        self.server.get_whoami()

    def _connect(self):
        return jenkins.Jenkins(self.url, username=self.username, password=self.password)

    def get_version(self):
        """get jenkins version"""
        print(self.server.get_version())        
        
    def get_config(self, name):
        """get job config"""
        return self.server.get_job_config(name)

    def create_job(self, name, xml):
        """create new job"""
        return self.server.create_job(name, xml)

    def build_job(self, name, *args, **kwargs):
        """build job"""
        return self.server.build_job(name, *args, **kwargs)

    def delete_job(self, name):       
        return self.server.delete_job(name)


if __name__ == '__main__':
    jenkins_obj = JenkinsAPI()
    jenkins_obj.get_version()
