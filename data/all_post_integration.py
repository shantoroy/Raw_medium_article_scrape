import json
count = 0
final_json_data = []

file_name_list = ["ethereum.json", "blockchain.json", "smart-contract.json",
                      "solidity.json", "vyper.json", "ripple.json",
                      "remix.json", "metamask.json", "bitcoin.json"]
tag_list = ["ethereum", "blockchain", "smart contract", "solidity", "vyper", "ripple",
                "remix", "metamask", "bitcoin"]

for file_name, tag in zip(file_name_list, tag_list):

    json_data  = json.load(open(filename))

    for key in json_data:
    tags = key['tags']
    for item in tags: 
        if tag in item.lower():
            final_json_data.append(key)
	    count += 1

    # Output the updated file with pretty JSON                                      
open("final_all_post_data.json", "w").write(
        json.dumps(final_json_data, sort_keys=True, indent=4, separators=(',', ': '))
    )
print("The total no of post is: ", count)
