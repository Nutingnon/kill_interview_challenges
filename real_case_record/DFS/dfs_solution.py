# 面试官你好，我在去公司的路上想了一下用DFS的方法。代码要简洁一些。请您过目，谢谢！


def solve(nums):
    
    def moveUp(curr_pos, visited):
        if curr_pos[0] == 0:
            return False
        elif nums[curr_pos[0]-1][curr_pos[1]] > nums[curr_pos[0]][curr_pos[1]] and (curr_pos[0]-1, curr_pos[1]) not in visited:
            return True
        else:
            return False
    def moveDown(curr_pos, visited):
        if curr_pos[0] == len(nums)-1:
            return False
        elif nums[curr_pos[0]+1][curr_pos[1]] > nums[curr_pos[0]][curr_pos[1]] and (curr_pos[0]+1, curr_pos[1]) not in visited:
            return True
        else:
            return False
    def moveLeft(curr_pos, visited):
        if curr_pos[1] == 0:
            return False
        elif nums[curr_pos[0]][curr_pos[1]-1] > nums[curr_pos[0]][curr_pos[1]] and (curr_pos[0], curr_pos[1]-1) not in visited:
            return True
        else:
            return False
    def moveRight(curr_pos, visited):
        if curr_pos[1] == len(nums[0])-1:
            return False
        elif nums[curr_pos[0]][curr_pos[1]+1] > nums[curr_pos[0]][curr_pos[1]] and (curr_pos[0], curr_pos[1]+1) not in visited:
            return True
        else:
            return False
        
    def dfs(nums, path):
        print("path is", path, "answer is", answer)
        pos = path[-1]
        if (not moveLeft(pos, path)) and (not moveUp(pos,path)) and (not moveDown(pos,path)) and (not moveRight(pos, path)):
            print("arrive final", len(path), len(answer))
            if len(path) > answer[0]:
                answer[0]= len(path)
                answer[1] = path
            return
        
        if len(path) == 1 and pos in visited_elements:
            return
        
        if moveLeft(pos, path):
            visited_elements.add((pos[0], pos[1]-1))
            dfs(nums, path + [(pos[0], pos[1]-1)])

            
        if moveRight(pos, path):
            visited_elements.add((pos[0], pos[1]+1))
            dfs(nums, path+[(pos[0], pos[1]+1)])
            
        if moveUp(pos, path):
            visited_elements.add((pos[0]-1, pos[1]))
            dfs(nums, path+[(pos[0]-1, pos[1])])
            
        if moveDown(pos, path):
            visited_elements.add((pos[0]+1, pos[1]))
            dfs(nums, path+[(pos[0]+1, pos[1])])
        
        
    answer = [0, []]
    visited_elements = set()
    
        
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            # 以这些点为起点
                dfs(nums, [(i,j)])
                
    
    return answer[0]
            
    
