# python program to display the user id and domain name from email address

email = input('Enter the email address : ')

# method-1
userId, domainName = email.split('@')

print('UserId :', userId)
print('Domain Name :', domainName)

# method-2
indexOfAtrate = email.find('@')

userId = email[:indexOfAtrate:]
domainName = email[indexOfAtrate+1::]

print('UserId :', userId)
print('Domain Name :', domainName)