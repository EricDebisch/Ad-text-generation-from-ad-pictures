# Advertisement-text-generation-from-advertisement-pictures
Short description:
Analysis of advertisement image files to generate advertisement text with transformer Pegasus
Tools in use:
YoloV5 to detect objects on images
Zero-Shot to generate a descriptive text of the image file
Transformer Pegasus to generate new text on the basis of the advertisement image analysis
BLEURT to evaluate the suitability of the generated text. 

Contributers: 1 person (EricDebisch)

Any changes will be updated in the readme.md

State of 2022-09-13 A few test scripts have been uploaded to have a prototype, how the end solution could look like.
For this, the advertisement pictures have been analyzed and the input data for the text generation by Pegasus and text evaluation by BLEURT are created, how they potentially could look like.
The results have been commented in the corresponding python scripts of the tests to document the first test results and how to proceed with the implementation.
One change could be to use the colors of the picture and objects on the picture to use as a match with training data.
This match could be evaluated to compare the uploaded picture without advertisement text to advertisement pictures with similiar features (e.g. colors match to at least 60 %, objects match at least 40 %).
The text on the matching advertisement pictures and the result of Zero-Shot would then be used by transformer Pegasus as input texts to generate a new text.
THe same advertisement text would then be used as references for the generated text by transformer Pegasus and give a final score for the generated text.
The results will then be used to evaluate, if the used tools are suitable to generate advertisement text for pictures without advertisement text.



State of 2022-08-10: The following contains the planned setup for the generation of advertisement next.
Required steps to achieve text generation (Steps will remain as a documentation of the first draft. Steps might have changed in more recent updates.):
1.  Advertisement images will be analyzed for their properties, e.g. color, color distribution, objects on the image, etc.
    This will be done with Python libraries for image analysis and tools for object detection like YoloV5 on basis of the CoCo dataset

2.  The parameters resulting from the analysis will server as training data for a neural network
    The neural network could be built with the PyTorch Framework

3.  The training data will serve as the basis for the advertisement text generation
    For this, a picture can be uploaded/processed and from the analysis a text will be generated
    The text could be generated with the transformer Pegasus

4.  The result for the text anaylsis will be checked, of the generated advertisement text is fitting for the context of the used image.
    The evaluation tool BLEURT could be able to evaluate the generated advertisement text






