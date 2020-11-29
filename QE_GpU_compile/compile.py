import os


"""
Installing the Normal version of quantum ESPRESSO

 #Clone the QE git
 #Install the dependencies
 #enter the q-e folder
 #run the configure file
 #make the pw file

"""
def compile_normal():
    os.system("git clone https://github.com/QEF/q-e.git")  #Clone the QE git
    os.system("apt-get install -y libfftw3–3 libfftw3-dev libfftw3-doc") #Install the dependencies
    os.system("%cd q-e") #enter the q-e folder
    os.system("DFLAGS = ‘-D__OPENMP -D__FFTW3 -D__MPI -D__SCALAPACK’ FFT_LIBS = ‘-lfftw3’ ./configure --enable-openmp") #run the configure file
    os.system("make pw") #make the pw file

def compile_gpu():
    pass
