# Youtube video
  - [Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)](https://www.youtube.com/watch?v=w8yWXqWQYmU) by [Samson Zhang](https://www.youtube.com/@SamsonZhangTheSalmon)

# Kaggle notebook
  - [Simple MNIST NN from scratch (numpy, no TF/Keras)](https://www.kaggle.com/code/wwsalmon/simple-mnist-nn-from-scratch-numpy-no-tf-keras)

# Create conda evironment
```bash
conda create -n nn python=3.10
```

# Activate conda environment
```bash
conda activate nn
```

# Init poetry project
```bash
poetry init --no-interaction
```

# Add poetry dependencies
```bash
poetry add numpy pandas matplotlib
```

# Download kaggle data
```bash
kaggle competitions download -c digit-recognizer
```

# Install mypy
```bash
poetry add mypy
```

# Github warning
```bash
(nn) ┌──(klx㉿kali)-[~/build-neural-network-samson-zhang] (main)
└─$ git remote add origin git@github.com:klxcoder/build-neural-network-samson-zhang.git
git branch -M main
git push -u origin main
Enumerating objects: 99, done.
Counting objects: 100% (99/99), done.
Delta compression using up to 16 threads
Compressing objects: 100% (96/96), done.
Writing objects: 100% (99/99), 19.45 MiB | 1.39 MiB/s, done.
Total 99 (delta 53), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (53/53), done.
remote: warning: See https://gh.io/lfs for more information.
remote: warning: File kaggle/input/digit-recognizer/train.csv is 73.22 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: warning: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To github.com:klxcoder/build-neural-network-samson-zhang.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

(nn) ┌──(klx㉿kali)-[~/build-neural-network-samson-zhang] (main)
└─$ 
```