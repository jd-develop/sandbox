#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Generic-purpose StackOverFlowAI."""
import random

sentences = [
        "Could you provide more context please?",
        "Don’t use that, it is deprecated.",
        "Who really needs to do that?",
        "Please provide screenshots of your problem.",
        "This question is duplicated.",
        "This is the first answer on Google!",
        "You could read the documentation.",
        "There is a russian blog talking about this problem, you could have read it before asking!"
]

while True:
    question = input("What’s your question? ")
    if question == "exit": break
    print(random.choice(sentences))

