#!/usr/bin/env python
#coding=utf8
import qiniu.conf
import qiniu.rsf
import qiniu.rs
import qiniu.io
import sys
import qiniu.resumable_io as rio

#设置在七牛申请的key
qiniu.conf.ACCESS_KEY = "xxxxxxxxxxxx"
qiniu.conf.SECRET_KEY = "xxxxxxxxxxxx"
#设置七牛的空间名字
bucket_name="xxxx"
#设置要同步的文件和在七牛云存储的名字
backup_file=sys.argv[1]
backup_name=sys.argv[2]

policy = qiniu.rs.PutPolicy(bucket_name)
extra = rio.PutExtra(bucket_name)

uptoken = policy.token()
ret, err = rio.put_file(uptoken, backup_name, backup_file, extra)
if err is not None:
    sys.stderr.write('error: %s ' % err)


