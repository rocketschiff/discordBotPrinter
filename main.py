
import time
import os

from dotenv import load_dotenv
from github import Github

load_dotenv()
github = Github(os.getenv('GITHUB_TOKEN'))
repository = github.get_user().get_repo('discordBotPrinter')
sleepTime = int(os.getenv('sleepTime'))

previousIp = ' '
while True:
    stream = os.popen('hostname -I')
    localIp = stream.readlines()[0].strip()
    if previousIp != localIp:
        previousIp = localIp
        contents = repository.get_contents("printerip.txt")
        repository.update_file('printerip.txt', 'Octopi Python script updated printer ip', localIp, contents.sha)
        print(f"Updated printer ip to {localIp}")
    time.sleep(sleepTime)
