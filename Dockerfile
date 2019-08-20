FROM python:3.7
ARG BRODMANN_HOME=/Brodmann/BIrodmann
ADD ./main/ ${BRODMANN_HOME}/main
ADD requirements.txt /
RUN pip install -r requirements.txt
WORKDIR ${BRODMANN_HOME}
ENTRYPOINT ["python","-m", "main.Executors.Launcher"]

