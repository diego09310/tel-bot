# tel-bot
A bot implementation using python and the telegram.ext library. The bot provides information about the computer where is installed and allows some interaction. The bot is protected to only respond to my user ID.

## Commands
**/start** Responds with a greeting (always the same).
**/ip** Returns the public IP address of the server.
**/add_torrent + [torrent_link]** Adds the torrent passed.

When the user ID is not from the owner, returns always the same message ("Sorry, this is a private bot") and logs the id, name and last name of the user.

## Configuration
In order for the bot to work, the file config.txt has to exist and contain:
[bot token]
[allowed user id]
[*ip\_address\_of\_transmission\_server* *port\_of\_transmission\_server* *username* *password*]

## Log
The bot is configured with logs which go to stderr and also keeps record of unallowed users trying to communicate with the bot in the file unauthorized.log.

## TODO

Restruct and clean the code

####More functionalities:
-add_torrent in two messages
-search_torrent (search films or tv shows and add the torrent)
-status of the server
-more?
