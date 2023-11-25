from huggingface_hub import hf_hub_download
import re
from PIL import Image

from transformers import NougatProcessor, VisionEncoderDecoderModel
from datasets import load_dataset
import torch


# https://huggingface.co/docs/transformers/main/en/model_doc/nougat

def nougatProcessor_base(filepath):
    processor = NougatProcessor.from_pretrained("Xenova/nougat-small")
    model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-small")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    # prepare PDF image for the model filepath = hf_hub_download(repo_id="hf-internal-testing/fixtures_docvqa",
    # filename="nougat_paper.png", repo_type="dataset")
    default_filepath = ""
    image = Image.open(filepath)
    pixel_values = processor(image, return_tensors="pt").pixel_values

    # generate transcription (here we only generate 30 tokens)
    # TODO  token 的生成的数量
    outputs = model.generate(
        pixel_values.to(device),
        min_length=1,
        max_new_tokens=100,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
    )

    sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    sequence = processor.post_process_generation(sequence, fix_markdown=False)
    # note: we're using repr here such for the sake of printing the \n characters, feel free to just print the sequence
    print(repr(sequence))