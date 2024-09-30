from typing import List

s = "aa"
p = ".*"

class Solution:
    def find(self, p:str, char:str) -> List[int]:
        find_list = []

        for i in range(len(p)):
            if p[i] == char:
                find_list.append(i)

        return find_list

    def isMatch(self, s: str, p: str) -> bool:

        if p.find("*") == -1:

            if p.find(".") == -1:
                return p is s

            # There is a .
            else:

                find_list = self.find(p, ".")
                if len(find_list) == 1:
                    if p[]
                for i in range(len(find_list)-1):
                    repeated = p[find_list[i],find_list[i+1]]



        # There is a *
        else:

            if p.find(".") == -1:

                for i in self.find(p, "*"):
                    repeated = p[i-1]

                    if repeated not in s:
                        return False

                return True

            # There is a .
            else:
                return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.isMatch(s, p))
