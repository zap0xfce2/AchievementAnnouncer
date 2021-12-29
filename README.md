# AchievementAnnouncer

A pythonscript in docker for tweeting your retroachievements from emulationstation on your raspberry pi!

## Usage

### What you need

- obviously a Twitter account & api keys (http://twitter.com)
- an retroachievements account & api keys (https://retroachievements.org)
- docker installed and ready to run

### Getting started

- clone the repo
- add a folder in AchievementAnnouncer and name it "config"
- in this "config" folder add the following files and contens:
  - Long.url - The long url to your retroachievemnts profile
  - Short.url - The short url to your retroachievemnts profile
  - RetroAchievements.key - Your retroachievments api key
  - RetroAchievements.user - Your retroachievments username
  - TwitterAccess.token - Your twitter access token
  - TwitterAccessToken.secret - Your twitter access token secret
  - TwitterApi.key - Your twitter api key
  - TwitterApiSecret.key - Your twitter api secret
- run "build-and-run.sh" to build your dockerimage

## Changelog

- **1.0**: Initial release.
