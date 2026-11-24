from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food
from .serialisers import FoodSerializer
# Create your views here.



#  FRONTEND VIEWS 

def food_page(request):
    query = request.GET.get("q", "").strip()
    foods = Food.objects.all().order_by("-created_at")

    if query:
        foods = foods.filter(name__icontains=query)

    return render(
        request,
        "foods/food_list.html",
        {"foods": foods, "query": query},
    )


def food_create_page(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        price_text = request.POST.get("price", "").strip()
        description = request.POST.get("description", "").strip()

        if not name:
            messages.error(request, "Food name is required.")
            return render(request, "foods/food_form.html", {"food": None})

        try:
            price = int(price_text)
            if price < 0:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, "Enter a valid price of 0 UGX or more.")
            return render(
                request,
                "foods/food_form.html",
                {"food": None},
            )

        Food.objects.create(
            name=name,
            price=price,
            description=description,
        )
        messages.success(request, "Food item added successfully.")
        return redirect("food-page")

    return render(request, "foods/food_form.html", {"food": None})


def food_update_page(request, pk):
    food = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        price_text = request.POST.get("price", "").strip()
        description = request.POST.get("description", "").strip()

        if not name:
            messages.error(request, "Food name is required.")
            return render(request, "foods/food_form.html", {"food": food})

        try:
            price = int(price_text)
            if price < 0:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, "Enter a valid price of 0 UGX or more.")
            return render(request, "foods/food_form.html", {"food": food})

        food.name = name
        food.price = price
        food.description = description
        food.save()
        messages.success(request, "Food item updated successfully.")
        return redirect("food-page")

    return render(request, "foods/food_form.html", {"food": food})


def food_delete_page(request, pk):
    food = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        food.delete()
        messages.success(request, "Food item deleted.")
        return redirect("food-page")

    return render(
        request,
        "foods/food_confirm_delete.html",
        {"food": food}
    )


#  REST API VIEWS 

@api_view(["GET"])
def home_view(request):
    return Response(
        {"message": "Food Management System API is running."},
        status=status.HTTP_200_OK,
    )


@api_view(["GET", "POST"])
def food_view(request):
    if request.method == "GET":
        foods = Food.objects.all().order_by("-created_at")
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def food_detail_view(request, pk):
    food = get_object_or_404(Food, pk=pk)

    if request.method == "GET":
        serializer = FoodSerializer(food)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = FoodSerializer(food, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    food.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
