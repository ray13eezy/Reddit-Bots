import praw
import time
import datetime

r = praw.Reddit('EbonyMawderator')

# Get time
currentSysTime = time.localtime()
now = datetime.datetime.now(datetime.timezone.utc).timestamp()
today = datetime.date.today()

log_post = (r.submission('93ypq5'))

subbie = 'ThanosDidNothingWrong' # sub to operate in
moderators = r.subreddit(subbie).moderator()
print("Bot for r/{}. Removes dead submissions.".format(subbie))
print("Checking submissions...")

def TDNWRemoveBot():
    removal_reason = """Hear me and rejoice, /u/{}. Your post has had the privilege of being removed by the Great Titan. 
                        You may think this is suffering, no. It is salvation. The universal scales tip toward balance because of your sacrifice. 
                        Smile. For even in death, you have become Children of Thanos.

 ---

  **RULE 2:**

  - 2b. All posts 1 day old and below 50 karma will be automatically removed.
    
---

*If you feel this was removed in error or are unsure about why this was removed then please [modmail us.](https://www.reddit.com/message/compose?to=%2Fr%2Fthanosdidnothingwrong)*


^^If ^^you ^^are ^^not ^^able ^^to ^^read ^^the ^^removal ^^reason ^^please ^^use ^^desktop ^^mode.
    """
    removed = []
    for submission in r.subreddit(subbie).new(limit=1000): #get 1000 unapproved posts
        if submission.score < 50: # only if they are < 50
            age = now - submission.created_utc
            if age > int(86400): # if it's over 24 hours
                if submission not in removed:
                  if submission.author not in moderators:
                    submission.mod.remove() # remove submission
                    removal_comment = submission.reply(removal_reason.format(submission.author))
                    removal_comment.mod.distinguish(how='yes', sticky=True)
                    removed.append(submission.permalink)
                    print("reddit.com" + submission.permalink)
                    
    print(len(removed))
    removals = '\n\n * '.join(removed)
    r.subreddit(subbie).message('[Notification] Automated Removals - {}'.format(today),
    """
The following submissions were removed for being low-effort after receiving less than 50 upvotes in twenty-four hours.

 * {}

Total removals: {}
    """.format(removals, len(removed)))


TDNWRemoveBot()
