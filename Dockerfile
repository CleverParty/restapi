FROM golang:alpine

# Set necessary environmet variables needed for our image
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

RUN go get github.com/gorilla/mux
RUN go build -o .


RUN cp /build/main .
EXPOSE 3007

# Command to run when starting the container
CMD ["/dist/main"]