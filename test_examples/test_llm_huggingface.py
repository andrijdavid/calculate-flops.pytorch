# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

# '''
#  Description  :
#  Version      : 1.0
#  Author       : MrYXJ
#  Mail         : yxj2017@gmail.com
#  Github       : https://github.com/MrYxJ
#  Date         : 2023-09-12 16:51:53
#  LastEditTime : 2023-09-13 16:03:07
#  Copyright (C) 2023 mryxj. All rights reserved.
# '''

# from calflops import calculate_flops_hf

# batch_size = 1
# max_seq_length = 128
# # model_name = "baichuan-inc/Baichuan-13B-Chat"
# # flops, macs, params = calculate_flops_hf(model_name=model_name, input_shape=(batch_size, max_seq_length))
# # print("%s FLOPs:%s  MACs:%s  Params:%s \n" %(model_name, flops, macs, params))


# model_name = "gpt2"
# flops, macs, params, print_results = calculate_flops_hf(model_name=model_name,
#                                                         input_shape=(batch_size, max_seq_length),
#                                                         forward_mode="forward",
#                                                         output_as_string=True,
#                                                         output_precision=2,
#                                                         output_unit='G',
#                                                         print_results=True,
#                                                         print_detailed=True,
#                                                         )

# print(flops, macs, params)
# print(print_results)
