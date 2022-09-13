#The script is an example from HuggingFace.
#Source URL: https://huggingface.co/docs/transformers/model_doc/pegasus

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

import torch

#Example text, how the data could be modeled in order to be used to generate text.

src_text = [
    #The example would be for travel advertisement pictures. The first sentence is an example of a description with Zero-Shot
    #""" Sun on the ocean at the beach. 699pp. With a price like this, you'll be floating on air. The wings of china. The dreams of the world. Land your dream. Air China. Entire world. Free with every van. Forget winter. Escape to the sun. Dream bigger. Virgin holiday Sale. Boarding pass. Fly high with Turkey"""
    #Output result was "Book now:" A suitable text for a travel advertisement picture. Longer sentences appear to be suitable for Pegasus to generate appropriate advertisement text for an image.

    #The example would be for perfume advertisement pictures. The first sentence is an example of a description with Zero-Shot
    """ Women in black suit sitting on a couch. Aqua di gio. A perfume from Giorgio Armani. Acqua di parma. Colonia. Chanel No. 5. Libre Yves Saint Lauren. The new eau du parfum intense. Jadore. Infinitele woman. Dior. Chloe. Boss. Moschino Toy 2. Eau de parfum. Alien. Mugler. Linterdit Givenchy. Sauvage. Dior. Obession Men. Calvin Klein. Le femme prada. The scent of hermes girls. Twilly. Hermes perfumes. My Burberry """
    #Output result was: "All images are copyrighted"". This message seems to come up, if the sentences are only one to two words. This happened in 3 tests with one word sentences.
]

model_name = "google/pegasus-xsum"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = PegasusTokenizer.from_pretrained(model_name)

model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

batch = tokenizer(src_text, truncation=True, padding="longest", return_tensors="pt").to(device)

translated = model.generate(**batch)

tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text[0])

