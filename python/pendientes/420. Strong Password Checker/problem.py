password = "ABABABABABABABABABAB1"

class Solution:
    
    def islower(self, character: str) -> bool:
        if (ord(character) > 96) & (ord(character) < 123):
            return True
        else:
            return False

    def isupper(self, character: str) -> bool:
        if (ord(character) > 64) & (ord(character) < 91):
            return True
        else:
            return False

    def isnumeric(self, character: str) -> bool:
        if (ord(character) > 47) & (ord(character) < 58):
            return True
        else:
            return False
        
    def __init__(self) -> None:
        # Types criteria
        self.count_changes_types = 0
        self.is_lower = 0
        self.is_upper = 0
        self.is_numeric = 0
        # Repetition criteria
        self.count_changes_repetition = 0
        self.count_aux = 1

    def strongPasswordChecker(self, password: str) -> int:
        length = len(password)
        length_original = len(password)

        # Special case #1
        if length < 3:
            return 6 - length

        '''Lower/Upper/Number criteria'''
        for i in password:
            if ~self.is_lower & self.islower(i):
                # Found a lower character, skip this step in the next iterations
                self.is_lower = 1
            if ~self.is_upper & self.isupper(i):
                # Found a lower character, skip this step in the next iterations
                self.is_upper = 1
            if ~self.is_numeric & self.isnumeric(i):
                # Found a lower character, skip this step in the next iterations
                self.is_numeric = 1
            if self.is_lower & self.is_upper & self.is_numeric:
                # Found already at least one type of eacher character criteria, skipping the remaining
                break

        self.count_changes_types += (1 - self.is_lower) + (1 - self.is_upper) + (1 - self.is_numeric)
        length += self.count_changes_types

        '''Repetion criteria'''
        for i in range(length_original-1):
            if (password[i] == password[i+1]):
                self.count_aux += 1
            else:
                if self.count_aux >= 3:
                    self.count_changes_repetition += self.count_aux // 3
                self.count_aux = 1

        # In case the repetition is until the end of the string
        if self.count_aux >= 3:
            self.count_changes_repetition += self.count_aux // 3

        if self.count_changes_repetition <= self.count_changes_types:
            # The changes by the types criteria are enough to resolve the repetion criteria too
            self.count_changes_repetition = 0
        else:
            self.count_changes_repetition -= self.count_changes_types
            length += self.count_changes_repetition

        '''Length criteria'''
        if length < 6:
            return 6 - length + self.count_changes_types + self.count_changes_repetition
        elif length > 20:
            return length - 20 + self.count_changes_types + self.count_changes_repetition
        else:
            return self.count_changes_types + self.count_changes_repetition

if __name__ == "__main__":
    obj = Solution()
    print(obj.strongPasswordChecker(password))

'''
class Solution:
    
    def islower(self, password: str) -> bool:
        for i in password:
            if (ord(i) < 97) | (ord(i) > 122):
                return False
        return True

    def isupper(self, password: str) -> bool:
        for i in password:
            if (ord(i) < 65) | (ord(i) > 90):
                return False
        return True

    def isnumeric(self, password: str) -> bool:
        for i in password:
            if (ord(i) < 48) | (ord(i) > 57):
                return False
        return True

    def strongPasswordChecker(self, password: str) -> int:

        length = len(password)
        count_changes = 0

        # Special case #1
        if length < 3:
            return 6 - length

        # Repetion criteria
        count_aux = 1
        for i in range(length-1):

            if (password[i] == password[i+1]):
                count_aux += 1

            else:
                if count_aux >= 3:
                    count_changes += count_aux // 3
                count_aux = 1

        if count_aux >= 3:
            count_changes += count_aux // 3

        #length -= count_changes

        # Lower/Upper/Number criteria
        if self.islower(password) | self.isupper(password) | self.isnumeric(password):
            count_changes += 1
            length += count_changes

        # Length criteria
        if length < 6:
            return 6 - length + count_changes

        elif length > 20:
            return length - 20 + count_changes
        
        else:
            return count_changes        
'''
