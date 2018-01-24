from __future__ import print_function
import smtplib
import slackweb


# Function by Ethan Harlig, from his GITHUB
def send_email(username):
    with open('addresses.txt') as f:
        plain = f.readlines()
    nums = []
    for p in plain:
        nums.append(p.rstrip('\n'))

    for addr in nums:
        server.sendmail(username, addr, msg)


persons = []
finish = 'n'
times = input('Enter hours for sober ride: ')

# Ends when prompted to confirm and "Yes" or anything not
# containing n is answered
while 'n' in finish or 'N' in finish:
    # Searches 'roster.csv' for a name matching the one entered and if found
    # questions you want the selected person, if
    # yes adds to the list, if no continues searching for name if 'done'
    # entered, moves on to confirmation of msg
    name = input('Enter a name or enter done: ')
    with open('roster.csv') as f:
        lines = f.readlines()
    if name != 'done':
        for line in lines:
            if name in line:
                print('\n' + line.rstrip('\n'))
                confirm = input('Do you want this person? : ')
                if 'y' in confirm or 'Y' in confirm:
                    persons.append(line)
                    break
    msg = "Sober Ride " + times + '\n'
    if name == 'done':
        if len(persons) > 0:
            for n in persons:
                sp = n.split(',')
                msg = msg + sp[0] + " " + sp[1] + ' ' + sp[2]
            msg = msg + "Use ridetrackr.io"
            print('\n' + msg + '\n')
            finish = input('confirm?: ')
            if 'n' in finish:
                persons = []
        else:
            print("No names added to list. Please add a name to the list.")

print('Sending: \n' + msg)

with open('credentials.txt') as f:
    content = f.readlines()

username = content[0].rstrip('\n')
password = content[1].rstrip('\n')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)

send_email(username)

server.quit()

slack = slackweb.Slack(url=content[2].rstrip('\n'))
slack.notify(text=msg, channel="#CHANGEME",                         # CHANGE ME
             username="soberride-bot", icon_emoji=":CHANGEME:")
