# Changelogs:

## [v0.1_alpha - 2024.10.15](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.1_alpha)
- Initial release.
- Added the main menu.
- Added the ability to start a new session, or continue an existing one.
- Added the ability to manage your sessions (delete, rename).

## [v0.2_alpha - 2024.10.16](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.2_alpha)
- Added the ability to see the available sessions, when you continuing a session.
- Added an "are you sure" question, when you are deleting a session.
- Added a check, that if you enter a time, it checks, if it is a workable data.
- Added breaklines, to make the instructions more clear and nice.

## [v0.3_alpha - 2024.10.17](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.3_alpha)
- The idea to import csv files, is replaced, with importing cstimer.net files. (Still WIP)
- Made it clear, that when you can type anything to do something, you can just press 'enter'. It is faster.
- If you are making a new session, it does not starts it immediately. You need to choose the 'continue session' option.
- If you create a session, it does not create a comment and P.1 segment in the save file, because it was pointless.
- Made the code more clear, but that does not affects the user experience, only developers (in a good way).

## [v0.3.1_alpha - 2024.10.17](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.3.1_alpha)
- Fixed a bug, where you couldn't continue a session you just created, because it couldn't understand the header of the saved file.

## [v0.4_alpha - 2024.10.24](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.4_alpha)
- Updated the save file format with adding a new line, that says the type of the session.
- Added the ability to choose the type of the session you want to create.
- You can now choose from 222, 333 and 444.
- Added new scrambles for 222, 333 and 444.
- Added a function, that replaces " " with "_" in the name of the session.

## [v0.5_alpha - 2024.10.26](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.5_alpha)
- Added a check, if the session you want to continue, does not exist, it will return you to the main menu.
- Fixed a bug, where it did not save the last solve, if there were empty lines in the file.
- Added the ability to view your statistics (fastest solve, latest AO5, latest AO12, latest AO100, best AO5, best AO12, best AO100).

## [v1.0 - 2024.11.10](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v1.0.0)
### We finally stepped out of alpha!
- Fixed a bug, where if you didn't choose a valid option in the menu, it didn't cleared the screen.
- Fixed a bug, where it didn't cleared the screen after you were viewing your statistics.
- Added the ability to import cstimer.net sessions.
