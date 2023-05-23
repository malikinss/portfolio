NAME = sorted_list
USING_LIB = dlist
USING_LIB_PATH = ../dlist
TARGET = $(NAME).out
OBJ = $(NAME).o $(NAME)_test.o $(USING_LIB_PATH)/dlist.o
CC = gcc
CFLAGS =-I$(USING_LIB_PATH) -ansi -pedantic-errors -Wall -Wextra
VLG = valgrind --leak-check=yes --track-origins=yes

.PHONY : run clean release debug all

all :	debug

debug : CFLAGS += -g
debug :	$(OBJ)
		$(CC) $(CFLAGS) -o $(TARGET) $(OBJ) 

release : CFLAGS += -DNDEBUG -O3
release : $(OBJ)
		$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

clean :
		rm -f $(TARGET) $(OBJ)

run :
		./$(TARGET)

vlg :
		$(VLG) ./$(TARGET)

