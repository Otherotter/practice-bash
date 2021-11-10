#!/bin/bash
dir_to_backup=$1
backup_dir=~/backups/
backup_log_file=~/backups/backup_logs

echo "$(date) e"
mkdir $backup_dir
echo "$(date -R): Creating backup directory for $dir_to_backup" >> $backup_dir
echo "$(date -R) : Copying Files for $dir_to_backups" >> $backup_log_file
cp -rv $dir_to_backup $backup_dir >> $backup_log_file
echo "$(date -R): Finished copying $dir_to_backups" >> $backup_log_file
