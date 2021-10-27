import social_analyzer as sa
import time
import sys

def test_twtretrieve():
    input1 = "honeygrow"
    res = sa.twitter_retrieve(input1, 3)
    assert isinstance(res, list)
    assert type(res[0]["Likes"] == int)

    input2 = None
    res2 = sa.twitter_retrieve(input2, 3)
    assert res2 == []

    input3 = 250
    res3 = sa.twitter_retrieve(input1, input3)
    assert res3 == []

def test_entsentretrieve():
    input1 = dict()
    input1["Tweets"] = "test tweets"
    input1["Likes"] = 4
    input1["Time"] = time.gmtime(0)
    input1["Hashtags"] = "test hashtag"

    res1 = sa.entities_sentiments_retrieve(input1)
    assert isinstance(res1, list)
    assert type(res1[0]["Tweet Text"] == str)

    input2 = "array"
    res2 = sa.entities_sentiments_retrieve(input2)
    assert res2 == []

def test_hashtagretrieve():
    input1 = dict()
    input1["Tweets"] = "test tweets2"
    input1["Likes"] = 8
    input1["Time"] = time.gmtime(0)
    input1["Hashtags"] = "test hashtag2"

    hashtag = "test hashtag2"
    res1 = sa.txt_hashtag_retrieve(hashtag, input1)
    assert type(res1[0]) == str

    hashtag2 = "no"
    res2 = sa.txt_hashtag_retrieve(hashtag2, input1)
    assert res2 == []
