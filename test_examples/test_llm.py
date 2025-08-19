# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Mail         : yxj2017@gmail.com
 Github       : https://github.com/MrYxJ
 Date         : 2023-08-24 11:49:08
 LastEditTime : 2023-09-03 11:38:11
 Copyright (C) 2023 mryxj. All rights reserved.
'''

from calflops import calculate_flops
from transformers import LlamaTokenizer
from transformers import LlamaForCausalLM

batch_size = 1
max_seq_length = 128
from transformers import GPT2Tokenizer, GPT2Model
model_name = "gpt2"
model = GPT2Model.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
flops, macs, params = calculate_flops(model=model,
                                      input_shape=(batch_size, max_seq_length),
                                      transformer_tokenizer=tokenizer)
print("GPT2 FLOPs:%s   MACs:%s   Params:%s \n" %(flops, macs, params))

