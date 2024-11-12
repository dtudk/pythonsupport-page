# DTU Python support homepage

Welcome to the DTU Python support development site.

Our homepage is hosted [here](https://pythonsupport.dtu.dk).

If you are a DTU student and want help with installing
packages for a course at DTU, please visit
[pythonsupport.dtu.dk](https://pythonsupport.dtu.dk).



## Building the documentation

To build the documentation in a controlled environment we recommend you
to use a virtual environment.
Subsequently, the required packages should be installed, and lastly the
documentation can be built.

The steps can be outlined like this:

1. Create a virtual environment (on a Linux box)

       python3 -m venv ps-page-env
       source ps-page-env/bin/activate

2. Install the requirements:

       python3 -m pip install -r requirements.txt sphinx-autobuild
       # currently there is a blocking dependency on some of the
       # packages listed in requirements.txt, however, since pip
       # will allow updating a package that breaks compatibility, we
       # can use this to our advantage. The documentation builds fine.
       # Only some non-used features will not work. So we should be fine.
       #    :fingers_crossed:
       python3 -m pip install -U "sphinx>=7.2.5"

3. Development server (optional)

       make livehtml

   This will open a local webserver that auto-reloads whenever you make 
   changes to the `rst` documentation or any files in the `docs/` directory.

4. Build documentation

       make

   Now the documentation is build and can be found in `build/html`.

5. Open the documentation:

       firefox build/html/index.html

   And you should be ready to see the just build documentation.

### Creating the `gifs`

There are some gifs used to show how the terminal looks like.

In order to create these one requires these small packages (which are javascript):

- `npm` (Node.js package manager)
- `terminalizer` (the script that generates GIFs from `yaml` files)

Once these are installed, simply do:

    make gifs

and the gifs should be created. The script will only create them once,
and keep them around. So this should only be required to be done once.


## Running Locally in Podman

You can easily run the site locally (and deployed) using containers. You'll need:
- `podman` (or `docker`)

Run the following:
```bash
podman build . --tag pythonsupport-page:dev
podman run --rm -it --cap-drop ALL --publish 3000:3000 pythonsupport-page:dev
```

To control things like cache headers, compression, healthcheck endpoint, and basic authentication, see the `static-web-server` environment variable reference: https://static-web-server.net/configuration/environment-variables/
