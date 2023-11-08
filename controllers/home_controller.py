from flask import render_template, request, redirect, url_for

class HomeController:
  def index(self):
    return render_template('layouts/main.html')
