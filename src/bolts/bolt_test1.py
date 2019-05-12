import re

from streamparse.bolt import Bolt


data = {}

class SentenceCountBolt(Bolt):
    # 这里不需要再发现下一级
    def process(self, tup):
        word = tup.values[0]  # extract the sentence
        num = tup.values[1]
        if not word:
            # no words to process in the sentence, fail the tuple
            self.fail(tup)
            return
        if word in data:
            count = data.get(word)
            data[word] = count + num
        else:
            data[word] = num
        self.logger.info(
            "[word]: {}\t[count]: {}\t[pid={}]".format(word, data[word], self.pid)
        )

        # tuple acknowledgement is handled automatically