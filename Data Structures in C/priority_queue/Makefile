NAME = pqueue
USING_LIB1 = dlist
USING_LIB1_PATH = ../dlist
USING_LIB2 = sorted_list
USING_LIB2_PATH = ../sorted_list
TARGET = $(NAME).out
OBJ = $(NAME).o $(NAME)_test.o $(USING_LIB1_PATH)/$(USING_LIB1).o $(USING_LIB2_PATH)/$(USING_LIB2).o
CC = gcc
CFLAGS =-I$(USING_LIB1_PATH) -I$(USING_LIB2_PATH) -ansi -pedantic-errors -Wall -Wextra
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

