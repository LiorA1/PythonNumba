import time
from Graph import Graph, GraphNumba


def graphs_4():

    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    graph = Graph(edges, 4)
    print(f'Graph is : {graph}')

    print("--- Python DFS ---")
    start_time = time.perf_counter_ns()
    graph.iterative_dfs(0)
    finish_time = time.perf_counter_ns()
    print(f'DFS Finished in {(finish_time - start_time) / 1_000_000} MilliSeconds')


    #start_time = time.perf_counter_ns()
    # func_jit = jit(nopython=True)(func)
    # func_jit(parameters)
    #finish_time = time.perf_counter_ns()
    #print(f'fib_numba_wrapper Finished in {(finish_time - start_time) / 1_000_000} MilliSeconds')

    print("--- Numba DFS ---")
    graph_numba = GraphNumba(edges, 4)
    start_time = time.perf_counter_ns()
    graph_numba.iterative_dfs_numba_wrapper(0)
    finish_time = time.perf_counter_ns()
    print(f'DFS Finished in {(finish_time - start_time) / 1_000_000} MilliSeconds')


def graphs_10():
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3), (1, 4), (1, 5), (4, 8), (8, 9), (5, 7), (3, 6)]
    graph = Graph(edges, 10)
    print(f'Graph is : {graph}')

    print("--- Python DFS ---")
    start_time = time.perf_counter_ns()
    graph.iterative_dfs(0)
    finish_time = time.perf_counter_ns()
    print(f'DFS Finished in {(finish_time - start_time) / 1_000_000} MilliSeconds')

    print("--- Numba DFS ---")
    graph_numba = GraphNumba(edges, 10)
    start_time = time.perf_counter_ns()
    graph_numba.iterative_dfs_numba_wrapper(0)
    finish_time = time.perf_counter_ns()
    print(f'DFS Finished in {(finish_time - start_time) / 1_000_000} MilliSeconds')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    graphs_4()

    #graphs_10()
