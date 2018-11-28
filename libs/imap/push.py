import imaplib
 

def push_enable(server, port, email, password):
	try:
		connection = imaplib.IMAP4_SSL(server, port)
		connection.login(email, password)
		metadata = '(/private/vendor/vendor.dovecot/http-notify "user=' + email + '")'
		connection._simple_command('SETMETADATA', "", metadata)
		connection.logout()
		return 1
	except Exception as err:
		print('imap failed: ', err) 
		return 0

		
def push_disable(server, port, email, password):
	try:
		connection = imaplib.IMAP4_SSL(server, port)
		connection.login(email, password)
		metadata = '(/private/vendor/vendor.dovecot/http-notify NIL)'
		connection._simple_command('SETMETADATA', "", metadata)
		connection.logout()
		return 1
	except Exception as err:
		print('imap failed: ', err) 
		return 0

		 