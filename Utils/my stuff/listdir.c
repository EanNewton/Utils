       /*
	    You can list a directory containing 8 million files! But not with ls.

		I needed to list all files in a directory, but ls, find, and os.
		listdir all hung. This is my story.

		NOTE: there is no good reason that you should ever have 8 million files in the same directory, but if you do, this is your solution :-).

		LDR: Write a C program that calls the syscall getdents directly, with a large buffer size, ignore entries with inode == 0.

		Why doesn't ls work?

		ls and practically every other method of listing a directory (including python os.listdir, find .) rely on libc readdir(). 
		However readdir() only reads 32K of directory entries at a time, which means that if you have a lot of files in the same directory 
		(i.e. 500M of directory entries) it is going to take an insanely long time to read all the directory entries, especially on a slow disk. 
		For directories containing a large number of files, youâ€™ll need to dig deeper than tools that rely on readdir(). 
		You will need to use the getdents() syscall directly, rather than helper methods from libc.
		*/
	   
	   #define _GNU_SOURCE
       #include <dirent.h>     /* Defines DT_* constants */
       #include <fcntl.h>
       #include <stdint.h>
       #include <stdio.h>
       #include <unistd.h>
       #include <stdlib.h>
       #include <sys/stat.h>
       #include <sys/syscall.h>

       #define handle_error(msg) \
               do { perror(msg); exit(EXIT_FAILURE); } while (0)

       struct linux_dirent {
           unsigned long  d_ino;
           off_t          d_off;
           unsigned short d_reclen;
           char           d_name[];
       };

		// Increase buffer size to 5MB
       #define BUF_SIZE 1024*1024*5

       int
       main(int argc, char *argv[])
       {
           int fd;
           long nread;
           char buf[BUF_SIZE];
           struct linux_dirent *d;
           char d_type;

           fd = open(argc > 1 ? argv[1] : ".", O_RDONLY | O_DIRECTORY);
           if (fd == -1)
               handle_error("open");

           for (;;) {
               nread = syscall(SYS_getdents, fd, buf, BUF_SIZE);
               if (nread == -1)
                   handle_error("getdents");

               if (nread == 0)
                   break;

               printf("--------------- nread=%d ---------------\n", nread);
               printf("inode#    file type  d_reclen  d_off   d_name\n");
               for (long bpos = 0; bpos < nread;) {
                   d = (struct linux_dirent *) (buf + bpos);
                   printf("%8ld  ", d->d_ino);
                   d_type = *(buf + bpos + d->d_reclen - 1);
				   // Skip if inode == 0
                   if (dp->d_ino != 0) printf("%-10s ", (d_type == DT_REG) ?  "regular" :
                                    (d_type == DT_DIR) ?  "directory" :
                                    (d_type == DT_FIFO) ? "FIFO" :
                                    (d_type == DT_SOCK) ? "socket" :
                                    (d_type == DT_LNK) ?  "symlink" :
                                    (d_type == DT_BLK) ?  "block dev" :
                                    (d_type == DT_CHR) ?  "char dev" : "???");
                   printf("%4d %10jd  %s\n", d->d_reclen,
                           (intmax_t) d->d_off, d->d_name);
                   bpos += d->d_reclen;
               }
           }

           exit(EXIT_SUCCESS);
       }
