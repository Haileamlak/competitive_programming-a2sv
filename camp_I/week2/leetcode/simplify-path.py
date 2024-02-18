class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        new_path = path.split('/')
        for folder in new_path:
            if folder == '..':
                if len(stack):
                    stack.pop()
            elif folder == '.' or folder == '':
                pass
            else:
                stack.append('/' + folder)

        if not len(stack):
            stack.append('/')
        
        return ''.join(stack)
                


            