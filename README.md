DTU Python support homepage
===========================

Welcome to the DTU Python support development site.

Our homepage is hosted [here](https://pythonsupport.dtu.dk).

If you are a DTU student and want help with installing
packages for a course at DTU, plese visit 
[pythonsupport.dtu.dk](https://pythonsupport.dtu.dk).

Running Locally in Podman
-------------------------

You can easily run the site locally (and deployed) using containers. You'll need:
- `podman` (or `docker`)

Run the following:
```bash
podman build . --tag pythonsupport-page:dev
podman run --rm -it --cap-drop ALL --publish 3000:3000 pythonsupport-page:dev
```

To control things like cache headers, compression, healthcheck endpoint, and basic authentication, see the `static-web-server` environment variable reference: https://static-web-server.net/configuration/environment-variables/
