from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
import requests
from django.shortcuts import render
from .models import IndicatorData
import json
from django.db import connection

@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def updateTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"})
    
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"})
    
    task.delete()
    return Response({"message": "Task deleted successfully"})

@api_view(['POST'])
def fetch_indicator_dynamic(request):
    import requests

    indicator = request.data.get("indicator")
    countries = request.data.get("countries")
    start_year = int(request.data.get("start_year", 2000))
    end_year = int(request.data.get("end_year", 2025))

    if not indicator or not countries:
        return Response({"error": "indicator and countries are required"}, status=400)

    base_url = "https://api.worldbank.org/v2/country/{}/indicator/{}?format=json&per_page=2000"

    results = []
    saved_count = 0

    for country in countries:
        url = base_url.format(country, indicator)
        response = requests.get(url).json()

        if len(response) < 2:
            continue

        country_data = []

        for entry in response[1]:
            year = int(entry.get("date", 0))
            if not (start_year <= year <= end_year):
                continue

            value = entry.get("value")
            country_name = entry["country"]["value"]

            if value is None:
                continue

            exists = IndicatorData.objects.filter(
                country=country,
                indicator_code=indicator,
                year=year
            ).exists()

            if not exists:
                IndicatorData.objects.create(
                    country=country,
                    country_name=country_name,
                    indicator_code=indicator,
                    indicator_name="",
                    year=year,
                    value=value
                )
                saved_count += 1

            country_data.append({
                "year": year,
                "value": value,
                "country": country_name
            })

        if country_data:
            results.append({
                "country": country,
                "data": sorted(country_data, key=lambda x: x["year"])
            })

    flat_data = []
    for r in results:
        for d in r["data"]:
            flat_data.append({
                "country": r["country"],
                "year": d["year"],
                "value": d["value"]
            })

    return Response({
        "indicator": indicator,
        "saved_records": saved_count,
        "data": flat_data
    })

@api_view(['POST'])
def load_from_database(request):
    indicator = request.data.get("indicator")
    countries = request.data.get("countries")
    start_year = int(request.data.get("start_year", 2000))
    end_year = int(request.data.get("end_year", 2025))

    if not indicator or not countries:
        return Response({"error": "Missing fields"}, status=400)

    db_results = IndicatorData.objects.filter(
        indicator_code=indicator,
        country__in=countries,
        year__gte=start_year,
        year__lte=end_year
    ).order_by("year")

    formatted = {}
    for row in db_results:
        formatted.setdefault(row.country, []).append({
            "year": row.year,
            "value": row.value,
            "country": row.country_name
        })

    results = [{"country": k, "data": v} for k, v in formatted.items()]

    return Response({"results": results})
    
def home(request):
    return render(request, "home.html")

def tasksUI(request):
    return render(request, "tasks_ui.html", {
        "explanation": "This dashboard lets users create, edit, and delete tasks just like any real project management tool. Although the page looks simple, every action communicates with the backend using REST APIs - i mean the data updates in the database without refreshing the page",
        "steps": [
            "When a task is added, edited, or deleted, the page sends a REST API request to the server",
            "Django REST Framework receives the request and updates the database",
            "The UI uses JavaScript to instantly refresh the table, creating a smooth experience",
            "This fulfills Assignment Requirement #1 — A basic CRUD (Create, Read, Update, Delete) functionality via REST APIs"
        ]
    })
    
def fetchDataUI(request):
    return render(request, "fetch_data.html", {
        "explanation": "This feature connects to the official World Bank API to fetch real global economic data. The system imports data according to selected indicators, it ensures the data is not duplicated into Database (It ignores the data rows which are already present in database - we have implemented unique constratints on the table) and saves them into our database, similar to how real applications sync data from third-party services",
        "steps": [
            "User selects an economic metric (GDP, Population or Unemployement) and triggers import",
            "The backend requests real data from the World Bank public API",
            "Data is cleaned, filtered by year, and stored only if not already saved (Duplicates are avoided)",
            "This fulfills Assignment Requirement #2 - At least one API integration example (either pulling data from or sending data to a third-party API)"
        ]
    })

def analyticsDashboard(request):
    return render(request, "analytics.html", {
        "explanation": "This module converts saved database records (From Previous module where we fetched data from world bank API) into visual insights using interactive chart. Instead of calling the external API again, the system reads directly from the database",
        "steps": [
            "User selects countries, Data (Economic Indicator) type and year range for analysis. We have implemented range selection using datepicker UI component",
            "The backend loads filtered data from the database",
            "The data is displayed visually using Chart.js",
            "This fulfills Assignment Requirement #3 - A simple data visualization or reporting feature, showcasing data retrieved from your database"
        ]
    })