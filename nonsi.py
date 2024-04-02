# Initializing a T5 model from the 't5-small' pre-trained checkpoint
from transformers import T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained('t5-small')
