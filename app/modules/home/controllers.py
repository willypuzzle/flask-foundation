from flask import Blueprint, render_template, flash, request, redirect, url_for

from app.extensions import cache

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod = Blueprint('home', __name__, url_prefix='/')


@mod.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')