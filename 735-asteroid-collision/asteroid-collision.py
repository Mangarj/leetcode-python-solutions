class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for ast in asteroids:
            alive = True

            while result and ast < 0 < result[-1]:
                if abs(ast) > result[-1]:
                    result.pop()
                    continue
                elif abs(ast) == result[-1]:
                    result.pop()
                alive = False
                break

            if alive:
                result.append(ast)

        return result

        