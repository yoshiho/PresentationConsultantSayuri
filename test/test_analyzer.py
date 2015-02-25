# -*- coding: utf-8 -*-

import unittest
from analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):

    def test_analyze_parts(self):
        analyze=Analyzer()
        send_words=["こんな文章だとか","このようなかんじのないぶんしょうだとか","すもももももももものうち"]
        for words in send_words:
            print (words)
            print(analyze.analyze_parts(words))
        print("\n")


    def test_analyze_parts_speed(self):
        analyze=Analyzer()
        send_words=["こんな文章だとか","このようなかんじのないぶんしょうだとか","すもももももももものうち"]
        for words in send_words:
            print (words)
            interval=10000 #10秒
            result=analyze.analyze_parts(words)
            print(analyze.analyze_parts_speed(result,interval))

    def test_analyze_connect(self):
        print("test_check_connect:")
        analyze=Analyzer()
        import random
        words=["あー","えー","あ","え","の","てｓ","@","tue"]
        words_count={}
        for word in words:
            words_count[word]=0
        send_message=""
        num=0
        while num<20:
            random_word=random.sample(words,2)
            words_count[random_word[0]]+=1
            words_count[random_word[1]]+=1
            send_message=send_message+random_word[0]+" "+random_word[1]+" "
            checked=analyze.analyze_connect(send_message)
            num+=1
            print(send_message)
            print(checked)
            for word in checked.keys():
                self.assertEqual(words_count[word],checked[word])


    def test_count_characters(self):
        analyze=Analyzer()
        send_words=["こんな文章だとか","このようなかんじのないぶんしょうだとか","すもももももももものうち"]
        for words in send_words:
            print (words)
            print(analyze.count_characters(words))
        print("\n")


    """
    def test_check_connect(self):
        print("test_check_connect:")
        speech_message=Analyzer()
        import random
        words=["あー","えー","あ","え","の","てｓ","@","tue"]
        words_count={}
        for word in words:
            words_count[word]=0
        send_message=[]
        num=0
        while num<20:
            random_word=random.sample(words,2)
            words_count[random_word[0]]+=1
            words_count[random_word[1]]+=1
            send_message.append(random_word[0])
            send_message.append(random_word[1])
            checked=speech_message.check_connect(send_message)
            num+=1
            print("".join(send_message))
            print(checked)
            for word in speech_message.get_connect_words_dictionary():
                self.assertEqual(words_count[word],checked[word])

    def test_connect_analysis(self):
        print("test_connect_analysis:")
        speech_message=Analyzer()
        send_message="あ　な　た　は　どうでしょうかあ　まあ例えばこんなメッセージがあーきたりとかえーしますよね"
        print (send_message)
        return_dictionary=speech_message.analyze_connect(send_message)
        print(return_dictionary)


    def test_count_character(self):
        print("test_count_character:")
        speech_message=Analyzer()
        import random
        words=["あ ー"," えー"," あ2","え  で  ","4の","てす","@@","て     え"]
        words_count={}
        for word in words:
            words_count[word]=0
        send_message=""
        num=0
        while num<20:
            random_word=random.sample(words,2)
            send_message=send_message+(random_word[0])+(random_word[1])
            num+=1
        counted=speech_message.count_character(send_message)
        print(send_message+":"+str(counted))
        self.assertEqual(80,counted)
        """