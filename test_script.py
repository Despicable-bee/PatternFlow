"""
    FILENAME: test_script.py
    DESCRIPTION: Using the pre-trained generator sourced from one of our
            network pickles, Generates an image of a brain
    AUTHOR: Harry Nowakowski.
"""

import torch
import torchvision
import sys
import pickle
import matplotlib.pyplot as plt

# Load in the pickle containing our trained model
brainsFile = open('network-snapshot-000362.pkl', 'rb')

# Get the generator out (We can also get the discriminator out if we want to).
Generator = pickle.load(brainsFile)['G_ema'].cuda()

# Generate a random number in the range of the latent vector
# The latent vector controls the output of the generator.
z = torch.randn([1, Generator.z_dim]).cuda()

img = Generator(z, None).cpu()

# Extract the X and Y axis pixels from the NCWH image format.
# Since everything was greyscale to begin with, and we're only generating 
# a single image, the first two parameters don't matter.
plt.imshow(img[0,0,:,:])
plt.savefig('example_brain_output.png', )