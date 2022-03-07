import ezgmail, os

unreadThreads = ezgmail.unread(); # List of GmailThread objects.

ezgmail.summary(unreadThreads); #Prints unread threads

resultThreads = ezgmail.search('SPAM'); #Search for keywords

ezgmail.summary(resultThreads); #prints the threads that contain keywords

print(unreadThreads[0].messages[0].sender) #prints Email of sender at index 0

for thread in resultThreads:
  for message in thread.messages:
    sender = message.sender;
    ezgmail.send(sender, 'ILLEGAL WORD DETECTED', 'OMAE WA MOU SHINDEIRU') #sends email, this is where I'm fucked
