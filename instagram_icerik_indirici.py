# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:59:58 2022

@author: yunus
"""

from instaloader import Instaloader, Profile

L = Instaloader()
#PROFILE = "artificialintelligencefacts"

PROFILE = ['learn.machinelearning','machine.learning.memes','machinelearningknowledge','mlearning.ai']

for i in PROFILE:
    profile = Profile.from_username(L.context, i)
    
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)
    
    print(posts_sorted_by_likes)
    for post in posts_sorted_by_likes:
    
        #if post.is_video:
        L.download_post(post, i)
    
