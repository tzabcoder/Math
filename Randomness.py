
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# Random Number Generation -------------------------------------------------------------

# Program settings
npr.seed(100)
np.set_printoptions(precision=4)

# Generate a sequence of 10 random numbers
randSeq = npr.rand(10)
print(randSeq)

# Generate a matrix of random number of size: 5x5
randMat = npr.rand(5, 5)
print(randMat)

a = 5.0  # Lower limit
b = 10.0 # Upper limit

# Transformation of the random sequence (above) to the interval [a, b]
transformedSeq = npr.rand(10) * (b - a) + a
print(transformedSeq)

# Transformation of the random matrix (above) to the interval [a, b]
transformedMat = npr.rand(5, 5) * (b - a) + a
print(transformedMat)

# Random sampling
SAMPLE_SIZE = 500
a = [0, 25, 50, 75, 100]

rSeq1 = npr.rand(SAMPLE_SIZE, 3)        # Generate a random number matrix
rSeq2 = npr.randint(0, 10, SAMPLE_SIZE) # Generate a random integer sequence [0, 100)
rSeq3 = npr.sample(size=SAMPLE_SIZE)    # Generate a random sequence of floats on [0.0, 1.0)
rSeq4 = npr.choice(a, size=SAMPLE_SIZE) # Generate a random sample from a 1D array

# Plot the random samples
BINS = 25
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

ax1.hist(rSeq1, bins=BINS, stacked=True)
ax1.set_title('Random Number Matrix')
ax1.set_ylabel('Frequency')

ax2.hist(rSeq2, bins=BINS)
ax2.set_title('Random Integer Sequence')

ax3.hist(rSeq3, bins=BINS)
ax3.set_title('Random Float Sequence')
ax3.set_ylabel('Frequency')

ax4.hist(rSeq4, bins=BINS)
ax4.set_title('Random Sampling from Array')
plt.show()

# Distributions ------------------------------------------------------------------------
SAMPLE_SIZE = 500
BINS = 25

standardNormal = npr.standard_normal(SAMPLE_SIZE) # Create a standard normal distribution

normMean = 100
normStddev = 20
normal = npr.normal(normMean, normStddev, SAMPLE_SIZE) # Create a normal (Gaussian) distribution

degreesFreedom = 0.5
chiSquare = npr.chisquare(df=degreesFreedom, size=SAMPLE_SIZE) # Create a chi-square distribution

lambda_d = 1.0
poisson = npr.poisson(lam=lambda_d, size=SAMPLE_SIZE) # Create a poisson distribution

# Plot the distributions
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

ax1.hist(standardNormal, bins=BINS)
ax1.set_title('Standard Normal Distribution')
ax1.set_ylabel('Frequency')

ax2.hist(normal, bins=BINS)
ax2.set_title('Normal (Gaussian) Distribution')

ax3.hist(chiSquare, bins=BINS)
ax3.set_title('Chi Square Distribution')
ax3.set_ylabel('Frequency')

ax4.hist(poisson, bins=BINS)
ax4.set_title('Poisson Distribution')
plt.show()