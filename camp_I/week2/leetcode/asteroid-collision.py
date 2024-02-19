class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final_state = []
        for asteroid in asteroids:
            if asteroid > 0:
                final_state.append(asteroid)
            else:
                while final_state and final_state[-1] > 0 and final_state[-1] < abs(asteroid):
                    final_state.pop()
                if final_state:
                    if final_state[-1] < 0:
                        final_state.append(asteroid)
                    elif final_state[-1] == abs(asteroid):
                        final_state.pop()
                    
                else:
                    final_state.append(asteroid)
        
        return final_state