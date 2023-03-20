a= ['accept', 'accept4', 'arch_prctl', 'bind', 'capget', 'capset', 'chdir', 'chown', 'clone', 'close', 'connect', 'creat', 'dup2', 'epoll_create', 'epoll_ctl', 'epoll_wait', 'execve', 'faccessat', 'fcntl', 'fstat', 'fstatfs', 'futex', 'getdents', 'getdents64', 'getpgrp', 'getppid', 'getrlimit', 'getsockopt', 'ioctl', 'listen', 'lstat', 'mkdir', 'mmap', 'mprotect', 'newfstatat', 'open', 'openat', 'poll', 'prctl', 'pread64', 'read', 'readv', 'recvfrom', 'rt_sigaction', 'rt_sigprocmask', 'rt_sigreturn', 'sendto', 'setgid', 'setgroups', 'setsid', 'setsockopt', 'setuid', 'shutdown', 'socket', 'socketpair', 'stat', 'uname', 'wait4', 'write', 'writev']
b= ['accept', 'accept4', 'access', 'arch_prctl', 'bind', 'brk', 'chdir', 'chown', 'clone', 'close', 'connect', 'creat', 'dup2', 'epoll_create', 'epoll_ctl', 'epoll_wait', 'eventfd2', 'execve', 'exit_group', 'fchmodat', 'fcntl', 'fstat', 'futex', 'getcwd', 'getdents', 'getegid', 'geteuid', 'getgid', 'getpgrp', 'getpid', 'getppid', 'getrlimit', 'getsockname', 'getsockopt', 'gettid', 'getuid', 'io_setup', 'ioctl', 'listen', 'lseek', 'lstat', 'mkdir', 'mmap', 'mprotect', 'munmap', 'newfstatat', 'open', 'openat', 'pipe2', 'poll', 'prctl', 'pread64', 'pwrite64', 'read', 'readv', 'recvfrom', 'recvmsg', 'rt_sigaction', 'rt_sigprocmask', 'rt_sigreturn', 'rt_sigsuspend', 'sendmsg', 'sendto', 'set_robust_list', 'set_tid_address', 'setgid', 'setgroups', 'setitimer', 'setsid', 'setsockopt', 'setuid', 'shutdown', 'socket', 'socketpair', 'stat', 'statfs', 'times', 'umask', 'uname', 'unlink', 'unlinkat', 'wait4', 'write', 'writev']
diff = set(b)- set(a)
print(diff)

diff =
"fchmodat",
"sendmsg",
"geteuid",
"recvmsg",
"unlink",
"times",
"munmap",
"brk",
"getcwd",
"io_setup",
"getegid",
"umask",
"pwrite64",
"eventfd2",
"getuid",
"rt_sigsuspend",
"access",
"exit_group",
"getsockname",
"set_robust_list",
"lseek",
"pipe2",
"getpid",
"getgid",
"statfs",
"unlinkat",
"gettid",
"set_tid_address",
"setitimer"
