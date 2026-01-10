from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    

def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")
    clean_blocks_list = []
    blocks_list_stripped = list(map(lambda x: x.strip(), blocks_list))
    for i in range(0, len(blocks_list_stripped)):
        if blocks_list_stripped[i] != "":
            clean_blocks_list.append(blocks_list_stripped[i])
    return clean_blocks_list

def block_to_block_type(block):
    
    # optional, falls Windows-Zeilenumbrüche vorkommen
    block = block.replace("\r\n", "\n")

    if re.fullmatch(r"#{1,6} .*", block):
        return BlockType.HEADING

    if re.fullmatch(r"```[^\n]*\n.*?\n```", block, flags=re.DOTALL):
        return BlockType.CODE

    if re.fullmatch(r"(?:> .*(?:\n|$))+", block, flags=re.MULTILINE):
        return BlockType.QUOTE

    # Unordered list: jede Zeile beginnt mit "- "
    if re.fullmatch(r"(?:- .*(?:\n|$))+", block, flags=re.MULTILINE):
        return BlockType.UNORDERED_LIST

    # Ordered list: jede Zeile sieht aus wie "N. " ...,
    # und N muss bei 1 starten und pro Zeile +1 sein
    if re.fullmatch(r"(?:\d+\. .*(?:\n|$))+", block, flags=re.MULTILINE):
        lines = block.splitlines()

        # Nummern extrahieren und prüfen
        nums = []
        for line in lines:
            m = re.match(r"(\d+)\. ", line)
            if not m:  # sollte durch fullmatch eigentlich nie passieren
                return BlockType.PARAGRAPH
            nums.append(int(m.group(1)))

        if nums and nums[0] == 1 and nums == list(range(1, len(nums) + 1)):
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

    
    



