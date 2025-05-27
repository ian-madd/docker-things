# Add NAME variable using ENV variable

```sh
docker build -t hello-env .
```

The `NAME` variable is defined in the Dockerfile.
There's also a default defined in `app.py`.

Define the `NAME` variable with docker run:

```sh
docker run --env NAME=Alice hello-env
```

