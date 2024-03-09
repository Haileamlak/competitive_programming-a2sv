class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def can_heat(radius):
            heater_pointer = house_pointer = 0
            while heater_pointer < len(heaters) and house_pointer < len(houses): 
                if houses[house_pointer] <= heaters[heater_pointer]:
                    if heaters[heater_pointer] - radius > houses[house_pointer]:
                        return False
                    house_pointer += 1

                elif houses[house_pointer] > heaters[heater_pointer]:
                    if heaters[heater_pointer] + radius < houses[house_pointer]:
                        heater_pointer += 1
                    else:
                        house_pointer += 1
                else:
                    return False
            
            return house_pointer == len(houses) 

        minimum = 0
        maximum = pow(10, 9)             
        while minimum < maximum:
            mid = minimum + (maximum - minimum) // 2
            if can_heat(mid):
                maximum = mid
            else:
                minimum = mid + 1
        
        return minimum