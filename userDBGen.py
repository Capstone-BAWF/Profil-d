from generateDB import *

collection_U = db.collection_user

user_tweets = []

#lesvivants
if(len(sys.argv) > 1):
    username = str(sys.argv[1])
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(10):
        user_tweets.append(tweet)

#get_user_tweets(user_tweets)

userfile = open("csvs/user.csv","wb")
write_to_file(userfile,user_tweets)
userfile.close()

userfile = open("csvs/user.csv","r+")

data = pd.read_csv(userfile, quoting=csv.QUOTE_NONE)
data_json = json.loads(data.to_json(orient = 'records'))

collection_U.remove()
collection_U.insert(data_json)

userfile.close()
