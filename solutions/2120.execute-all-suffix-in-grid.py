class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        return_list = []
        for index in range(len(s)):
            return_list.append(self.movement(startPos,s[index:],n))
        return return_list

    def movement(self,pos,substring,n):
        movement_dict={
            "L":(0,-1),
            "R":(0,1),
            "U":(-1,0),
            "D":(1,0)
        }
        count = 0
        for chara in substring:
            mvtup=movement_dict[chara]
            return_pos = (pos[0]+mvtup[0],pos[1]+mvtup[1])
            #print(return_pos,count)
            y,x = return_pos
            if y<0 or y>n-1 or x>n-1 or x<0:
                break
            count += 1
            pos = return_pos
        return count