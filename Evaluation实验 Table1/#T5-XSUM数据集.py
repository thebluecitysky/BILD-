#XSUM数据集
#T5-small
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/T5-small-xsum")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/T5-small-xsum")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/T5-small-xsum")


#T5-small (aligned)
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/T5-small-xsum-bild-aligned")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/T5-small-xsum-bild-aligned")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/T5-small-xsum-bild-aligned")


#T5-large
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/T5-large-xsum")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/T5-large-xsum")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/T5-large-xsum")


