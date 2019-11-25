CC=g++
CFLAGS = -I. -O2 -lm
#CFLAGS = -O3 -w -DLINUX -fPIC -I. -lm

namsmake: nams.o hungarian.o Main.o awts.o
	$(CC) -o nams nams.o hungarian.o Main.o awts.o $(CFLAGS)
