import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def visualize(tracker):
    websites = ('Twitter', 'Instagram', 'Meetup')
    y_pos = np.arange(len(websites))
    followers = [tracker.twitter(),tracker.instagram(),tracker.meetup()]
    plt.bar(y_pos, followers, align='center', alpha=0.5)
    plt.xticks(y_pos, websites)
    plt.ylabel('Followers')
    plt.title('Social Media')
    plt.show()