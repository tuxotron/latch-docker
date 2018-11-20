FROM golang:1.11 as build

WORKDIR /go/src/app
COPY main.go .

RUN go get -d -v ./... 
RUN go install -v ./...

FROM gcr.io/distroless/base

COPY docker-conf/group /etc/group
COPY docker-conf/passwd /etc/passwd
USER app

COPY --from=build /go/bin/app /
COPY templates /templates
EXPOSE 8081

CMD ["/app"]