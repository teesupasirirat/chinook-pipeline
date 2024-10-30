# Databricks notebook source
import pandas as pd
import math

input_file = "/Workspace/Users/narumopi@ais.co.th/track_small.csv"
output_file = "/Workspace/Users/narumopi@ais.co.th/output_small.csv"

# Extract
tracks = pd.read_csv(input_file)

# Transform
tracks['UnitPrice'] = tracks['UnitPrice'].apply(lambda x:math.ceil(x))

# Load
tracks.to_csv(output_file, index=False)
