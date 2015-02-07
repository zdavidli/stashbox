import os
import pickle
import dropbox

def saveObject(obj, filename):
	with open(filename, 'w+') as output:
		pickle.dump(obj,output,-1)

def saveSimple(var, filename):
	with open(filename, 'w+') as output:
		output.write(var)

def loadSimple(var, filename):
	try: 		
		with open(filename, 'r+') as input:
			return output.read
	except IOError:
		print "File does not exist yet"



def loadObject(filename):
	#will this correctly load the object?
	try: 		
		with open(filename, 'r+') as input:
			return pickle.load(input)
	except IOError:
		print "File does not exist yet"



def saveToDropbox(obj, uploadPath):
	f = open(obj, 'rb')
	response = client.put_file(uploadPath, f)
	print response

def setupAuthentication():
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





def main():
	authenticated = False;
	authenticated = loadObject("saveAuth.p")
	print authenticated
	if (not authenticated):
		setupAuthentication()
		authentication = True;
		saveObject(authenticated, "saveAuth.p")
	stringToSave = "Helloooo"
	saveToDropbox(stringToSave, "/StashDropArchive")


if __name__ == '__main__':
	main()

