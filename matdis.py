import sys
import os
# ==============================================================================
# KELAS NODE: Merepresentasikan File atau Folder
# ==============================================================================
# Setiap item di dalam sistem file kita, baik itu file atau folder adalah sebuah 'Node' atau simpul dalam struktur pohon.
class Node:
    def __init__(self,name, is_directory=False):
        """
        inisialisasi untuk kelas Node.
        """
        self.name = name
        self.is_directory = is_directory
        self.parent = None # Pointer ke induknya, akan diatur saat ditambahkan
        self.children = {} if self.is_directory else None  # Jika ini adalah direktori, ia bisa punya anak.
    def __repr__(self):
        """ 
        Representasi string untuk mempermudah debugging
        """
        return f"Node('{self.name}', dir={self.is_directory})"


# ==============================================================================
# KELAS FILESYSTEM: Mengelola Keseluruhan Pohon Sistem File
# ==============================================================================
# Kelas ini bertindak sebagai 'otak' yang mengelola semua operasi seperti membuat folder/file, mencari file, dll.
class FileSystem:
    def __init__(self):
        """
        inisialisasi untuk kelas FileSystem.
        membuat direktori root '/' saat pertama kali dibuat.
        """
        self.root = Node("/", is_directory=True)
        self.current_directory = self.root  # Awalnya, kita berada di root
    def mkdir(self, name):
        if name in self.current_directory.children:
            print(f"Error: '{name}' sudah ada.")
            return
        new_node = Node(name, is_directory=True)
        new_node.parent = self.current_directory
        self.current_directory.children[name] = new_node
    def touch(self, name):
        """
        membuat file baru di dalam direktori saat ini.
        """
        if name in self.current_directory.children:
            print(f"Error: '{name}' sudah ada.")
            return
        new_node = Node(name, is_directory=False)
        new_node.parent = self.current_directory
        self.current_directory.children[name] = new_node
        print(f"File '{name}' berhasil dibuat di '{self.current_directory.name}'.")


        print(f"Direktori '{name}' berhasil dibuat di '{self.current_directory.name}'.")
    def ls(self):
        """
        Menampilkan daftar file dan direktori di dalam direktori saat ini.
        """
        for name, node in self.current_directory.children.items():
            if node.is_directory:
                print(f"📁 {name}/")
            else:
                print(f"📄 {name}")
    def cd(self, name):
        """Berpindah ke direktori yang ditentukan (logika diperbaiki)."""
        if name == ".":
            # Tidak melakukan apa-apa, tetap di direktori saat ini
            return
        elif name == "..":
            if self.current_directory.parent is not None:
                self.current_directory = self.current_directory.parent
        elif name in self.current_directory.children and self.current_directory.children[name].is_directory:
            self.current_directory = self.current_directory.children[name]
        else:
            print(f"Error: Direktori '{name}' tidak ditemukan.")
    
    def _get_full_path(self, node):
        """
        Mendapatkan path lengkap dari node ke root.
        """
        if node == self.root:
            return "/"
        
        parts = []
        current_node = node
        while current_node != self.root:
            parts.append(current_node.name)
            current_node = current_node.parent
        return "/" + "/".join(reversed(parts))
        
    def _dfs(self, current_node, target_name,found_paths):
        """
        Fungsi rekursif untuk melakukan DFS pada pohon file.
        """
        for name, node in current_node.children.items():
            # Jika nama cocok dengan target, catat path lengkapnya
            if node.name == target_name:
                found_paths.append(self._get_full_path(node))
            # Jika node adalah direktori, lanjutkan pencarian di dalamnya
            if node.is_directory:
                self._dfs(node, target_name, found_paths)

    def find(self, target_name):
        """
        Mencari file atau folder dengan nama tertentu di seluruh sistem file menggunakan algoritma Depth-First Search (DFS), dimulai dari root.
        """
        print(f"Mencari '{target_name}'...")
        found_paths = []
        self._dfs(self.root, target_name, found_paths)
        
        if not found_paths:
            print(f"'{target_name}' tidak ditemukan.")
        else:
            print("Hasil pencarian:")
            for path in found_paths:
                print(path)

if __name__ == "__main__":
    """
    Inisiasi awal
    """
    fs = FileSystem()
    fs.mkdir("home")
    fs.cd("home")
    fs.touch("file1.txt")
    fs.ls()
    fs.mkdir("user")
    fs.cd("user")
    fs.touch("file2.txt")
    fs.ls()
    fs.cd("..")  # Kembali ke direktori home
    fs.ls()  # Menampilkan isi direktori home
    fs.find('file2.txt') 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Memulai interaksi dengan pengguna
    user_input = input(f"{fs._get_full_path(fs.current_directory)} > ")
    while user_input.lower() != "exit":
        parts = user_input.split()
        command = parts[0].lower()
        
        if command == "mkdir" and len(parts) > 1:
            fs.mkdir(parts[1])
        elif command == "touch" and len(parts) > 1:
            fs.touch(parts[1])
        elif command == "ls":
            fs.ls()
        elif command == "cd" and len(parts) > 1:
            fs.cd(parts[1])
        elif command == "find" and len(parts) > 1:
            fs.find(parts[1])
        else:
            print("Perintah tidak dikenali.")
        user_input = input(f"{fs._get_full_path(fs.current_directory)} > ")
    


