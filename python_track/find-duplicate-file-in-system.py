class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_to_path = {} # example - {"efgh": ["root/a/2.txt","root/c/d/4.txt","root/4.txt"]}

        for path in paths:
            directory_files = path.split(' ')
            directory = directory_files[0]
            for i in range(1, len(directory_files)):
                file1 = directory_files[i]
                index = file1.index('(')
                text = file1[index + 1:-1]
                file_to_path[text] = file_to_path.get(text, []) + [directory + '/' + file1[:index]]
            
        res = []
        for paths in file_to_path.values():
            if len(paths) >= 2:
                res.append(paths)
            
        return res