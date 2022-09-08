# Advertisement-text-generation-from-advertisement-pictures
Short description:
Analysis of advertisement image files to generate advertisement text with transformer Pegasus

State of 2022-08-10: The following contains the planned setup for the generation of advertisement next.
Any changes will be updated in the readme.md

Contributers: 1 person (EricDebisch)

Required steps to achieve text generation:
1.  Advertisement images will be analyzed for their properties, e.g. color, color distribution, objects on the image, etc.
    This will be done with Python libraries for image analysis and tools for object detection like YoloV5 on basis of the CoCo dataset

2.  The parameters resulting from the analysis will server as training data for a neural network
    The neural network could be built with the PyTorch Framework

3.  The training data will serve as the basis for the advertisement text generation
    For this, a picture can be uploaded/processed and from the analysis a text will be generated
    The text could be generated with the transformer Pegasus

4.  The result for the text anaylsis will be checked, of the generated advertisement text is fitting for the context of the used image.
    The evaluation tool BLEURT could be able to evaluate the generated advertisement text
