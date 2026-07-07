class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        split_path = path.split("/")

        for part in split_path:
            if part == "" or part == " " or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)