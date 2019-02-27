class Solution:
    def shoppingOffers(self, price: 'List[int]', special: 'List[List[int]]', needs: 'List[int]') -> int:
        
        def dot(left_needs):
            res = 0
            for i in range(len(price)):
                res += price[i] * left_needs[i]
            return res
        
        def list2str(left_needs):
            return (''.join([str(i) for i in left_needs]))

        # method 1: recursion
        def recurion_method(left_needs) -> int:
            min_cost = dot(left_needs)
            for sp in special:
                new_left_needs = [need for need in left_needs]
                for i, p in enumerate(sp[:-1]):
                    new_left_needs[i] -= p
                    if new_left_needs[i] < 0:
                        break
                else:
                    min_cost = min(min_cost, recurion_method(new_left_needs) + sp[-1])
            return min_cost
        return recurion_method(needs)

        # method 2: recursion with memo
        memo = {}
        def recurion_method_with_momo(left_needs) -> int:
            if list2str(left_needs) in memo.keys():
                return memo[list2str(left_needs)]
            min_cost = dot(left_needs)
            for sp in special:
                new_left_needs = [need for need in left_needs]
                for i, p in enumerate(sp[:-1]):
                    new_left_needs[i] -= p
                    if new_left_needs[i] < 0:
                        break
                else:
                    min_cost = min(min_cost, recurion_method(new_left_needs) + sp[-1])
            memo[list2str(left_needs)] = min_cost
            
            return memo[list2str(left_needs)]
        return recurion_method_with_momo(needs)


if __name__ == '__main__':
    sol = Solution()
    print(sol.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))

