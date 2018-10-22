You must first install FFTW first.

Download URL: http://www.fftw.org/download.html
Installation instructions: http://www.fftw.org/fftw3_doc/Installation-on-Unix.html

You can then compile FIt-SNE source code:
```g++ -std=c++11 -O3  src/sptree.cpp src/tsne.cpp src/nbodyfft.cpp  -o bin/fast_tsne -pthread -lfftw3 -lm```

It can now be installed:
```python setup.py develop```


