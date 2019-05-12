import itertools
import time

from streamparse.spout import Spout


class SentenceSpout(Spout):
    outputs = ['sentence']

    def initialize(self, stormconf, context):
        self.sentences = [
            'I am tom i am a genius',
        ]
        self.sentences = itertools.cycle(self.sentences)

    def next_tuple(self):
        sentence = next(self.sentences)
        self.emit([sentence])
        time.sleep(0.5)

    def ack(self, tup_id):
        print('a tuple is processed properly')  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        print('a tuple fails to process')  # if a tuple fails to process, do nothing