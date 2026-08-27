FROM eclipse-temurin:8-jre

ENV JYTHON_VERSION=2.7.3


ADD https://repo1.maven.org/maven2/org/python/jython-standalone/${JYTHON_VERSION}/jython-standalone-${JYTHON_VERSION}.jar /opt/jython.jar

WORKDIR /app
COPY exemplo1.py exemplo2.py ./


CMD ["sh", "-c", "java -jar /opt/jython.jar exemplo1.py && echo '\n----------------------------------------\n' && java -jar /opt/jython.jar exemplo2.py"]