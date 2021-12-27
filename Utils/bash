# Full ls with color
alias lsf='ls -ACFRghs --color'
# DNS Info
alias dnsi='systemd-resolve --status'

# Rename all files in a directory based on patterns. E.g. "My" becomes "Our"
dir | rename-item -NewName {$_.name -replace "My","Our"}

# WARNING: KILLS ALL PROCESSESS ASSOCIATED TO CURRENT DIRECTORY
# For when rm -rf fails due to ""device locked or busy"" . 
#    awk grabs the PIDs.
#    tail gets rid of the pesky first entry: ""PID"".
#    xargs executes kill -9 on the PIDs. 
# The -r / --no-run-if-empty, prevents kill command failure, in case lsof did not return any PID.
lsof +D ./ | awk '{print $2}' | tail -n +2 | xargs -r kill -9
