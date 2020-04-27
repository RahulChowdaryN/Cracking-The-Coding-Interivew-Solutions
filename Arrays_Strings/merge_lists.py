def merge2lists(l1, l2):
    # print("merging")
    i = 0
    j = 0
    response = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            response.append(l1[i])
            i += 1
        # elif l1[i] > l2[j]:
        #     response.append(l2[j])
        #     j += 1
        else:
            response.append(l2[j])
            # i += 1
            j += 1

    if i < len(l1):
        response += l1
    if j < len(l2):
        response += l2

    return response

print(merge2lists([57, 81],[ 63, 7]))