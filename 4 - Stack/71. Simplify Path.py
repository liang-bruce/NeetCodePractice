class Solution:
    def simplifyPath(self, path: str) -> str:
        # using split - much faster
        stack = []

        for i in path.split("/"):
            #  if i == "/" or i == '//', it becomes '' (empty string)

            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                # skip "." or an empty string
                continue
            else:
                stack.append(i)

        res = "/" + "/".join(stack)
        return res
        
        
        # not using split, use 2 while loops to achieve split
        # dirStack = []
        # curDir = ""

        # i = 0
        # while i < len(path):
        #     while i < len(path) and path[i] != '/':
        #         curDir += path[i]
        #         i += 1
        #     if curDir:
        #         if curDir == '.':
        #             pass
        #         elif curDir == '..':
        #             if dirStack:
        #                 dirStack.pop()
        #         else:
        #             dirStack.append(curDir)
        #     # print(dirStack, curDir)
        #     curDir = "" 
        #     i += 1
        
        # return "/" + "/".join(dirStack)