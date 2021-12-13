#!/bin/sh

# Also run `chmod +x run.sh` in command line
# TODO: Change by environment
sessionKey="changeme"
clientId="changeme"
clientSecret="changeme"

SESSION_SIGNING_KEY=$sessionKey STREAMLABS_CLIENT_NAME=$clientId STREAMLABS_CLIENT_SECRET=$clientSecret python app.py
