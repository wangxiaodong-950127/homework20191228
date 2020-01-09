#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 14:42
# @Author  : GXl
# @File    : jenkins
# 定义远程的jenkins master server的url，用户名和密码
import jenkins

jenkins_server_url='http://127.0.0.1:8080/'
username='wangxiaodong-950127'
password='wxd950127'
job_name='PyDemo'
server=jenkins.Jenkins(jenkins_server_url, username=username, password=password)

# 获取job名为job_name的信息
print ("######",server.get_job_info(job_name))

# 获取job名为job_name的job的最后次构建号
build_number=server.get_job_info(job_name)['lastCompletedBuild']['number']

print (build_number)

# 获取job名为job_name的job的某次构建的执行结果状态
print("######",server.get_build_info(job_name,build_number)['result'])

#server.build_job(job_name)


server.create_job("APIDemo","")
