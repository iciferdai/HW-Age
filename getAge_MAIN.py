import getAge_DATA
import getAge_LOSS
from getAge_BASE import *
from getAge_GEN import *
import itertools


def show_progress(num):
    progress=int(num*100/total_combos_times)
    print(f'\r>>>>>>>>>>>>>>>>>>>> Progress: ...{progress}%|{num}|{total_combos_times}...', end='', flush=True)


age_test = getAge_DATA.Age_Data()
age_loss = getAge_LOSS.Age_Loss(init_age_table, init_check_29_age)

count=1
for combo1 in itertools.product(*source_output1_ranges):
    for combo2 in itertools.product(*source_output2_ranges):
        for combo3 in itertools.product(*init_bk_input1_ranges):
            for combo4 in itertools.product(*first_output_ranges):
                for combo5 in itertools.product(*less_34_output_ranges):
                    for combo6 in itertools.product(*over_35_output_ranges):
                        age_test.set_parameters(
                            source_output1=list(combo1),
                            source_output2=list(combo2),
                            bk_input=np.array(combo3),
                            first_output=list(combo4),
                            less_34_output=list(combo5),
                            over_35_output=list(combo6)
                        )
                        age_test.update_input_num()
                        age_test.calculate_age()
                        tbl=age_test.get_table()
                        ck29=age_test.get_check_29()
                        age_loss.set_table_check(tbl, ck29)
                        upt, rfs = age_loss.get_sum_loss()
                        if upt:
                            print('\n=============================================================================')
                            age_loss.show_loss(False)
                            age_test.show_params()
                            print('=============================================================================')
                            age_test.show_ages()
                            print('=============================================================================')
                        elif rfs:
                            age_loss.show_loss(True)
                        age_test.reset_table()
                        show_progress(count)
                        count+=1

age_loss.show_finish()
print('Done')
exit(0)
