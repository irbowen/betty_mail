# betty_mail

A quick and dirty script to send an email reminder to everyone on betty's wall of shame.

Shame: https://chezbetty.eecs.umich.edu/shame

After you clone, edit mailmerge_template.txt and mailmerge_server.conf to use your uniqname / email.

Then, just type
```bash
./run.sh
```

This gives you a preview of the emails to be sent. If everything looks good, edit run.sh and replace --no-dry-run with --dry-run, and run again. Your emails should be sending!
