import json
import sys


def get_vertices(graph):
    # return list of verticies
    return list(graph.keys())


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        try:
            iterset = set(graph.get(vertex)) - set(path)
        except TypeError:  # URL not in allowed_domains or > depth
            continue

        for next in iterset:
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):

    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def diameter(graph):
    # calculate the diameter of the graph
    v = get_vertices(graph)
    pairs = [(v[i], v[j]) for i in range(len(v)) for j in range(i + 1, len(v))]
    smallest_paths = []
    for en, (s, e) in enumerate(pairs):
        smallest = shortest_path(graph, s, e)  # orders the list
        if smallest:
            smallest_paths.append(smallest)
    smallest_paths.sort(key=len)  # sorts the list so longest path is at the end
    diameter = len(smallest_paths[-1])

    return diameter, smallest_paths[-1]


def main():
    if len(sys.argv) != 2:
        print("usage: %s file.json " % sys.argv[0])
        sys.exit(-1)

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    graph_dict = {item['url']: item['items'] for item in data}

    print(diameter(graph_dict))


if __name__ == '__main__':
    main()