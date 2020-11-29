
## Compilation steps
links to learn about gpu compilation:
- https://lists.quantum-espresso.org/pipermail/users/2016-August/036172.html

Note on google colab:
- The os.system("") is able to compile the normal version of QE as follows:
  - os.system("git clone https://github.com/QEF/q-e.git")  #Clone the QE git
  - os.system("apt-get install -y libfftw3–3 libfftw3-dev libfftw3-doc") #Install the dependencies
  - os.system("%cd q-e") #enter the q-e folder
  - os.system("DFLAGS = ‘-D__OPENMP -D__FFTW3 -D__MPI -D__SCALAPACK’ FFT_LIBS = ‘-lfftw3’ ./configure --enable-openmp") #run the configure file
  - os.system("make pw") #make the pw file
