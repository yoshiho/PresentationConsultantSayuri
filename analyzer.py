#coding: UTF-8
from collections import Counter
import MeCab

class Analyzer(object):

    BAD_WORDS=["あー", "えー", "あ", "え"]
    keys=["名詞", "動詞", "形容詞", "副詞", "助詞", "接続詞", "助動詞", "連体詞", "感動詞"]
    def __init__(self):
        pass

    def analyze(self, message):
        result = {}
        text = message["message"]
        sentence = message["sentenceCount"]
        interval = message["interval"]
        result["characters"]=self.count_characters(text)
        result["speed"] = self.analyze_speed(text, interval)
        result["sentenceSpeed"]=sentence/interval*1000
        result["parts"]=self.analyze_parts(text)
        result["parts_speed"]=self.analyze_parts_speed(result["parts"],interval)

        return result

    def analyze_parts(self,speech):
        tagger = MeCab.Tagger('mecabrc')
        node = tagger.parseToNode(speech)

        parts={}
        for key in self.keys:
            parts[key]=0
        while node:
            pos = node.feature.split(",")[0]
            if (pos in parts):
                parts[pos]+=1
            node = node.next
        return parts

    def analyze_parts_speed(self,parts,interval):
        speed={}
        for key in self.keys:
            speed[key]=parts[key]/interval*1000
        return speed

    def analyze_connect(self, text):
        tagger = MeCab.Tagger("-Owakati")
        analyzed = tagger.parse(text)
        splitted = analyzed.split()

        counter = Counter()
        for word in splitted:
            if word in self.BAD_WORDS:
                counter[word] += 1

        return counter

    def analyze_speed(self, text, interval):
        word_count = self.count_characters(text)
        return word_count / interval * 1000 # per second

    def count_characters(self, text):
      tagger=MeCab.Tagger("-Oyomi")
      analyzed=tagger.parse(text)
      analyzed=analyzed.replace(" ","")
      counted = len(analyzed)
      return counted - 1
