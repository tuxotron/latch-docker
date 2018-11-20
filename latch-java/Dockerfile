FROM maven:3.5.4-jdk-8-alpine AS build

RUN mkdir -p /app/src
COPY pom.xml /app/
COPY src /app/src/
RUN mvn -f /app/pom.xml clean package


FROM gcr.io/distroless/java

COPY docker-conf/group /etc/group
COPY docker-conf/passwd /etc/passwd
USER app

COPY --from=build /app/target/latch-0.0.1-SNAPSHOT.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
