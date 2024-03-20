# Start by building base
FROM python:3.11.8-slim as builder

# For convention, copy into /opt/
ENV HOME_DIR=/opt/api

# Change location of poetry install
ENV POETRY_INSTALL_LOCATION=${HOME_DIR}/.venv/bin
ENV PATH=${POETRY_INSTALL_LOCATION}${PATH:+":$PATH"}

# Run updates
RUN apt-get update --no-install-recommends \
  && apt-get install --no-install-recommends --yes \
  && apt-get autoremove \
  && apt-get clean \
  && mkdir --parents ${POETRY_INSTALL_LOCATION}

WORKDIR ${HOME_DIR}

# Do a poetry install
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --only=main --no-root

# Cache remaining files
COPY app/ ${HOME_DIR}/app/


# ----------------------------- SECOND STAGE -----------------------------

# Run everything distroless
FROM gcr.io/distroless/python3-debian12 as prod

# For convention, copy into /opt/
ENV HOME_DIR=/opt/api

# Change location of poetry install
ENV POETRY_INSTALL_LOCATION=${HOME_DIR}/.venv/bin
ENV PYTHON_PACKAGES_LOC=${HOME_DIR}/.venv/lib/python3.11/site-packages
ENV PATH=${POETRY_INSTALL_LOCATION}${PATH:+":$PATH"}

# NOTE - How to fix this? This is needed b/c distroless uses /usr/bin vs /usr/local/bin
COPY --from=builder /usr/local/ /usr/local/

# Copy over relevant layers
COPY --from=builder ${PYTHON_PACKAGES_LOC} ${PYTHON_PACKAGES_LOC}
COPY --from=builder ${POETRY_INSTALL_LOCATION} ${POETRY_INSTALL_LOCATION}
COPY --from=builder ${HOME_DIR}/app/ ${HOME_DIR}/app/

# Needed for correct installation
ENV PYTHONPATH=${PYTHON_PACKAGES_LOC}${PYTHONPATH:+":$PYTHONPATH"}

WORKDIR ${HOME_DIR}

# TODO - fix relative imports
ENTRYPOINT ["/usr/bin/python"]
CMD ["app/run.py"]
