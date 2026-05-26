from getAge_BASE import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Age_Loss:
    def __init__(self, table, check_29):
        self.age_table = table
        self.check_29_age = check_29
        self.min_age_loss = 30000
        self.min_num_loss = 30000
        self.sum_loss = 60000
        self.loss_age_list = []
        self.loss_num_list = []
        self.loss_sum_list = []
        self.allow_raise = 1.05
        self.update_limit = 1000
        self.count = 0
        plt.ion()
        _, self.ax = plt.subplots()
        self.ax.set_xlabel('Iteration')
        self.ax.set_ylabel('Loss')
        self.ax.set_title('Loss over Iteration')


    def set_table_check(self, table, check_29):
        self.age_table = table
        self.check_29_age = check_29


    def get_age29_loss(self):
        check_29_2021 = self.check_29_age[YEAR_2021]
        check_29_2022 = self.check_29_age[YEAR_2022]
        check_29_2023 = self.check_29_age[YEAR_2023]
        age_29_2021 = self.age_table[AGE_29][YEAR_2021]
        age_29_2022 = self.age_table[AGE_29][YEAR_2022]
        age_29_2023 = self.age_table[AGE_29][YEAR_2023]
        loss_29 = ((((check_29_2021 - age_29_2021) * 100 / check_29_2021) ** 2) +
                   (((check_29_2022 - age_29_2022) * 100 / check_29_2022) ** 2) +
                   (((check_29_2023 - age_29_2023) * 100 / check_29_2023) ** 2))
        return loss_29


    def get_l30_loss(self):
        check_l30_2021 = check_l30_num[YEAR_2021]
        check_l30_2022 = check_l30_num[YEAR_2022]
        check_l30_2023 = check_l30_num[YEAR_2023]
        num_l30_2021 = np.sum(self.age_table[AGE_22:AGE_30, YEAR_2021])
        num_l30_2022 = np.sum(self.age_table[AGE_22:AGE_30, YEAR_2022])
        num_l30_2023 = np.sum(self.age_table[AGE_22:AGE_30, YEAR_2023])
        loss_l30 = ((((num_l30_2021 - check_l30_2021) * 100 / check_l30_2021) ** 2) +
                   (((num_l30_2022 - check_l30_2022) * 100 / check_l30_2022) ** 2) +
                   (((num_l30_2023 - check_l30_2023) * 100 / check_l30_2023) ** 2))
        return loss_l30


    def get_sum_loss(self):
        is_update = False
        loss_age = self.get_age29_loss()
        loss_num = self.get_l30_loss()
        sum_loss = loss_age + loss_age

        if sum_loss < self.sum_loss:
            is_update = True
        elif (loss_age < self.min_age_loss) & (loss_num < self.min_num_loss * self.allow_raise):
            is_update = True
        elif (loss_age < self.min_age_loss * self.allow_raise) & (loss_num < self.min_num_loss):
            is_update = True
        else:
            self.count += 1

        if is_update:
            self.sum_loss = sum_loss
            self.min_age_loss = loss_age
            self.min_num_loss = loss_num
            self.loss_age_list.append(loss_age)
            self.loss_num_list.append(loss_num)
            self.loss_sum_list.append(sum_loss)

        return is_update, self.count>=self.update_limit


    def show_loss(self, only_fresh=True):
        self.count = 0
        if only_fresh:
            self.ax.legend()
            plt.pause(0.01)  # 更新用
            return
        self.ax.clear()
        self.ax.plot(self.loss_age_list, label='Loss_age')
        self.ax.plot(self.loss_num_list, label='Loss_num')
        self.ax.plot(self.loss_sum_list, label='Loss_SUM')
        print(f'Loss :{self.sum_loss}|{self.min_age_loss}|{self.min_num_loss}')
        self.ax.legend()
        plt.pause(0.1)


    def show_finish(self):
        print('\nAll Finished, please close this window')
        plt.ioff()
        plt.show()