def flames(name1: str, name2: str) -> str:
    name1 = name1.lower().replace(' ', '')
    name2 = name2.lower().replace(' ', '')
    common_chars = list(set(name1) & set(name2))
    total_chars = (len(name1) + len(name2)) - (2 * len(common_chars))
    flames_list = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    while len(flames_list) > 1:
        split_index = (total_chars % len(flames_list) - 1)
        flames_list = flames_list[split_index + 1:] + flames_list[:split_index]
    return flames_list[0]

# Input
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Output
print(f"The relationship between {name1} and {name2} is: {flames(name1, name2)}")
