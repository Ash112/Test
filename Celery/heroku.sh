#!/bin/bash
gunicorn app:app --daemon
python main.py