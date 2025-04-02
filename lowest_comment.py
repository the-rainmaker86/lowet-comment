import praw
from script import reddit 

# Get your own Redditor instance.
me = reddit.redditor("junior_dos_nachos")

# Retrieve your comments; you might limit this if you have many.
my_comments = list(me.comments.controversial(limit=None))
print(len(my_comments))

# Sort comments by score (ascending order).
lowest_comments = sorted(my_comments, key=lambda comment: comment.score)

# Print out the 10 lowest-rated comments.
page = 10
for comment in list(reversed(lowest_comments[:10])):
    print(f"#{page}")
    print(f"Score: {comment.score} | {comment.body}")
    print("\n")
    page -= 1
