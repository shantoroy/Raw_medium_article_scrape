import json
import re
import operator
import string


# Class to append value in a dictionary
class MyDictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


class Relevancy(object):
    def __init__(self, file_name, tag):
        self.tag = tag
        self.file_name = file_name
        with open(self.file_name, "r") as f:
            self.data = json.load(f)

    # Python3 code to pre-processing the string
    # Intending to remove all punctuation and common words
    def pre_process(self, str):
        # removing punctuation ---> using string module
        translator = str.maketrans('', '', string.punctuation)
        str = str.translate(translator)

        # converting all into lower cases
        str = str.lower()

        # removing prep, conj, articles ---> using re module
        str = re.sub('(\s+)(a|an|and|the|this|that|these|those|i|would|could|should)(\s+)', ' ', str)
        str = re.sub('(\s+)(to|for|from|in|into|under|with|within|below|up|down|of|on)(\s+)', ' ', str)
        str = re.sub('(\s+)(are|may|by|as|we|or|it|be|which|the|when|make|no|set|your|its|it\'s)(\s+)', ' ', str)
        str = re.sub('(\s+)(if|any|used|all|has|have|new|data|at|code|node|state|-|they|our)(\s+)', ' ', str)
        str = re.sub('(\s+)(you|must|every|each|not|what|one|then|way|so|will|also|is|can)(\s+)', ' ', str)
        str = re.sub('(\s+)(their|was|more|other|use|do|need|my|some|get|out|many|had|here|over)(\s+)', ' ', str)
        return str

    # Python3 code to find frequency of each word
    # function for calculating the frequency
    def freq(self, str):
        str = self.pre_process(str)

        # break the string into list of words
        str_list = str.split()

        # gives set of unique words
        unique_words = set(str_list)
        frequency = MyDictionary()
        for word in unique_words:
            frequency.add(word, str_list.count(word))

        # sort by value (downwards) ---> using operator module
        sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

        # collect first 10 items in dictionary
        # first_few_items = {k: sorted_freq[k] for k in list(sorted_freq)[:10]}
        # btw, sorted_freq is a list
        return sorted_freq[0:20]  # , len(sorted_freq)

    # merge two lists toether without appending same word
    # if same word found, increases count
    def merge_two_lists(self, a, b):
        new_list = {}
        for pair in a + b:
            key, value = pair
            new_list[key] = new_list.get(key, 0) + value
        new_list = [[key, value] for key, value in new_list.items()]
        return new_list

    # convert a tuple into a list
    def tuple_to_list(self, listname):
        a = []
        for i in range(0, len(listname)):
            a.append(list(listname[i]))
        return a

    # For sorting a list of lists using 2nd item
    def second_item(self, item):
        return item[1]

    # for getting a list of words for a particular tag
    def list_of_most_used_words(self):
        freq_list = []
        for key in self.data:
            if self.tag in key['title'].lower():
                str = key['content']
                freq_list = self.merge_two_lists(freq_list, self.tuple_to_list(self.freq(str)))

        freq_list.sort(key=self.second_item, reverse=True)
        return freq_list

    # Return number of Relevant posts
    def relevant_post(self):
        relevant = 0
        for key in self.data:
            if self.tag in key['title'].lower():
                relevant += 1
        return relevant
