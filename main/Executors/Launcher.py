from main.Factories.Reports.FactoryReport import FactoryReport
from main.Factories.Graphs.FactoryGraph import FactoryGraph
from main.Config.ConfigUtils import ConfigUtils
from main.Config.LoggerConfig import LoggerConfig
import argparse


def main():
    try:
        logger = LoggerConfig().get_logger()
        parser = argparse.ArgumentParser(description='Build & sketch reports')

        parser.add_argument('--create_report', help='Create new csv report')
        parser.add_argument('--sketch_report', help='Create new csv report')
        parser.add_argument('--conf', help='Configuration file path')
        args = parser.parse_args()

        if args.conf:
            conf = ConfigUtils(args.conf).get_conf()
            logger.info(f"Loaded configuration file: {conf}")
        else:
            raise Exception("Please provide conf file")

        if args.create_report:
            report = FactoryReport(args.create_report,conf,logger).build()
            report.execute()

        if args.sketch_report:
            graph = FactoryGraph(args.sketch_report,conf,logger).build()
            graph.execute()

    except Exception as e:
        logger = LoggerConfig().get_logger()
        logger.error(f'Error occurred:', exc_info=True)


if __name__ == "__main__":
    main()



