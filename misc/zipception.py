import zipfile

n = 3000

for i in range(3000):
	with zipfile.ZipFile(f"temp/flag{n}.zip", 'r') as zip_ref:
		zip_ref.extractall("temp")
	
	n = n - 1