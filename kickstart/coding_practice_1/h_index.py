import datetime

def h_index(citations):
    h_index_array = list()
    paper_citation_map = dict()
    h_index = 0
    if len(citations) % 2 != 0:
        paper_citation_map[citations[len(citations) / 2]] = 1
    for i in range(int(len(citations) / 2)):
        first_elem = citations[i]
        last_elem = citations[0-i-1]
        if first_elem in paper_citation_map and h_index <= i:
            paper_citation_map[first_elem] = paper_citation_map[first_elem] + 1
        else:
            paper_citation_map[first_elem] = 1
        if last_elem in paper_citation_map and h_index <= i:
            paper_citation_map[last_elem] = paper_citation_map[last_elem] + 1
        else:
            paper_citation_map[last_elem] = 1
        paper_citation_map_copy = dict()
        count_citations = 0
        for k in paper_citation_map:
            if k > h_index:
                count_citations += paper_citation_map[k]
                paper_citation_map_copy[k] = paper_citation_map[k]
        paper_citation_map = paper_citation_map_copy
        if count_citations > h_index:
            h_index += 1
        h_index_array.append(str(h_index))
    return h_index_array


for i in range(int(input())):
    n_papers = int(input())
    n_citations = [int(k) for k in input().split(" ")]
    start_time = datetime.datetime.now()
    print("Case #{}: {}".format(i + 1, " ".join(h_index(n_citations))))
    time_diff = (datetime.datetime.now() - start_time)
    executtion_time = time_diff.total_seconds()
    print(executtion_time)
