/path/to/inc_backups/* {
    daily
    missingok
    rotate 1
    create
    compress
    delaycompress
    notifempty
    dateext
    dateformat -%Y%m%d
    lastaction
        mv -f /path/to/inc_backups/* /path/to/inc_old_backups/
    endscript
}
