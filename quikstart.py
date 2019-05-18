import util as ut
import vis_util as vu

# You can change usernames as you wish or leave it None
twitter_username = "deeplearningtr"
instagram_username = "deeplearningtr"
meetup_username = "Deep-Learning-Turkiye"

tracker = ut.followertracker(twitter_username, instagram_username, meetup_username)

ut.printer(tracker)
vu.visualize(tracker)