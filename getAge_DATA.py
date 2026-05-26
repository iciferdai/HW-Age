from getAge_BASE import *
import copy

class Age_Data:
    def __init__(self):
        self.age_table = copy.deepcopy(init_age_table)
        self.source_output1 = init_source_output1
        self.source_output2 = init_source_output2
        self.check_29_age = init_check_29_age
        self.input_num_list = init_input_num_list
        self.bk_input1 = init_bk_input1
        self.bk_input2 = init_bk_input2
        self.ss_input1 = init_ss_input1
        self.ss_input2 = init_ss_input2
        self.first_output = init_first_output
        self.less_34_output = init_less_34_output
        self.over_35_output = init_over_35_output
        self.over_41_output = init_over_41_output
        self.over_46_output = init_over_46_output
        self.diff1 = np.diff(check_l30_num)
        self.diff2 = np.diff(check_m30_num)
        self.diff3 = np.diff(check_m50_num)
        self.transfer_num = None
        self.input_num = None


    def reset_table(self):
        self.age_table = copy.deepcopy(init_age_table)


    def set_parameters(self, source_output1=None, source_output2=None, bk_input=None, first_output=None,
                       less_34_output=None, over_35_output=None, over_41_output=None, over_46_output=None):
        if source_output1 is not None: self.source_output1 = source_output1
        if source_output2 is not None: self.source_output2 = source_output2
        if bk_input is not None:
            self.bk_input1 = bk_input
            self.bk_input2 = bk_input // 2
            self.ss_input1 = (100 - self.bk_input1 - self.bk_input2) * 2 // 3
            self.ss_input2 = 100 - self.bk_input1 - self.bk_input2 - self.ss_input1
        if first_output is not None: self.first_output = first_output
        if less_34_output is not None: self.less_34_output = less_34_output
        if over_35_output is not None: self.over_35_output = over_35_output
        if over_41_output is not None: self.over_41_output = over_41_output
        if over_46_output is not None: self.over_46_output = over_46_output


    def update_input_num(self):
        leave1 = (check_l30_num * self.source_output1 * 0.01).astype(int)
        leave2 = (check_m30_num * self.source_output2 * 0.01).astype(int)
        self.transfer_num = self.diff2 + self.diff3 + leave2[:11]
        self.input_num = self.diff1 + self.transfer_num + leave1[:11]
        self.check_29_age = np.append(self.transfer_num, 9000)
        self.input_num_list = np.insert(self.input_num, 0, 10000)


    def deal_year_input(self, year):
        num = self.input_num_list[year]
        bk_num1 = int(num * self.bk_input1[year] * 0.01 * (1 - (self.first_output[year] * 0.01)))
        bk_num2 = int(num * self.bk_input2[year] * 0.01 * (1 - (self.first_output[year] * 0.01)))
        ss_num1 = int(num * self.ss_input1[year] * 0.01 * (1 - (self.first_output[year] * 0.01)))
        ss_num2 = int(num * self.ss_input2[year] * 0.01 * (1 - (self.first_output[year] * 0.01)))
        self.age_table[AGE_22][year] += bk_num1
        self.age_table[AGE_23][year] += bk_num2
        self.age_table[AGE_25][year] += ss_num1
        self.age_table[AGE_26][year] += ss_num2


    def deal_year_2_next(self, year):
        base_num = 0
        for k in range(AGE_35):
            self.age_table[k][year+1] += base_num
            leave_num = int(self.age_table[k][year] * self.less_34_output[year+1] * 0.01)
            base_num = self.age_table[k][year] - leave_num

        for k in range(AGE_35, AGE_41):
            self.age_table[k][year+1] += base_num
            leave_num = int(self.age_table[k][year] * self.over_35_output[year+1] * 0.01)
            base_num = self.age_table[k][year] - leave_num

        for k in range(AGE_41, AGE_46):
            self.age_table[k][year+1] += base_num
            leave_num = int(self.age_table[k][year] * self.over_41_output[year+1] * 0.01)
            base_num = self.age_table[k][year] - leave_num

        self.age_table[AGE_46][year+1] += base_num


    def calculate_age(self):
        for year in range(len(self.input_num_list)):
            self.deal_year_input(year)
            self.deal_year_2_next(year)


    def get_table(self):
        return self.age_table


    def get_check_29(self):
        return self.check_29_age


    def show_ages(self):
        np.set_printoptions(linewidth=1000)
        print(self.age_table)


    def show_params(self):
        print(f'source_output1: {self.source_output1}')
        print(f'source_output2: {self.source_output2}')
        print(f'bk_input1: {self.bk_input1}')
        print(f'bk_input2: {self.bk_input2}')
        print(f'ss_input1: {self.ss_input1}')
        print(f'ss_input2: {self.ss_input2}')
        print(f'first_output: {self.first_output}')
        print(f'less_34_output: {self.less_34_output}')
        print(f'over_35_output: {self.over_35_output}')
        print(f'over_41_output: {self.over_41_output}')
        print(f'over_46_output: {self.over_46_output}')
        print(f'check_29_age: {self.check_29_age}')
        print(f'input_num_list: {self.input_num_list}')