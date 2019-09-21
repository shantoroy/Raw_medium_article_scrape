from keyword_search import Relevancy

# application code
if __name__ == "__main__":
    file_name = "ethereum-390.json"
    tag = 'ethereum'
    keyword = Relevancy(file_name, tag)
    print("Number of Relevant post is:", keyword.relevant_post(tag))
    print(keyword.list_of_most_used_words())
