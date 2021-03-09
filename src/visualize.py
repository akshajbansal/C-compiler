import pygraphviz as pgv

def draw_ast(node):
    G = pgv.AGraph(strict=True, directed=True)
    node_list =[node]

    G.add_node(node.id, label = node.value)

    while node_list:

        top_node = node_list[0]
        node_list.pop(0)

        for nd in top_node.children:
            G.add_node(nd.id, label = nd.value)
            G.add_edge(top_node.id, nd.id)
            node_list += [nd]
    
    G.layout()
    G.layout(prog="dot")

    return G


