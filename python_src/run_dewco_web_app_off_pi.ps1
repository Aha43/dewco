#!/usr/bin/env pwsh

$env:__sense_hat_module__ = "dewco.systems.sensehat.dummy_sense_hat"
py ./dewco_web_app.py
