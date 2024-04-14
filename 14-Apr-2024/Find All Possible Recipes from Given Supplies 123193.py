# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[recipes[i]].append(ingredient)

        res = []
        recipe = set(recipes)
        supply = set(supplies)
        temp = {}

        def dfs(curr, visited):
            if curr in temp:
                return temp[curr]
            
            visited.add(curr)

            for ingredient in graph[curr]:
                if (ingredient not in supply and ingredient not in recipe) or ingredient in visited:
                    temp[curr] = False
                    return False

                if ingredient not in supply and not dfs(ingredient, visited):
                    temp[curr] = False
                    return False

            visited.remove(curr)
            
            temp[curr] = True
            return True
        
        for r in recipes:
            if dfs(r, set()):
                res.append(r)
        
        return res