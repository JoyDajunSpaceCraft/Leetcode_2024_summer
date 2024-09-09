class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # times = [i[0]for i in customers]
        # make_time = [i[1] for i in customers]
        time_list = []

        pre_end = 0
        idx = 0
        while idx< len(customers):
            start_time = customers[idx][0]
            make_time = customers[idx][1]
            if idx ==0:
                pre_end += start_time+make_time
               
            else:
                if start_time < pre_end:
                    pre_end += make_time
                else:
                    pre_end = start_time + make_time
            # print("pre_end",pre_end)
            used_time =  pre_end - start_time
            # print("used_time",used_time)
            time_list.append(used_time)
            idx+=1
        return sum(time_list)/len(time_list)

