class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmail = set()

        for email in emails:
            names = email.split("@")
            localName = names[0]
            hostName = names[1]
            temp = ""

            for ch in localName:
                if ch == "+":
                    break
                if ch != ".":
                    temp += ch

            localName = temp
            currEmail = localName + "@" + hostName
            validEmail.add(currEmail)
        # print(validEmail)
        return len(validEmail)