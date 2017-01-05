import requests
import smtplib

def send_mail(msg):

	sender = 'splashpressmedia@gmail.com'
	receiver = 'dave.splashpress@gmail.com'
	server = smtplib.SMTP('smtp.gmail.com', 587)
	with open('keys.txt') as f:
		pwrd = f.read().strip() 
	server.starttls()
	server.ehlo()
	server.login('splashpressmedia@gmail.com', pwrd)
	#msg = 'Some links are now 404s!'
	server.sendmail(sender, receiver, msg)
	server.set_debuglevel(1)
	server.quit()


#Get the list of urls from a file 

fp = open('test_urls.txt', 'r')

#remove whitespace and filter out empty items

urls = fp.read().splitlines()

urls = filter(None, urls)


#check http response of each url in the list

dead_urls = []

for url in urls:

	r = requests.get(url)

	print url, " returns a ", r.status_code
	if r.status_code == 404:

		dead_urls.append(url)

		subject = 'Some linked pages are now 404s'

		msg_text = 'You have 404s from some links'

		msg = 'Subject: %s\n\n%s' % (subject, msg_text)

		try:
			send_mail(msg)
		except SMTPException:
			print "Unable to send mail, please try again"








		
		




