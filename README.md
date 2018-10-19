You must first install fftw3 first.
Then you must compile the source code:
'''g++ -std=c++11 -O3  src/sptree.cpp src/tsne.cpp src/nbodyfft.cpp  -o bin/fast_tsne -pthread -lfftw3 -lm'''
You can now install fast_tsne in your path:
'''python setup.py develop'''


