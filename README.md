A starting point for a Flask API backend

## Development Environment

The development environment uses [Docker](http://www.docker.com/) and [Fig](http://orchardup.github.io/fig/). This makes it super easy to get up and running with a configuration that would closely mirror production. A [Vagrant](http://www.vagrantup.com/) config file is included for operating systems that cannot yet run Docker natively.

With Docker/Fig/Vagrant installed, use the following steps to launch for the first time:

* `vagrant up` - from within the project root to build the Ubuntu VM with Docker and Fig automatically installed. If you're already using Linux, you can skip this step and just install Docker and Fig on your system.
* `fig up` to start the web app. This will download and provision two containers: one running PostgreSQL and one running the Flask app. This will take a while, but once it completes subsequent launches will be much faster. (NOTE: if you are using the Vagrant VM that was provisioned in the first step, change into the `/vagrant` directory before running `fig up`.)
* When `fig up` completes, the app should be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000). (NOTE: if running commands within the Vagrant VM that was provisioned in the first step, the app can be found at: [http://192.168.13.81:5000](http://192.168.13.81:5000))


## Environment Variables

There are just a couple of configurations managed as environment variables. In the development environment, these are injected by Fig and managed in the `fig.yml` file.

* `DATABASE_URL` - This is the connection URL for the PostgreSQL database. It is not used in the **development environment**.
* `DEBUG` - This toggle debug mode for the app to True/False.
* `PORT` - This controls the port the API will serve from. If omitted, the default is 5000. If the port is changed in the **development environment**, and you are using a Vagrant VM, the port mapping in the `Vagrantfile` will also need to be updated to match.
* `SECRET_KEY` - This is a secret string that you make up. It is used to encrypt and verify the authentication token on routes that require authentication.


## Project Organization

* Application-wide settings are stored in `settings.py` at the root of the repository. These items are accessible on the `config` dictionary property of the `app` object. Example: `debug = app.config['DEBUG']`
* The directory `/app` contains the API application
* URL mapping is managed in `/app/urls.py`
* Functionality is organized in packages. Example: `/app/users` or `/app/utils`.
