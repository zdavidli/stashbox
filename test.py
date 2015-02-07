import os
import pickle
import dropbox

global client

def saveObject(obj, filename):
	with open(filename, 'w+') as output:
		pickle.dump(obj,output,-1)

"""def saveSimple(var, filename):
	with open(filename, 'w+') as output:
		output.seek(0)
		output.write(var)
		print var

def loadSimple(filename):
	try: 		
		with open(filename, 'r+') as input:
			return input.read()
	except IOError:
		print "File does not exist yet" 
		"""



def loadObject(filename):
	#will this correctly load the object?
	try: 		
		with open(filename, 'r+') as input:
			return pickle.load(input)
	except IOError:
		print "File does not exist yet"



def saveToDropbox(obj, uploadPath):
	with open(obj, 'rb') as f:
		response = client.put_file(uploadPath, f)
	print response



def setupAuthentication():
	global client
	app_key = "9s7hb21rv9udehc"
	app_secret = "d0grqcxuf3rnzmb"

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	# Have the user sign in and authorize this token
	authorize_url = flow.start()
	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()
	access_token, user_id = flow.finish(code)
	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()
	saveObject(client, "saveClient.p")

def main():
	authenticated = False;
	authenticated = loadObject("saveAuth.p")
	print authenticated
	if (not (authenticated == True)):
		setupAuthentication()
		authenticated = True;
		saveObject(authenticated, "saveAuth.p")

	saveToDropbox("saveFile.txt", "/StashDropArchive")



if __name__ == '__main__':
	main()

