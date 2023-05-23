NAME = scheduler
USING_LIB1 = pqueue
USING_LIB1_PATH = ../$(USING_LIB1)
USING_LIB2 = sorted_linked_list
USING_LIB2_PATH = ../$(USING_LIB2)
USING_LIB3 = uid
USING_LIB3_PATH = ../uid
USING_LIB4 = dlist
USING_LIB4_PATH = ../dlist
USING_LIB5 = task
USING_LIB5_PATH = ../task
TARGET = $(NAME).out
OBJ = $(NAME).o $(NAME)_test.o $(USING_LIB1_PATH)/$(USING_LIB1).o $(USING_LIB2_PATH)/$(USING_LIB2).o $(USING_LIB3_PATH)/$(USING_LIB3).o $(USING_LIB4_PATH)/$(USING_LIB4).o $(USING_LIB5_PATH)/$(USING_LIB5).o
CC = gcc
CFLAGS =-I$(USING_LIB1_PATH) -I$(USING_LIB2_PATH) -I$(USING_LIB3_PATH) -I$(USING_LIB4_PATH) -I$(USING_LIB5_PATH) -ansi -pedantic-errors -Wall -Wextra
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

