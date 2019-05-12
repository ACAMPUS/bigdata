from streamparse import Grouping, Topology

from bolts.bolt_test import SentenceSplitterBolt
from bolts.bolt_test1 import SentenceCountBolt
from spouts.spout_test import SentenceSpout


class WordCount(Topology):
    """组装topo结构"""
    word_spout = SentenceSpout.spec()
    split_bolt = SentenceSplitterBolt.spec(inputs={word_spout: Grouping.fields("sentence")}, par=2)
    count_bolt = SentenceCountBolt.spec(inputs={split_bolt: Grouping.fields('word', 'num')}, par=2)
