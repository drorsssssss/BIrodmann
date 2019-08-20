from main.Factories.Persistence.IPersistenceDF import IPersistence


class PersistLocalFS(IPersistence):
    def __init__(self,df,conf,logger):
        self.df=df
        self.conf=conf
        self.logger=logger

    def persist(self):
        try:
            output_path=self.conf.get_string("App.Reports.persist.path")
            file_type=self.conf.get_string("App.Reports.persist.file_type")
            getattr(self.df,file_type)(output_path,index=False)

        except Exception as e:
            self.logger.error(f'Error occurred:', exc_info=True)
            raise Exception(f"Error occurred while persisting: {e}")


