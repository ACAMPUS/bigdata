import re

from streamparse.bolt import Bolt


class SentenceSplitterBolt(Bolt):
    outputs = ['word', 'num']  # 由于emit发出的是两个，所以这里应该有两个，否则报错

    def process(self, tup):
        sentence = tup.values[0]  # extract the sentence
        sentence = re.sub(r"[,.;!\?]", "", sentence)  # get rid of punctuation
        words = [word.strip() for word in sentence.split(" ") if word.strip()]
        if not words:
            # no words to process in the sentence, fail the tuple
            self.fail(tup)
            return

        for word in words:
            self.emit((word, 1))

        # tuple acknowledgement is handled automatically