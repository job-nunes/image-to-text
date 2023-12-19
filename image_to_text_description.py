from transformers import pipeline,BitsAndBytesConfig
import torch

class Transformers_image():
    '''PARA FAZER COM O LLAVA BASTA TROCAR AS LINHAS QUE ESTÃO COMENTADAS EM CADA FUNÇÃO.
    ELE DEMANDA MAIS PODER COMPUPTACIONAL'''
    def __init__(self) -> None:
        # self.quantization_config = BitsAndBytesConfig(
        #                                 load_in_4bit=True,
        #                                 bnb_4bit_compute_dtype=torch.float16
        #                             )
        #self.captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
        #self.pipe = pipeline("image-to-text", model="llava-hf/llava-1.5-7b-hf", model_kwargs={"quantization_config": self.quantization_config})
        self.captioner  = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

    def description_image(self,image):
        #max_new_tokens = 200
        #prompt = "USER: <image>\ndescribe the image to me and points of attention\nASSISTANT:"
        #outputs = self.pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": max_new_tokens})
        #return outputs[0]['generated_text']
        return self.captioner(image)[0]['generated_text']
