class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()
        stack = []
        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append([pos, health, direction, idx])
            else:
                # direction == 'L'
                while stack and stack[-1][2] == 'R' and health > 0:
                    if stack[-1][1] < health:
                        # right robot dies
                        health -= 1
                        stack.pop()
                    elif stack[-1][1] == health:
                        # both die
                        stack.pop()
                        health = 0
                        break
                    else:
                        # left robot dies
                        stack[-1][1] -= 1
                        health = 0
                        break
                
                if health > 0:
                    stack.append([pos, health, direction, idx])
        
        # Sort back to original order
        stack.sort(key=lambda x: x[3])
        
        return [robot[1] for robot in stack]
        