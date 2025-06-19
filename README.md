# Virtual File System Using N-ary Trees with Depth-First Search Traversal Algorithm

## Overview

This project implements a **Virtual File System (VFS)** using N-ary tree data structures with a Depth-First Search (DFS) traversal algorithm. The system simulates basic file system operations such as creating directories, creating files, navigating between directories, listing contents, and searching files/directories across the entire file system hierarchy.

## Author

**Kurt Mikhael Purba** - Student ID: 13524065

## Project Description

The Virtual File System is designed to demonstrate the practical application of tree data structures and graph traversal algorithms in computer science. This implementation uses:

- **N-ary Trees**: Each directory node can have multiple children (files and subdirectories)
- **Depth-First Search (DFS)**: Used for searching files and directories across the entire file system
- **Object-Oriented Design**: Clean separation of concerns with Node and FileSystem classes

## Features

### Core Functionality
- ✅ **Directory Creation** (`mkdir`): Create new directories
- ✅ **File Creation** (`touch`): Create new files
- ✅ **Navigation** (`cd`): Move between directories
- ✅ **Listing** (`ls`): Display contents of current directory
- ✅ **Search** (`find`): Search for files/directories using DFS algorithm
- ✅ **Interactive Shell**: Command-line interface for user interaction

### Special Navigation
- Support for relative navigation (`cd ..` for parent directory)
- Support for current directory reference (`cd .`)
- Full path display in command prompt

## Technical Architecture

### Node Class
```python
class Node:
    - name: str              # Name of file/directory
    - is_directory: bool     # Flag to distinguish files from directories
    - parent: Node           # Reference to parent node
    - children: dict         # Dictionary of child nodes (for directories only)
```

### FileSystem Class
```python
class FileSystem:
    - root: Node             # Root directory node
    - current_directory: Node # Current working directory
```

### Key Algorithms

#### Depth-First Search Implementation
The `find` operation uses recursive DFS to traverse the entire file system tree:
1. Start from root directory
2. For each node, check if name matches target
3. If node is directory, recursively search its children
4. Collect all matching paths and display results

## Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Application

```bash
# Clone or download the project
cd Virtual-File-System-Using-N-ary-Trees-with-a-Depth-First-Search-Traversal-Algorithm

# Run the application
python matdis.py
```

### Available Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| `mkdir` | `mkdir <directory_name>` | Create a new directory |
| `touch` | `touch <file_name>` | Create a new file |
| `ls` | `ls` | List contents of current directory |
| `cd` | `cd <directory_name>` | Change to specified directory |
| `cd ..` | `cd ..` | Move to parent directory |
| `find` | `find <name>` | Search for file/directory using DFS |
| `exit` | `exit` | Exit the application |

### Example Usage Session

```bash
/ > mkdir documents
Direktori 'documents' berhasil dibuat di '/'.

/ > cd documents
/documents > touch readme.txt
File 'readme.txt' berhasil dibuat di 'documents'.

/documents > mkdir projects
Direktori 'projects' berhasil dibuat di 'documents'.

/documents > ls
📁 projects/
📄 readme.txt

/documents > cd projects
/documents/projects > touch main.py
File 'main.py' berhasil dibuat di 'projects'.

/documents/projects > cd /
/ > find readme.txt
Mencari 'readme.txt'...
Hasil pencarian:
/documents/readme.txt
```

## Project Structure

```
Virtual-File-System-Using-N-ary-Trees-with-a-Depth-First-Search-Traversal-Algorithm/
├── matdis.py                    # Main implementation file
├── README.md                    # Project documentation
└── 13524065-Kurt Mikhael Purba-Design and Analysis of a Virtual File System Using N-ary Trees with a Depth-First Search Traversal Algorithm.pdf
```

## Algorithm Complexity

### Time Complexity
- **mkdir, touch, cd, ls**: O(1) - Constant time operations
- **find**: O(n) - Linear time where n is the total number of nodes in the file system

### Space Complexity
- **Overall**: O(n) - Linear space where n is the total number of files and directories
- **DFS Search**: O(h) - Space complexity of O(h) where h is the height of the tree (recursion stack)

## Key Design Decisions

1. **N-ary Tree Structure**: Each directory node maintains a dictionary of children, allowing efficient O(1) lookup and unlimited child nodes
2. **Parent Pointers**: Each node maintains a reference to its parent for efficient upward navigation
3. **Path Reconstruction**: Full paths are constructed by traversing parent pointers up to the root
4. **DFS Implementation**: Recursive implementation for intuitive tree traversal and search functionality

## Educational Value

This project demonstrates several important computer science concepts:

- **Data Structures**: N-ary trees, dictionaries, recursive structures
- **Algorithms**: Depth-First Search, tree traversal, path finding
- **Software Design**: Object-oriented programming, separation of concerns
- **System Programming**: File system simulation, command-line interfaces

## Future Enhancements

Potential improvements for extended functionality:

- [ ] File content storage and editing
- [ ] File permissions and access control
- [ ] Absolute path navigation
- [ ] File size and metadata tracking
- [ ] Breadth-First Search option for find command
- [ ] Export/import file system structure
- [ ] Tab completion for commands
- [ ] Wildcard pattern matching in search

## Contributing

This is an educational project. Contributions and suggestions for improvements are welcome.

## License

This project is created for educational purposes as part of coursework in discrete mathematics and data structures.

---

**Note**: This implementation is a simulation of a file system and does not interact with the actual operating system's file system. All operations are performed in memory and data is not persisted between sessions.
