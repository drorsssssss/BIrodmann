BIrodmann Data Tool
==

The BIrodmann Data Tool gives the user the ability to get insights regarding
GitHub user events

This version support the following features:
- Aggregated insights regarding GitHub user by time resolution and number of events they did
- Sketch tool for visualization

<h3>Setup Instructions</h3>
 
 - Download and install Docker for Ubuntu/CentOS etc
 - git clone https://github.com/drorsssssss/BIrodmann.git
 
 - cd ./BIrodmann
 
 - docker build -t birodmann .
 
 - docker run -v "$(pwd)"/Files:/Brodmann/BIrodmann/Files birodmann --create_report "report_agg_user" --sketch_report "user_count_events" --conf "Files/conf/application.conf"



<h4>Docker run parameters</h4>
 
 - "--create_report" parameter: Expect the report name to be calculated. Currently support "report_agg_user"
 
 - "--sketch_report" parameter: Expect the graph name to be sketched. Currently support "user_count_events"
 
 - "--conf" parameter:(Mandatory) Expect a configuration file (.conf). See reference in Files/conf/application.conf

<h5>Configuration file</h5>
The BIrodmann app uses HOCON configuration format which is much more user-friendly than other conf formats.

The parameters:
 - App.Report.report_name: Report name
 - App.Report.input_path: The input files to be processed
 - App.Report.filter_columns_json: Filter based on column name and a value. The format: """{"type":"CommitCommentEvent"}"""
 - App.Report.agg_time_resolution: The time resolution for the aggregation (hour/day/month/year)
 - App.Report.topn: Number of users to be presented per aggregation
 - App.Report.persist.target: The target for result file persistence. Currently support only local. In the future  
   could support Google Bucket/ Amazon S3 etc
 - App.Report.persist.file_type: Result file type. Currently support only csv
 - App.Report.persist.path: The output file path
 - App.Report.download_files.concurrency_level: Number of cpus for concurrency level when performing url     
   requests(Default=5)
 - App.Report.download_files.is_active: Enable/Disable the files downloading from the url
 - App.Report.download_files.clear_input_path: Enable/Disable input files directory before downloading new ones
 - App.Report.download_files.urls: A list of urls to download the files from
 
 - App.Graph.graph_name: Graph name
 - App.Graph.input_path: The input path (Usually the result csv from report conf) for the graph sketch
 - App.Graph.output_path: The output path for the graph (pdf file) 
 
 
 
 <h4>Unit Testing</h4>
 
 In order to run the unit tests, please follow these steps:
 
 - Go to Brodmann/BIrodmann/test/unit_tests/test_report_agg_user
 
 - Edit test_report_agg_user.py - Change the base path parameter (BASE_PATH)
 
 - Run test_report_agg_user.py
 
 