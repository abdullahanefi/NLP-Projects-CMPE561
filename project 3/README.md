# Assignment 3 - Relation Extraction

I used MaxEnt library to implement only the baseline algorithm.

The first 3000 sentences are used as the training set and 15 iterations are made on this training set. The remaining labeled sentences are used as test set.

## Usage

Usage : python2 baseline.py path_to_sentences path_to_labels

## Results

correct   : 969
false     : 87
accuracy  : 91.76%

## Expected Output on the given dataset

Total 3000 training events and 0 heldout events added in 0.05 s
Reducing events (cutoff is 1)...
Reduced to 1834 training events

Starting L-BFGS iterations...
Number of Predicates:  4964
Number of Outcomes:    2
Number of Parameters:  6333
Number of Corrections: 5
Tolerance:             1.000000E-05
Gaussian Penalty:      off
Optimized version
iter  eval     loglikelihood  training accuracy   heldout accuracy
==================================================================
  0      1  -6.931472E-01     58.800%        N/A
  1      2  -5.969253E-01     69.167%        N/A
  2      3  -3.387740E-01     83.467%        N/A
  3      4  -2.597741E-01     89.767%        N/A
  4      5  -2.457569E-01     89.967%        N/A
  5      6  -1.862437E-01     91.967%        N/A
  6      7  -1.562840E-01     93.233%        N/A
  7      8  -1.213146E-01     96.033%        N/A
  8      9  -8.186559E-02     97.100%        N/A
  9     10  -6.087684E-02     97.833%        N/A
 10     11  -4.891914E-02     98.467%        N/A
 11     12  -4.253133E-02     98.633%        N/A
 12     13  -3.851209E-02     98.733%        N/A
 13     14  -3.449065E-02     98.800%        N/A
 14     15  -2.769265E-02     99.133%        N/A
 15     16  -1.784638E-02     99.567%        N/A
Maximum numbers of 15 iterations reached in 0.04 seconds
Highest log-likelihood: -1.784638E-02
correct   : 969
false     : 87
accuracy  : 91.76%
