#WMT-2014-De-En数据集
#mT5-small
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/mT5-small-wmt2014-de-en")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/mT5-small-wmt2014-de-en")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/mT5-small-wmt2014-de-en")

#mT5-small (aligned)
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/mT5-small-wmt2014-de-en-bild-aligned")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/mT5-small-wmt2014-de-en-bild-aligned")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/mT5-small-wmt2014-de-en-bild-aligned")

#mT5-large
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="kssteven/mT5-large-wmt2014-de-en")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("kssteven/mT5-large-wmt2014-de-en")
model = AutoModelForSeq2SeqLM.from_pretrained("kssteven/mT5-large-wmt2014-de-en")