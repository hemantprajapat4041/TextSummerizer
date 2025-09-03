import os
from src.TextSummerizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.TextSummerizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert(self):
        dataset_samusm=load_from_disk(self.config.data_path)
        dataset_samusm_pt=dataset_samusm.map(self.convert_examples_to_features, batched=True)
        dataset_samusm_pt.save_to_disk(self.config.root_dir)
