from flask import request, redirect, url_for
from traits import render, view
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from traits.query_builder import QueryBuilder
from models.example_model import ExampleModel

exampleModel = ExampleModel()

class TestController:

  def index(self):
    data = exampleModel.builder().raw('SELECT * FROM examples').get()
    return render(view('tests/index'), data=data)