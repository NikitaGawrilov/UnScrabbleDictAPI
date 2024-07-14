from bigtree import list_to_tree, tree_to_dataframe

lines = []
with open("validated_dict.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    while line:
        if line != '\n' and not line[0].isdigit():
            lines.append(line[:-1])
        line = f.readline()

sep_lines = ['/'.join(['^'] + list(line) + ['$']) for line in lines]
root = list_to_tree(sep_lines)

root_df = tree_to_dataframe(root)

root_df.to_pickle("small_tree.pickle")
