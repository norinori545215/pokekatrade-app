# PokekaTrade App

A minimal Flask application. Use the invite code `TRIAL-2025-1234` to log in.

## Setup

Install Python and the required packages:

```bash
pip install -r requirements.txt
```

## Running the app

Start the development server:

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser and enter the invite code.

## Mercari graphs

The `/prices` page displays a sample Mercari price trend graph generated with `matplotlib`.
Reloading the page regenerates the chart.

Example command to fetch the page:

```bash
curl http://localhost:5000/prices
```

You can also open the URL in a browser to view the graph interactively.
