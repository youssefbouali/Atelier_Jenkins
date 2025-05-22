FROM scratch

COPY test.txt /test.txt

CMD ["cat", "/test.txt"]