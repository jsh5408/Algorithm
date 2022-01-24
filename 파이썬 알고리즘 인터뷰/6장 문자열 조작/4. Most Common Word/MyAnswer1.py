class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.lower()
        p = paragraph.split()
        
        for i in range(len(banned)):
            while banned[i] in p:
                p.remove(banned[i])
        
        dic = collections.defaultdict(int)
        for w in p:
            dic[w] += 1
        
        for k, v in dic.items():
            if v == max(dic.values()):
                return k