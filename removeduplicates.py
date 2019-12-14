import os,sys,re;

def checkext(f):
	def g():
		if len(sys.argv)<3:
			print("Enter atleast one extension..")
			if len(sys.argv)<2:
				print("Enter Directory..")
			return
		
		f()
	return g

def regex(str):
	if not str:
		return None
	return re.match(r'.+\(\d+\).*',str)

def stripNum(str):
	if not str:
		return None
	start=re.search(r'\(\d+\).*',str)
	return str if not start else str[:start.start()]
		
@checkext
def main():
	duplicates=[]
	for file in os.listdir(sys.argv[1]):
		for extension in sys.argv[2:]:
			if file.endswith("."+extension):
				str=file.rsplit(".",1)[0]
				if regex(str):
					print(str)
					str=stripNum(str).strip()
					print(str)
				if str in duplicates:
					check=input(f"Enter y to delete {str}\n").lower()
					if check in ('y','yes'):
						sys.argv[1]=sys.argv[1].strip("/")
						os.remove(sys.argv[1]+"/"+file)
						# os.rename(file,sys.argv[1]+"/"+stripNum(str)+"."+extension)
				else:
					duplicates.append(str)
	print("Removed duplicates\n")

if __name__ == '__main__':
	main()