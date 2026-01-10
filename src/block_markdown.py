def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")
    clean_blocks_list = []
    blocks_list_stripped = list(map(lambda x: x.strip(), blocks_list))
    for i in range(0, len(blocks_list_stripped)):
        if blocks_list_stripped[i] != "":
            clean_blocks_list.append(blocks_list_stripped[i])
    return clean_blocks_list

