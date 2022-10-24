'''run evaluations on multiple models'''

import os

models_to_evaluate = [
        # 'unsupervised_2s_satb_bcbq_mf0_1',
        'unsupervised_4s_satb_bcbq_mf0_1_again',
        'unsupervised_4s_bc1song_mf0_1',
        'supervised_4s_bc1song_mf0_1',
        'supervised_4s_satb_bcbq_mf0_1'
        ]

eval_mode='default' # default evaluation
eval_mode='fast' # fast evaluation
eval_mode='robustness' # run many unique evaluations for each model, following different types of robustness tests
eval_mode='robustness_vad' # run many unique evaluations for each model, with vad error tests only



for tag in models_to_evaluate:
    
    if eval_mode=='robustness_vad' :
        for i in range(5):
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute baseline_gtf0 gtf0_strict_error_percent --vadseed {}".format(tag,i)
            print(command)
            os.system(command)
    else:
        if eval_mode=='original_paper':
            command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD'".format(tag)
    
        elif eval_mode=='default':
            command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD' --show-progress --compute all".format(tag)
        
        elif eval_mode=='fast':
            command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD' --show-progress --compute SI-SDR_mask".format(tag)

        elif eval_mode=='robustness':
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute all".format(tag)

        elif eval_mode=='robustness_vad':
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute baseline_gtf0 gtf0_strict_error_percent --vadseed 0".format(tag)


        print(command)
        os.system(command)
