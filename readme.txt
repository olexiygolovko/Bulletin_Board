Task:
We need to develop an Internet resource for a fan server of one famous
MMORPG is something like a bulletin board. Users of our resource should be able to
register in it by e-mail, receiving a letter with a registration confirmation code.
After registration, they can create and edit advertisements.
Ads consist of a title and text, which may contain images, embedded videos and other content.
Users can post plain text responses to other users' advertisements.
When sending a response, the user should receive an e-mail notifying about it.
The user should also have access to a private page with responses to his ads, inside which he
can filter responses by ads, delete them and accept them (when accepting a response to a user,
the person who left the response should also receive a notification). In addition, the user must define
advertisement in one of the following categories: Tanks, Healers, DD, Merchants, Guildmasters, Questgivers, Blacksmiths, Tanners,
Potions masters, spell masters.

We would also like to be able to send newsletters to users.


Job Celery | Setting up Redis via Docker
Launch Celery with the command - celery -A bulletinboard worker -l INFO
