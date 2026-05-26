from functools import reduce
import operator

# 暴力调参，参数范围2013-2024
# 如[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
source_output1_ranges = [range(10,11,1), range(10,11,1), range(10,11,1), range(10,11,1),
                            range(10,11,1), range(10,11,1), range(10,11,1), range(9,10,1),
                            range(11,12,1), range(9,10,1), range(1,2,1), range(1,2,1)]

# 如[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
source_output2_ranges = [range(5,6,1), range(5,6,1), range(5,6,1), range(5,6,1),
                            range(5,6,1), range(5,6,1), range(5,6,1), range(5,6,1),
                            range(5,6,1), range(5,6,1), range(5,6,1), range(1,6,1)]

# 如[10, 18, 20, 33, 38, 32, 32, 32, 9, 9, 11, 5]
init_bk_input1_ranges = [range(9,10,1), range(19,20,1), range(27,28,1), range(32,33,1),
                            range(39,40,1), range(33,34,1), range(31,32,1), range(31,32,1),
                            range(10,11,1), range(15,16,1), range(10,11,1), range(4,5,1)]

# 如[39, 39, 39, 40, 40, 39, 41, 41, 41, 39, 39, 39]
first_output_ranges = [range(10,11,1), range(10,11,1), range(39,40,1), range(41,42,1),
                            range(41,42,1), range(41,42,1), range(41,42,1), range(41,42,1),
                            range(41,42,1), range(19,20,1), range(1,42,10), range(10,15,1)]

# 最后补一位保护位，就不用改代码，方便； 如[1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 0]
less_34_output_ranges = [range(1,2,1), range(1,2,1), range(3,4,1), range(1,2,1),
                            range(2,3,1), range(1,2,1), range(1,2,1), range(1,2,1),
                            range(1,2,1), range(3,4,1), range(1,2,1), range(1,2,1), range(0,1,1)]

# 最后补一位保护位，就不用改代码，方便； 如[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
over_35_output_ranges = [range(1,2,1), range(1,2,1), range(1,2,1), range(1,2,1),
                            range(1,2,1), range(1,2,1), range(1,2,1), range(1,2,1),
                            range(1,2,1), range(1,2,1), range(1,2,1), range(1,2,1), range(0,1,1)]

all_combos=[]
all_combos.extend(source_output1_ranges)
all_combos.extend(source_output2_ranges)
all_combos.extend(init_bk_input1_ranges)
all_combos.extend(first_output_ranges)
all_combos.extend(less_34_output_ranges)
all_combos.extend(over_35_output_ranges)
total_combos_times = reduce(operator.mul, [len(r) for r in all_combos])