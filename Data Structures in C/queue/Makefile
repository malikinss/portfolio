NAME=queue
TARGET=$(NAME).out
OBJ=slinkedlist.o $(NAME).o $(NAME)_test.o
CC=gcc
CFLAGS=-ansi -pedantic-errors -Wall -Wextra
VLG=valgrind --leak-check=yes --track-origins=yes

.PHONY : run clean release debug all

all :	debug

debug : CFLAGS+=-g
debug :	$(OBJ)
		$(CC) $(CFLAGS) -o $(TARGET) $(OBJ) 

release : CFLAGS+=-DNDEBUG -O3
release : $(OBJ)
		$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

clean :
		rm $(TARGET) $(OBJ)

run :
		./$(TARGET)

vlg :
		$(VLG) ./$(TARGET)

