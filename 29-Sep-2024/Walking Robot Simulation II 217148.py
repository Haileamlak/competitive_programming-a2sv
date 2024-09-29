# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

# class Robot:

#     def __init__(self, width: int, height: int):
#         # 0 - East, 1 - North, 2 - West, 3 - South
#         self.direction = "East"
#         self.pos = [0, 0]
#         self.width = width - 1
#         self.height = height - 1

#     def step(self, num: int) -> None:
#         while num > 0:
#             if self.direction ==  "East":
#                 newPos = self.pos[0] + num
#                 print("here")
#                 if newPos <= self.width:
#                     self.pos[0] = newPos
#                     num = 0
#                     print("here1")
                
#                 # elif newPos == self.width:
#                 #     self.pos[0] = newPos
#                 #     self.direction = "North"

#                 else:
#                     self.pos[0] = self.width
#                     self.direction = "North"
#                     print("here2")

#                     num = newPos - self.width
#                     # self.step(num)

#             elif self.direction ==  "West":
#                 newPos = self.pos[0] - num

#                 if newPos >= 0:
#                     self.pos[0] = newPos
#                     num = 0
                
#                 # elif newPos == 0:
#                 #     self.pos[0] = newPos
#                 #     self.direction = "South"

#                 else:
#                     self.pos[0] = 0
#                     self.direction = "South"

#                     num = 0 - newPos
#                     # self.step(num)

#             elif self.direction ==  "North":
#                 newPos = self.pos[1] + num

#                 if newPos <= self.height:
#                     self.pos[1] = newPos
#                     num = 0
                
#                 # elif newPos == self.height:
#                 #     self.pos[1] = newPos
#                 #     self.direction = "West"

#                 else:
#                     self.pos[1] = self.height
#                     self.direction = "West"

#                     num = newPos - self.height
#                     # self.step(num)

#             elif self.direction ==  "South":
#                 newPos = self.pos[1] - num

#                 if newPos >= 0:
#                     self.pos[1] = newPos
#                     num = 0
                
#                 # elif newPos == 0:
#                 #     self.pos[1] = newPos
#                 #     self.direction = "East"

#                 else:
#                     self.pos[1] = 0
#                     self.direction = "East"

#                     num = 0 - newPos
#                     # self.step(num)
            
#             num %= 2 * (self.width + self.height)

#     def getPos(self) -> List[int]:
#         return self.pos

#     def getDir(self) -> str:
#         return self.direction


# # Your Robot object will be instantiated and called as such:
# # obj = Robot(width, height)
# # obj.step(num)
# # param_2 = obj.getPos()
# # param_3 = obj.getDir()

class Robot:
    def __init__(self, w, h):
        self.i = 0
        self.pos = [[0, 0, 'South']] + [[i, 0, 'East'] for i in range(1, w)] + \
            [[w - 1, i, 'North'] for i in range(1, h)] + \
            [[i, h - 1, 'West'] for i in range(w - 2, -1, -1)] +\
            [[0, i, 'South'] for i in range(h - 2, 0, -1)]

    def step(self, x):
        self.i += x

    def getPos(self):
        return self.pos[self.i % len(self.pos)][:2]

    def getDir(self):
        return self.pos[self.i % len(self.pos)][2] if self.i else 'East'