def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest_pre = "" # longest prefix
    prefixes = ""
    len_str = len(strs)
    # handles when strs is 1
    if len_str == 1:
        return strs[0]
    num = 0
    pos = 1
    while num < len(strs[0]):
        while pos < len_str:
            try:
                if strs[0][num] == strs[pos][num]:
                    # if strs[0][num] not in longest_pre:
                    prefixes += strs[0][num]
                else:
                    return longest_pre
            except:
                pass
            pos += 1
        if len(prefixes) == len_str - 1 and len(prefixes) != 0:
                longest_pre += prefixes[0]
        prefixes = ""
        pos = 1
        num += 1
    return longest_pre