class Solution(object):
    def displayTable(self, orders):
        foods =  ["Table"] + sorted(list({order[2] for order in orders}))
        tables = sorted(list(set(order[1] for order in orders)), key=lambda x:int(x))
        colMap = {val:i for i,val in enumerate(foods)}
        rowMap = {val:i+1 for i,val in enumerate(tables)}
        res = [foods]+[[table]+["0"]*(len(foods)-1) for i,table in enumerate(tables)]
        for _,table,food in orders:
            cur = res[rowMap[table]][colMap[food]]
            res[rowMap[table]][colMap[food]] = str(int(cur)+1)
        return res
