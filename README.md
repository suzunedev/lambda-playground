# lambda-playground

## Setup

```bash
$ cp .envrc.sample .envrc
$ direnv allow
```

## Go build

```bash
$ cd src/go-sample-zip
$ GOOS=linux GOARCH=amd64 go build -tags lambda.norpc -o bootstrap main.go
```

## Manual deploy

```bash
$ cd src/python-sample-zip
$ lambroll deploy
```
