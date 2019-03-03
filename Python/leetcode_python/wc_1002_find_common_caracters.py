class Solution:
    def commonChars(self, A):
        all_codings = []
        for l in A:
            coding = [0 for _ in range(256)]
            for c in l:
                coding[ord(c)] += 1
            all_codings.append(coding)


        temp1 = [[idx for idx in range(256) if l[idx] != 0] for l in all_codings]
        temp2 = [set(l) for l in temp1]


        intersect_ = temp2[0]
        for t in temp2:
            intersect_ = intersect_.intersection(t)

        result = []
        for c in intersect_:
            min_ = float('inf')
            for l in all_codings:
                min_ = min(min_, l[c])
            for i in range(min_):
                result.append(chr(c))
        return result
