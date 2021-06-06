import json


def main():
    print('\nFirst test:')
    test_alghorithm_with_data_file('first')
    print('\nSecond test:')
    test_alghorithm_with_data_file('second')
    print('\nThird test:')
    test_alghorithm_with_data_file('third')
    print('\nPiano test:')
    test_alghorithm_with_data_file('piano')


def print_lowest_way(graph: dict, parents: dict, costs: dict):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    dir = parents['finish']
    path = []
    path.append("finish")
    while dir in parents:
        path.append(dir)
        dir = parents[dir]
    path.append("start")
    path.reverse()

    print('The lowest cost is ' + str(costs['finish']))
    print('The lowest cost path is "' + ' - '.join(path) + '"')


def find_lowest_cost_node(costs: dict, processed: dict):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def test_alghorithm_with_data_str(input):
    jsonGraph = json.loads(input)

    graph = {}
    parents = {}
    infinity = float('inf')
    costs = {}

    for cur_node in jsonGraph:
        cur_node_id = cur_node["id"]
        graph[cur_node_id] = {}

        directions = cur_node["directions"]
        if directions is not None:
            for direction in directions:
                direction_id = direction["id"]
                if direction_id not in costs:
                    costs[direction_id] = infinity
                directtion_weight = direction["weight"]
                graph[cur_node_id][direction_id] = directtion_weight
                if direction_id not in parents:
                    if cur_node_id == 'start':
                        parents[direction_id] = cur_node_id
                        costs[direction_id] = directtion_weight
                    else:
                        parents[direction_id] = None

    parents['finish'] = None
    costs['finish'] = infinity

    print_lowest_way(graph, parents, costs)


def test_alghorithm_with_data_file(test_file_name: str):
    with open("dijkstras/test_data/" + test_file_name + ".json", 'r') as read_file:
        json_data = read_file.read()
    test_alghorithm_with_data_str(json_data)


main()
