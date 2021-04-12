def ping(hostname):
    import subprocess

    output = subprocess.Popen(["ping.exe","-n","1","-l","1",hostname],shell=True,stdout = subprocess.PIPE).communicate()[0]
    output=output.decode('UTF-8')
    if output.find('unreachable')!=-1:
        return 1
    else:
        return 0
ping("google.com")