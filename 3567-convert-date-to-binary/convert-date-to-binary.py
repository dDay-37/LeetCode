class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date=date.split("-")
        return str(bin(int(date[0]))[2:]) + "-" + str(bin(int(date[1]))[2:]) + "-" + str(bin(int(date[2]))[2:])
