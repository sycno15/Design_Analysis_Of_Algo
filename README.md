# Graph Coloring Algorithm

## Description

This implementation of the **Graph Coloring** algorithm assigns colors to vertices of a graph such that no two adjacent vertices share the same color. It uses a **backtracking approach** to explore possible color assignments and ensures valid coloring using a limited number of colors.

## How It Works

1. **Graph Representation:** The graph is represented as an adjacency matrix.
2. **Backtracking:** The algorithm attempts to color each vertex recursively.
3. **Validation:** Before assigning a color, it checks that adjacent vertices are not already assigned the same color.
4. **Result:** If all vertices can be colored, the solution is displayed; otherwise, it reports that no valid coloring exists.

## Example Graphs

Two demo graphs are used:

* **Graph 1:** A sparse graph with 6 vertices and selective edges.
* **Graph 2:** A dense (complete) graph with 5 vertices.

## Example Output

```
For Graph 1:
Vertex 1 ---> Color 1
Vertex 2 ---> Color 2
Vertex 3 ---> Color 3
Vertex 4 ---> Color 1
Vertex 5 ---> Color 2
Vertex 6 ---> Color 3

For Graph 2:
No solution exists with 3 colors.
```

## Usage

1. Navigate to the folder:

```bash
cd Graph-Coloring
```

2. Run the script:

```bash
python graphColoring.py
```

3. The program prints the color assigned to each vertex (if possible).

## Complexity

* **Time Complexity:** O(m^V), where V is the number of vertices and m is the number of colors.
* **Space Complexity:** O(V) for storing color assignments.

## Applications

* Scheduling problems
* Register allocation in compilers
* Map coloring
* Frequency assignment in wireless networks

## Contributing

Contributions are welcome! You can:

* Improve algorithm efficiency
* Add additional test graphs
* Extend the implementation with heuristics

Please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License.
