BIrodmann Data Tool
==
- git clone
- docker build -t birodmann .
- docker run -v "$(pwd)"/Files:/Brodmann/BIrodmann/Files birodmann --create_report "report_agg_user" --conf "Files/conf/application.conf"

- configuration file: under Files/conf/application.conf