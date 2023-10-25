# Use an official Alpine Linux as a parent image
FROM alpine:latest

# Install stress-ng
RUN apk --no-cache add stress-ng
RUN apk --no-cache add iperf

# Set an entry point
CMD ["/bin/sh"]