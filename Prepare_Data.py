import pandas as pd
import numpy as np

TWEET_DATA = pd.read_csv("question_philoit.csv", usecols=["id", "content"])
TWEET_DATA.columns = ["id", "content"]

TWEET_DATA.head()
