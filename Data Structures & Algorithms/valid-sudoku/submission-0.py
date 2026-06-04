class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        frec_r = {}
        frec_c = []
        frec_w = defaultdict(dict)
        for v in board:
            frec_c.append(defaultdict(dict))
        h = 1
        for i, r in enumerate(board):
            for j, n in enumerate(r):
                if n == '.':
                    continue
                frec_r[n] = frec_r.get(n, 0) + 1
                frec_c[j][n] = frec_c[j][n] + 1 if frec_c[j][n] else 1
                print(frec_w)
                if not frec_w[(i//3, j//3)]:
                    frec_w[(i//3, j//3)] = set()
                if n in frec_w[(i//3, j//3)]:
                    return False
                else:
                    frec_w[(i//3, j//3)].add(n)
            for k in frec_r:
                if frec_r[k] > 1:
                    return False
            frec_r = {}

        for c in frec_c:
            dict_c = dict(c)
            for k in dict_c:
                if dict_c[k] > 1:
                    return False

        return True
            