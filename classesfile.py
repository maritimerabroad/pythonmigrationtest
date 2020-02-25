class Workload():
	ip = ('192.168.0.1')
	username = ''
	password = ''
	domain = ''
	storage = []
	
class Credentials():
	username = 'testusername'
	password = 'testpassword'
	domain = 'testdomain'
	Workload.domain = domain
	Workload.password = password
	Workload.username = username
	
class Mountpoint():
	mountinfo = []
	mountinfo.append({'mountpoint': 'C:/', 'size': 107374182400})
	mountinfo.append({'mountpoint': 'D:/', 'size': 53687091200})
	for info in mountinfo:
		mountsize = info.get('size')
		mountpoint = info.get('mountpoint')
		Workload.storage.append(mountpoint)
		Workload.storage.append(mountsize)

class MigrationTarget():
	cloudtype = ("aws", "azure", "vsphere", "vcloud")
	cloudusername = Credentials.username
	cloudpassword = Credentials.password
	clouddomain = Credentials.domain
