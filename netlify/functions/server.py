import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from api.app import app

if __name__ == "__main__":
    app.run()
