import heapq


def calculate_h_index(citations):
    h_index_array = list()
    paper_citation_map = []
    h_index = 0
    for i in citations:
        if i > h_index:
            heapq.heappush(paper_citation_map, i)
        while paper_citation_map and paper_citation_map[0] <= h_index:
            heapq.heappop(paper_citation_map)
        if len(paper_citation_map) >= h_index + 1:
            h_index += 1
        h_index_array.append(str(h_index))
    return h_index_array


for i in range(int(input())):
    n_papers = int(input())
    n_citations = [int(k) for k in input().split(" ")]
    print("Case #{}: {}".format(i + 1, " ".join(calculate_h_index(n_citations))))
