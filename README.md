## s4484282 StyleGAN2 OASIS brain generative model

![brain teaser](https://github.com/Despicable-bee/PatternFlow/blob/s4484282_branch/example_brain_output.png)

A generative model built using Nvidia's StyleGAN2 - ADA implementation in 
PyTorch.

The code was implemented almost entirely in Google Colab, which you can find
a link to [here](https://github.com/Despicable-bee/PatternFlow/blob/s4484282_branch/StyleGAN2_ADA.ipynb)

The latest network snapshot that was used to generate the above brain image is [here](https://drive.google.com/file/d/13OisU2n5B6a5U4najs3ZWPwyvWGXOLEy/view?usp=sharing)

Training was done using Google Colab, which for $13/month, gives you access to a nice shiny Nvidia Tesla P100 GPU (which speeds things up really nicely)

The first 10 epochs produced the following image

![early brains](https://github.com/Despicable-bee/PatternFlow/blob/s4484282_branch/fakes000040.png)

With the generative model improving with various epochs

![later brains](https://github.com/Despicable-bee/PatternFlow/blob/s4484282_branch/fakes000056.png)

With the final brains looking like this

![final](https://github.com/Despicable-bee/PatternFlow/blob/s4484282_branch/fakes000362.png)


