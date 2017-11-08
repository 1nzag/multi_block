all: multi_block

multi_block: find_db.o nfqnl_test.o
	gcc -o multi_block find_db.o nfqnl_test.o -lnetfilter_queue

find_db.o: find_db.c find_db.h
	gcc -c -o find_db.o find_db.c

nfqnl_test.o: nfqnl_test.c find_db.h
	gcc -c -o nfqnl_test.o nfqnl_test.c -lnetfilter_queue

clean:
	rm *.o

