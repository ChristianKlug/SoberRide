# SoberRide
Script use for Sober Ride. Sets a time and chooses names and phone numbers from a given roster and sends a message to 
given addresses containing the names and phone numbers. Also includes Slack web-hook integration.

SETUP: create a credentials.txt file with the first line being your gmail address, the second being your password, and the third being a slack webhook url. If you don't wish to use the slack webhook integration, comment out the code in sendmessage.py at the bottom that utilizes it.
Create an addresses.txt file for the addresses you want to send to with the email addressses you want and phone numbers in 1234567890@carrier.com format.
