def sort_nodes(node_list):
    safe_nodes = []
    seen = set()
    for node in node_list:
        if any(x in seen for x in node):
            seen.update(node)
            for check in safe_nodes:
                if any(x in check for x in node):
                    safe_nodes.remove(check)
            continue
        else:
            seen.update(node)
            safe_nodes.append(node)
        
    return safe_nodes


if __name__ == '__main__':
    network_nodes = [[1,2],[2,3],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24],[25,26],[27,28],[31,32],[33,34],[35,36],[37,38],[39,40],[41,42],[43,44],[45,46],[47,48],[49,50],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88],[155,156],[157,158],[175,176],[177,178],[179,180],[181,182],[183,184],[195,196],[197,198],[198, 199],[199,200],[2,4],[4,6],[6,8],[8,10],[10,12]]

    node_pairs = sort_nodes(network_nodes)

    plain = [str(x) for y in node_pairs for x in y]
    
    print(','.join(plain))

