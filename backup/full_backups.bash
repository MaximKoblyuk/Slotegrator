/path/to/full_backups/* {
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
        mv -f /path/to/full_backups/* /path/to/full_old_backups/
    endscript
}

